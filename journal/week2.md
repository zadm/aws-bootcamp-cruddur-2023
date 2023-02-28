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