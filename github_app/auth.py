import json
import requests
import base64

from flask import current_app, request, Response, Blueprint

# Define blueprint module
auth = Blueprint('auth', __name__)

# Authenticate with the application id and application secret
def authenticateApp():
  # Build API for requesting access token of application
  auth_api = '%s/oauth/token' % current_app.config.get('WATSON_WORK_SERVICES')

  # Pull in app id and app secret
  credentials = '%s:%s' % (current_app.config.get(
      "APP_ID"), current_app.config.get("APP_SECRET"))

  # Construct "client_credentials" request for token
  payload = {"grant_type": "client_credentials"}
  headers = {"Authorization": "Basic %s" % base64.b64encode(credentials)}

  # POST to /oauth/token to obtain access token
  authResponse = requests.post(auth_api, data=payload, headers=headers)

  current_app.logger.info(authResponse.json())

  return authResponse.json()['access_token']
