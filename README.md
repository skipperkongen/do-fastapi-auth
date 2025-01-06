# do-fastapi-auth
An application based on FastAPI with Authentication for Digital Ocean App platform

Click [here](https://cloud.digitalocean.com/apps/github/install) to grant Digital Ocean access to the github repo.

[![Deploy to DigitalOcean](https://www.deploytodo.com/do-btn-blue.svg)](https://cloud.digitalocean.com/apps/new?repo=https://github.com/skipperkongen/do-fastapi-auth/tree/main)

## Run locally

```shell
fastapi dev main.py
```

## Deploy

Using CLI:

```shell
doctl apps create --spec .do/app.yaml
```
