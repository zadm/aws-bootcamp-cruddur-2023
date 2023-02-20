# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10
RUN python --version

# Install required package 
RUN git version
EXPOSE 8080

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt 

WORKDIR /app
COPY . /app

# RUN pip install .
COPY config/gunicorn.conf.py  /etc/gunicorn.conf.py

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["./entrypoint.sh", "FLASK"]
