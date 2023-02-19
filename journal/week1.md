# Week 1 — App Containerization

# Required Homework

## Containerize Application (Dockerfiles, Docker Compose)

[Link to the backend docker file](../backend-flask/Dockerfile)

The application is running behind a gunicorn server [config file](../backend-flask/config/gunicorn.conf.py)

### Write the frontend docker file

[Link to the backend docker file](../frontend-react-js/Dockerfile)

### Write the docker compose file
[docker-compose](../docker-compose.yml)
### Run the application in gitpod

1. Launch the application in gitpod
2. Execute the docker-compose
   
```bash
docker-compose -f docker-compose.yml  up --build
```
3. Make the ports public
4. Open the cruddur URL in your browser
![Cruddur in gitpod](../_docs/assets/week1/Cruddur-gitpod.png)

## Document the Notification Endpoint for the OpenAI Document

[Notification OpenAPI](../backend-flask/openapi-3.0.yml#L151-165)


## Write a Flask Backend Endpoint for Notifications

![Notification flask endpoint](../_docs/assets/week1/notification-flask-endpoint.png)


## Write a React Page for Notifications
Notification feature added to the application 

![Notification react js endpoint](../_docs/assets/week1/Cruddur-create-notification.png)

#  Homework Challenges   

## Learn how to install Docker on your localmachine and get the same containers running outside of Gitpod / Codespaces

1. Docker locally 

![Local docker](../_docs/assets/week1/docker-local.png)

2. Cruddur locally

![Local docker](../_docs/assets/week1/cruddur-local.png)