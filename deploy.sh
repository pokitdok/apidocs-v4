#!/bin/bash
# This program follows the deployment process for API Documentation
set -e

# Make sure we're on the right branch and up to date
git checkout dev
git pull origin dev

echo "Enter release tag, followed by [ENTER]: "
read tag_name

git checkout -b "$tag_name"
echo "Created release branch $tag_name with commits different from master:"

git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)%Creset' --abbrev-commit --date=relative master.."$tag_name" | grep -v "Merge"

echo "Enter staging bucket name, followed by [ENTER]: "
read staging

echo "Building docs..."
docker run -t -v "$PWD:/app" ruby:2.3 /app/build.sh

echo "Deploying to staging..."
aws s3 sync $PWD/build/ s3://$staging/ --acl public-read --delete

python -m webbrowser "https://s3.amazonaws.com/$staging/index.html"
echo "Deployed to staging. Please verify correctness by typing (Y/N), followed by [ENTER]: "
read staging_ok

if [ "$staging_ok" == "Y" ]; then
	echo "Continuing with deploy..."
	git checkout master
	git merge "$tag_name"
	echo "Enter production bucket name, followed by [ENTER]: "
	read production

	DATE=`date +%F_%s`
	echo "Backing up $production to $PWD/backup/$DATE..."
	aws s3 sync s3://$production/ $PWD/backup/$DATE/

	echo "Deploying to production..."
	aws s3 sync $PWD/build/ s3://$production/ --acl public-read --delete

	echo "Deployed to production, check it out:"
	python -m webbrowser "https://platform.pokitdok.com/documentation/v4/"

	git tag "DOCS-$tag_name"
	git push origin master --tags

	echo "Cleaning up..."
	git branch -d "$tag_name"
	git checkout dev
	echo "Deploy Process Complete."
fi