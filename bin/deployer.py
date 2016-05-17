import boto3
import os
import shutil
import datetime
import requests


class S3_Deployer():

	def __init__(self, bucket, directory, backup=None, url_verify=None):
		self.client = boto3.client('s3')
		self.bucket = bucket
		self.directory = directory
		self.backup = backup
		self.url_verify = url_verify

	def deploy(self):
		# full deployment process.
		self.backup_bucket()
		self.deploy_to_bucket()
		if self.url_verify is not None: self.verify_url()

	def backup_bucket(self):
		# Backup from bucket to backup directory
		print "Backing up current bucket contents...\n"
		if os.path.exists(self.backup):
			print "Removing current backup directory: " + self.backup
			shutil.rmtree(self.backup)

		self.backup_subdir = self.backup + os.sep + str(datetime.date.today())
		print "Creating backup directory: " + self.backup_subdir
		os.makedirs(self.backup_subdir)

		file_paths = []
		for obj in self.client.list_objects(Bucket=self.bucket)['Contents']:
			remote_path = obj['Key']
			local_path = self.backup_subdir + os.sep + remote_path
			local_directory_name = os.path.dirname(local_path)
			if local_path[-1] == os.sep or not os.path.exists(local_directory_name):
				print "Creating directory: " + local_directory_name
				os.makedirs(local_directory_name)
			try:
				self.client.download_file(self.bucket, remote_path, local_path)
				print "File Downloaded: " + remote_path
			except OSError: pass # trying to download directory, pass
		print "Backup Complete.\n"

	def deploy_to_bucket(self, bucket_subdir=""):
		# Deploy from directory to bucket
		# use bucket_subdir to deploy to bucket subdirectory of same name
		print "Uploading to " + self.bucket + " from " + self.directory + "..."
		errors = 0
		for local_path in self.get_file_paths(self.directory):
			remote_path = bucket_subdir + local_path.replace(self.directory, "")
			try:
				print "remote: " + remote_path
				self.client.upload_file(local_path, self.bucket, remote_path, ExtraArgs={'ACL': 'public-read'})
				print "uploaded: " + local_path
			except:
				print "UPLOAD FAILURE: " + local_path
				errors += 1

		if errors > 0:
			print str(errors) + " FAILURES DETECTED."
			if self.backup is not None:
				self.prompt_revert()
		else:
			print "Deploy Complete.\n"

	def verify_url(self):
		# verify status of site dependent on bucket
		status_code = self.get_status(self.url_verify)
		if status_code is 200:
			cleanup = raw_input("Remove Backup Directory? (y/n) ").strip()
			if cleanup in ['y','Y','yes','Yes','YES']:
				print "Removing backup directory: " + self.backup
				shutil.rmtree(self.backup)
			print "BIG SUCCESS."
		else:
			self.prompt_revert()
			self.get_status(self.url_verify)

	def prompt_revert(self):
		# prompt option to revert to previous files.
		redeploy = raw_input("Redeploy Backup files? (y/n) ").strip()
		if redeploy in ['y','Y','yes','Yes','YES']:
			print "Reverting to backup..."
			self.revert_to_backup()

	def revert_to_backup(self):
		# Push backup files back to bucket
		print "Reverting " + self.bucket + "..."
		errors = 0
		for local_path in self.get_file_paths(self.backup_subdir):
			remote_path = local_path.replace(self.backup_subdir,"")
			try:
				self.client.upload_file(local_path, self.bucket, remote_path, ExtraArgs={'ACL': 'public-read'})
				print "reverted: " + local_path
			except:
				print "FAILURE: " + local_path
				errors += 1
		if errors > 0:
			print str(errors) + " FAILURES DETECTED."
		else:
			print "Bucket back to previous."

	def get_file_paths(self, directory):
		# returns paths to all files within directory
		paths = []
		for (dirpath, dirnames, filenames) in os.walk(directory):
			for name in filenames:
				paths.append(dirpath + os.sep + name)

		return paths

	def get_status(self, url):
		# get http status from url
		status = requests.head(url).status_code
		print "(" + url + ") - status: " + str(status)
		return status




def main():
	# BUCKET_NAME = raw_input("Enter Bucket Name: ")
	BUCKET_NAME = 'pokitdok-apidocs'
	# BUCKET_NAME = 'pd-testbucket'

	# DIRECTORY = raw_input("Enter Directory Name: ")
	DIRECTORY = "./build"

	# BACKUP_DIR = raw_input("Enter Backup Directory Name: ")
	BACKUP_DIR = "./BACKUP"

	# VERIFY_URL = raw_input("Enter Verification URL (we'll check this for http status after deploy): ")
	VERIFY_URL = "https://platform.pokitdok.com/documentation/v4/"

	# build doc files to ./build directory
	build_files_yn = raw_input("Build latest documentation files? (y/n) ").strip()
	if build_files_yn in ['y','Y','yes','Yes','YES']:
		print "Building latest files..."
		os.system("bundle exec middleman build")
		print "Build Complete.\n"

	S3_Deployer(BUCKET_NAME, DIRECTORY, BACKUP_DIR, VERIFY_URL).deploy()


if __name__ == "__main__": 
	main()