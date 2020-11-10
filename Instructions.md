# CI/CD

## *"Microservices"*

There are 2 microservices:

* Service1 - creates hashes of strings
* Service2 - downloads a web page and calls service1 to create a md5 hash of it

Your task is to check (and fix) the microservice implementation / docker images:

* which improvements do you suggest
* which errors did you detect
* other comments

## Deployment (kubernetes)

1. Create two CI/CD strategies for the microservices:
    1. The microservices should be deployed independently from each-other for 2 projects
        * When a microservice is changed, it should be deployed to all projects
    2. The microservices should be deployed *dependently*
        * There should be a way to collect all the microservices and deploy them manually (e.g. a separate repository where only the correct versions are written, and they get deployed together)
2. Implement the CI/CD strategies in the chosen CI/CD tool
    * Take special care about the configuration - configuring the services for a new environment should be as painless as possible - a developer should easily be able (with instructions) to deploy his microservice(s)/project/...

## Expected outcome

1. Optimized, maintainable docker images
2. Automated, maintainable pipelines for build/deployment on multiple environments/projects (for both CI/CD strategies)
3. Automated versioning of service/solution artifacts
4. Deployed services on multiple environments/projects (for both CI/CD strategies) - with rollback possibilities
    * staging/prod project1
    * staging/prod project2
5. Addition of a new environment/project should be as simple (as fast) as possible

## Help

* Docker images can be stored on dockerhub or as tar.gz archives or any other way that you see fit
* The emphasis is not that the services work correctly, or make sense :), but on:
  * Service communication
  * Configurability
  * Maintainability
  * Time to deploy
  * Docker image optimization
  * Pipeline stability
  * Security (Service authentication/authorization is **not** important - but you can document a proposal for implementation)
* Each service should be a kubernetes deployment, and can include services/ingress/other kubernetes components

### Basic pipeline

* Build
* Unit Test+
* Integration Test+
* Publish Artifact
* Deploy to Staging
* Smoke Test
* End to End Test+
* Deploy to Production

+No need for writing unit/integration/e-2-e tests, just include a step that will execute them

### Tools

* Docker
* Kubernetes (local - docker, minikube, ...)
* Kubectl/kustomize
* Helm 3
* Git
* CI/CD tool (GitLab/Azure DevOps/CircleCI/Jenkins/...)
* Python
