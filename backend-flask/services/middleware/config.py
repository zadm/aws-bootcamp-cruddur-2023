
import cognitojwt 
from flask import Flask

def config_cognito(app: Flask):

    config = {
            'COGNITO_REGION': 'eu-west-1',
            'COGNITO_USERPOOL_ID': 'eu-west-1_pIL9bTPxv',

            # optional
            'COGNITO_APP_CLIENT_ID': '6k3b101ejkmvk1al0tqjqav1vp',  # client ID you wish to verify user is authenticated against   
            'COGNITO_CHECK_TOKEN_EXPIRATION': False,  # disable token expiration checking for testing purposes
            'COGNITO_JWT_HEADER_NAME': 'Authorization',
            'COGNITO_JWT_HEADER_PREFIX': 'Bearer',
        }
    for k, v in config.items():
        app.config[k] = v

if __name__ == "__main__":

    token = ""

    REGION = 'eu-west-1'
    USERPOOL_ID = 'eu-west-1_pIL9bTPxv'
    APP_CLIENT_ID = '6k3b101ejkmvk1al0tqjqav1vp'

    # Sync mode
    verified_claims: dict = cognitojwt.decode(
        token,
        REGION,
        USERPOOL_ID,
        app_client_id=APP_CLIENT_ID,  # Optional
        testmode=True  # Disable token expiration check for testing purposes
    )