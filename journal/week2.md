# Week 2 — Distributed Tracing

# Instrument our backend flask application to use Open Telemetry (OTEL) with Honeycomb.io as the provider

## Add opentelemetry to instrument flask app 
### Instrument flask application
[honeycomb module](../backend-flask/services/tracing/honycomb.py)

### Add span to home activities

![home activities honeycorn](../_docs/assets/week2/home-activities-honeycorn.png)   


### Add span to notification activieties

![home activities honeycorn](../_docs/assets/week2/notification-activities-heneycomb.png)

# Run queries to explore traces within Honeycomb.io

## Notification activities tarce
![](../_docs/assets/week2/honneycomb-app-notification-activities-trace.png)

## Show routes in honeycomb
![](../_docs/assets/week2/honeycomb-routes.png)

## Query where result exist
![](../_docs/assets/week2/honeycomb-query-app-result-exist.png)

## Query p99
![](../_docs/assets/week2/honeycomb-p99.png)

## Query where app.received.date exists

![](../_docs/assets/week2/honeycomb-where-attribute-exist.png)

## Honeycomb trace from gitpod
![](../_docs/assets/week2/honeycomb-gitpod.png)


# Instrument AWS X-Ray into backend flask application

## Setup AWS X-Ray Resources
All the aws resources have been created using terraform

[xray terraform stack](../terraform/backend-app/stacks/xray/)

[xray terraform config](../terraform/backend-app/config/xray/)


1. Create xray group
![](../_docs/assets/week2/terragrunt-create-group.png)

![](../_docs/assets/week2/aws-xray-group-proof.png)

2. Create a simple rule
![](../_docs/assets/week2/terragrunt-create-simple-rule.png)

![](../_docs/assets/week2/aws-simple-rule-proof.png)


## Add a new python module to handle xray
[xray python module](../backend-flask/services/tracing/aws_xray.py)

This module contains the code to instrument a falsk application. 

## Configure and provision X-Ray daemon within docker-compose and send data back to X-Ray API
[xray docker-compose](../docker-compose.yml#L73-82)

Console output of xray daemon
![](../_docs/assets/week2/xray-daemon-in-docker.png)

## Observe X-Ray traces within the AWS Console

### tarce list and graph
![](../_docs/assets/week2/xray-aws-cpnsole-trace-list-graph.png)

### all request with http.code == 200
![](../_docs/assets/week2/xray-qyery-http-code-200.png)

### home activities subsegment

I added a subsegment for the HomeActivities class 

[xray subsegment](../backend-flask/services/home_activities.py)

I managed to instrument this method with both xray and honneycomb, like that the traces are send to both of them
![](../_docs/assets/week2/aws-xray-subsegment-image.png)

![](../_docs/assets/week2/aws-xray-subsegment-raw.png)
