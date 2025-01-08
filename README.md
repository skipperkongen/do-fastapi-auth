# do-fastapi-auth

The most basic application based on FastAPI for Digital Ocean App platform.

Click [here](https://cloud.digitalocean.com/apps/github/install) to grant Digital Ocean access to the github repo.

[![Deploy to DigitalOcean](https://www.deploytodo.com/do-btn-blue.svg)](https://cloud.digitalocean.com/apps/new?repo=https://github.com/skipperkongen/do-fastapi-auth/tree/main)


## Run locally

```shell
fastapi dev main.py
```

## Deploy with CLI

Create app (first time only)

```shell
# brew install doctl
doctl apps create --spec .do/app.yaml
```

Update app (only works for app.yaml changes, not code changes?)

```shell
# get app id
doctl apps list
# update
doctl apps update e1109806-2801-4e97-a261-aeefdd5aedb1 --spec .do/app.yaml
```

After code changes

```shell
# on main branch (TODO: setup pull request restriction to main)
git commit -am 'updated code'; git push
```

## How the code was generated


### Backend

Authentication in backend implement by following the [security tutorial](https://fastapi.tiangolo.com/tutorial/security/) on the FastAPI homepage.

### Frontend

```shell
cd frontend
npm create vue@latest .
```