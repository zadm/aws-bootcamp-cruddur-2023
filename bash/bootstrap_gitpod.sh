#!/bin/bash
function configure_aws_with_gitpod (){
    # update AWS CLI
    OLD_DIR="$PWD"
    TMP_DIR="$(mktemp -d)"
    echo "Updating AWS"
    cd "${TMP_DIR}" || exit 1

    curl -fSsl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    unzip -qq awscliv2.zip
    sudo ./aws/install --update
    rm awscliv2.zip

    cd "${OLD_DIR}" || exit 1
    rm -rf "${TMP_DIR}"
}
function install_postgre(){
    curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc|sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
    echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" |sudo tee  /etc/apt/sources.list.d/pgdg.list
    sudo apt update
    sudo apt install -y postgresql-client-13 libpq-devw
}

function export_variables() {
    export FRONTEND_URL="*"
    export BACKEND_URL="*"
    export REACT_APP_BACKEND_URL="https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
    export REACT_APP_ENVOY_URL="https://8080-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
    export OTEL_EXPORTER_OTLP_ENDPOINT="https://api.honeycomb.io"
    export OTEL_EXPORTER_OTLP_HEADERS="x-honeycomb-team=${HONEYCOMB_API_KEY}"
    export OTEL_SERVICE_NAME="cruddur-backend"
    export HONEYCOMB_API_KEY=${HONEYCOMB_API_KEY}
    export AWS_XRAY_URL="*4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}*"
    export AWS_REGION="eu-west-1"
    export AWS_DEFAULT_REGION="eu-west-1"
    export REACT_APP_OTEL_COLLECTOR_ENDPOINT="https://4318-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"




    }

function run() {
   docker-compose   -f docker-compose-dev.yml up
}