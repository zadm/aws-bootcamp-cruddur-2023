import rollbar
import rollbar.contrib.flask
from flask import Flask
from flask import got_request_exception

import os
def init_rollbar(app: Flask):
    rollbar.init(
    access_token=os.getenv("ROLLBAR_ACCESS_TOKEN"),
    environment='cruddur flask',
    root=os.path.dirname(os.path.realpath(__file__)),
    code_version='1.0',
    allow_logging_basic_config=False
    )
    # send exceptions from `app` to rollbar, using flask's signal system.
    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)

# def init_rollbar(app: Flask):
#     app.before_first_request(init(app))
