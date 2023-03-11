
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

    token = "eyJraWQiOiI1dGM3T3VJTElvdGN5ZWwrSVBOeGdwVVBSY3RkMmkya0VPbnFBT1l0Kzk4PSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJiNDg4NGNhZS01MTVmLTQ0YjYtOWQzMi02ZTMwNjJlNTgzOTAiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuZXUtd2VzdC0xLmFtYXpvbmF3cy5jb21cL2V1LXdlc3QtMV9wSUw5YlRQeHYiLCJjbGllbnRfaWQiOiI2azNiMTAxZWprbXZrMWFsMHRxanFhdjF2cCIsIm9yaWdpbl9qdGkiOiJhZGE5NTU4OS0yZTFlLTQ5ZDQtODBlZS02Y2Q5NTIxNmY3MmUiLCJldmVudF9pZCI6ImVjZTg1YzAwLWU5NjgtNDRhYi04Nzg5LWZjYzczNzNmOWZhZiIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2Nzg1Mzc3NTUsImV4cCI6MTY3ODU0MTM1NSwiaWF0IjoxNjc4NTM3NzU1LCJqdGkiOiIzNDg1MWNlYS0xZDNlLTRhZDktOGFhYy01NDE0MmE2YjI4ZGIiLCJ1c2VybmFtZSI6ImI0ODg0Y2FlLTUxNWYtNDRiNi05ZDMyLTZlMzA2MmU1ODM5MCJ9.cRqA-1DeCLry0NC7tUNFxvLIdPURx44mGVJ7GwplIG9Eus3uF72486JAI8X6vj1c5nV8AZGurFGczt3sZ80hrORgO-mjMPCoBYWD0KGe9gEiO3m6CJoUqeCMMM4kj9XXqKUqysRRnrqDJZ6oBcnW3I9f6zs2S8Q-KjsmG-SXXvJ6HP2B4UZvZ_6cF-3aVnBWujbBM9xLGsjgrPX7wy7wIrfXnw2_SJxIzzd0XjoEpxp13LoIq4A67PFEji8zRRQen_EiwyRIdohbxTy9ehO4o8do-zR-XIYwxmBN7ebKU3Uu9Xy0mzrkQZnVf7tiF2bM2yQW_YGUhy_eiwOOucuybQ"

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