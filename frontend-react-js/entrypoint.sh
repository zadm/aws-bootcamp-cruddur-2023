#!/bin/bash
set -e

SERVICES="FLASK NODE"
usage() {
    echo "Run the script with:"
    echo "$(basename "$0") <SERVICE> "
    echo
    echo -e "With SERVICE one of : \n${SERVICES}"
}

SERVICE=$1

if [ "$SERVICE" == "FLASK" ]; then
    gunicorn app:app -c /etc/gunicorn.conf.py
elif [ "$SERVICE" == "NODE" ]; then
    npm install
    npm start
else
    usage
fi