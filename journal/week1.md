# Week 1 — App Containerization

## Build the application

### Write the backend docker file

[Link to the backend docker file](../backend-flask/Dockerfile)

The application is running behind a gunicorn server [config file](../backend-flask/config/gunicorn.conf.py)

### Write the frontend docker file

[Link to the backend docker file](../frontend-react-js/Dockerfile)

### Write the docker compose file
[docker-compose](../docker-compose-dev.yml)
### Run the application in gitpod

1. Launch the application in gitpod
2. Execute the docker-compose
   
```bash
docker-compose -f docker-compose-dev.yml  up --build
````
3. Make the ports public
4. Open the cruddur URL in your browser
![Cruddur in gitpod](../_docs/assets/week1/Cruddur-gitpod.png)


