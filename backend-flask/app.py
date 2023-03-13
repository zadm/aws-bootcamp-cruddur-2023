from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
import os


from services.home_activities import *
from services.user_activities import *
from services.create_activity import *
from services.create_reply import *
from services.search_activities import *
from services.message_groups import *
from services.messages import *
from services.create_message import *
from services.show_activity import *
from services.notifications_activities import *

from services.tracing.honycomb import init_honycomb
from services.tracing.aws_xray import init_xray

import logging
from services.logging.logger import setup_logger
setup_logger()

from services.middleware.flask_cognito import cognito_auth_required, CognitoAuth
from services.middleware.config import config_cognito

# configuration

# Rollbar
from services.logging.rollbar import init_rollbar


logger = logging.getLogger("cruddur")

frontend = os.getenv("FRONTEND_URL")
backend = os.getenv("BACKEND_URL")
app = Flask(__name__)

# Cognito
config_cognito(app)
# initialize extension
cogauth = CognitoAuth(app)



# instrument with  honeycomb
init_honycomb(app) 

# instrument with xray
init_xray(app)

# init rollbar
if os.getenv("ENABLE_ROLLBAR_LOG") and os.getenv("ENABLE_ROLLBAR_LOG").lower() == "true":
    init_rollbar(app)

origins = [frontend, backend]
allow_headers = ["content-type","if-modified-since","traceparent", "Authorization"]
cors = CORS(
    app,
    resources={r"/api/*": {"origins": origins}},
    expose_headers="Authorization",
    allow_headers=allow_headers,
    methods="OPTIONS,GET,HEAD,POST",
)

@app.route("/api/message_groups", methods=["GET"])
@cognito_auth_required
def data_message_groups():
    logger.info("message group request is received")
    user_handle = "andrewbrown"
    model = MessageGroups.run(user_handle=user_handle)
    if model["errors"] is not None:
        return model["errors"], 422
    else:
        return model["data"], 200


@app.route("/api/messages/@<string:handle>", methods=["GET"])
@cognito_auth_required
def data_messages(handle):
    user_sender_handle = "andrewbrown"
    user_receiver_handle = request.args.get("user_reciever_handle")

    model = Messages.run(
        user_sender_handle=user_sender_handle, user_receiver_handle=user_receiver_handle
    )
    if model["errors"] is not None:
        return model["errors"], 422
    else:
        return model["data"], 200
    return


@app.route("/api/messages", methods=["POST", "OPTIONS"])
@cross_origin()
@cognito_auth_required
def data_create_message():
    user_sender_handle = "andrewbrown"
    user_receiver_handle = request.json["user_receiver_handle"]
    message = request.json["message"]

    model = CreateMessage.run(
        message=message,
        user_sender_handle=user_sender_handle,
        user_receiver_handle=user_receiver_handle,
    )
    if model["errors"] is not None:
        return model["errors"], 422
    else:
        return model["data"], 200
    return

@app.route("/api/activities/home", methods=["GET"])
# @cognito_auth_required
def data_home():    
    logger.debug(request.headers)
    data = HomeActivities.run()
    return data, 200

@app.route("/api/activities/notifications", methods=["GET"])
# @cognito_auth_required
def data_notifications():
    logger.debug(request.headers)
    data = NotificationsActivities.run()
    return data, 200

@app.route("/api/activities/@<string:handle>", methods=["GET"])
@cognito_auth_required
def data_handle(handle):
    model = UserActivities.run(handle)
    if model["errors"] is not None:
        return model["errors"], 422
    else:
        return model["data"], 200

@app.route("/api/activities/search", methods=["GET"])
@cognito_auth_required
def data_search():
    term = request.args.get("term")
    model = SearchActivities.run(term)
    if model["errors"] is not None:
        return model["errors"], 422
    else:
        return model["data"], 200
    return

@app.route("/api/activities", methods=["POST", "OPTIONS"])
@cross_origin()
@cognito_auth_required
def data_activities():
    user_handle = "andrewbrown"
    message = request.json["message"]
    ttl = request.json["ttl"]
    model = CreateActivity.run(message, user_handle, ttl)
    if model["errors"] is not None:
        return model["errors"], 422
    else:
        return model["data"], 200
    return


@app.route("/api/activities/<string:activity_uuid>", methods=["GET"])
@cognito_auth_required
def data_show_activity(activity_uuid):
    data = ShowActivity.run(activity_uuid=activity_uuid)
    return data, 200


@app.route("/api/activities/<string:activity_uuid>/reply", methods=["POST", "OPTIONS"])
@cross_origin()
def data_activities_reply(activity_uuid):
    user_handle = "andrewbrown"
    message = request.json["message"]
    model = CreateReply.run(message, user_handle, activity_uuid)
    if model["errors"] is not None:
        return model["errors"], 422
    else:
        return model["data"], 200
    return


@app.route("/api/health", methods=["GET"])
def health():
    logger.info("health request received")
    data = {"success": True, "message": "healthy"}
    return data, 200

@app.route('/rollbar')
def hello():
    print("in hello")
    x = None
    x[5]
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)
