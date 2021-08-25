### [WIP] About `monorepo-template`

The `monorepo-template` is a _bare minimum_, _all batteries included_ template, that you can use to run or test applications locally in isolation, or within a Kubernetes cluster provisioned locally, which is generally useful for end-to-end testing.

Our goal is to have 1:1 parity with: local, CI/CD, and cloud environments.

The project includes reference implementations for: 
- React web app
- Python backend using Flask
- Infrastructure provisioned using Pulumi and Kind (locally)
- Machine learning workloads using Metaflow

We also include an end-to-end test suite that runs on top of the Kubernetes cluster.

## Features

- [ ] Test applications locally with hot-reload
- [ ] Run applications locally with hot-reload
- [ ] CI/CD support for GitHub
- [ ] CI/CD support for GitLab
- [ ] Support for GCP
- [ ] Support for AWS
- [ ] Support for Azure

## Stack

Infra
- [x] Python3.7
- [x] Docker
- [x] Kind
- [x] Kubernetes
- [x] Kubernetes Dashboard
- [x] Kubectl
- [x] Pulumi
- [ ] End-to-end tests

API
- [x] Python3.7
- [x] Flask
- [x] Graphene
- [x] SQLAlchemy
- [x] PostgreSQL
- [x] Pytest + Mocha
- [ ] Alembic

Frontend
- [x] Node v14
- [x] Apollo + GraphQL
- [x] React
- [x] NPM
- [x] Styled-components
- [x] Jest (with CSS testing)

Observability
- [ ] Grafana

MLOps
- [ ] Metaflow

# Getting started

Before we get started, make sure you have Docker installed in your local computer. If you don't already have Docker installed, visit https://docs.docker.com/get-docker.

## Testing locally

To test `api`, `frontend` or `infra` applications locally type in your command line:

```
./test.sh {APP_NAME}

```

Where `{APP_NAME}` is one of these values: `api`, `frontend` or `infra`.

Note: when you run `./test.sh infra`, a Kubernetes cluster will be provisioned inside a Docker container using [Kind](https://kind.sigs.k8s.io/), all applications (`api`, `frontend`, etc.) will be _containerized_ and _provisioned_ on Kubernetes. Once the cluster is _ready_, the end-to-end test suite will run.

## Running locally

To run `api`, `frontend` or `infra` applications locally type in your command line:

```
./run.sh {APP_NAME}

```

Where `{APP_NAME}` is one of these values: `api`, `frontend` or `infra`.

Note: when you run `./run.sh infra`, a Kubernetes cluster will be provisioned inside a Docker container using [Kind](https://kind.sigs.k8s.io/), all applications (`api`, `frontend`, etc.) will be _containerized_ and _provisioned_ on Kubernetes, and accessible through your browser.
