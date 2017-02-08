PokitDok API Documentation
==========================

*This documentation was created with Slate. Check it out at [tripit.github.io/slate](http://tripit.github.io/slate).*

This repository contains developer docs for the [PokitDok APIs](https://platform.pokitdok.com)

### Found a bug? Want to help update these docs? Excellent!

### Steps: ###
Easy Method (docker-compose)
 1. Fork this repository on Github.
 2. Clone *your forked repository* (not our original one) to your machine with `git clone https://github.com/YOURUSERNAME/apidocs-v4.git`
 3. `cd apidocs-v4`
 4. `docker-compose up`
 5. You can see the docs at <http://localhost:8080>

Old Method (docker-machine)
 1. Fork this repository on Github.
 2. Clone *your forked repository* (not our original one) to your machine with `git clone https://github.com/YOURUSERNAME/apidocs-v4.git`
 3. `cd apidocs-v4`
 4. If you do not have a docker host setup already:
     1. Use setup script to create docker-machine: `sh setup-osx.sh`
     2. Look at your docker-machine IP: `docker-machine ip apidocs`

        If you are on Mac:
        1. Run `docker-machine env apidocs` to verify the environment variables created by `sh setup-osx.sh`.
        2. Run the commented out command from sdout to finish configuring your shell (should look something like `eval $(docker-machine env apidocs)`)
 5. Start local server: `docker run -it -p 8080:4567 -v $PWD:/app ruby:2.3 /app/serve.sh`

If you are using docker-machine:
- Using the IP address of your local docker-machine and port 8080, you can now see the docs at `http://(docker-machine ip):8080`.

Otherwise, you can see the docs at <http://localhost:4567>

Whoa! That was fast!

[Handy reference guide for editing slate markdown.](https://github.com/tripit/slate/wiki/Markdown-Syntax)

When you're done editing, send us a pull request.
