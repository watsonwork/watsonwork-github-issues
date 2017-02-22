import json
import requests

from flask import current_app, request, Response, Blueprint

from auth import authenticateApp

# Define blueprint module
sendmessage = Blueprint('sendmessage', __name__, url_prefix='/sendmessage')

# Expose endpoint for testing the mechanism to send a message to Watson Work Services
@sendmessage.route("/", methods=['POST'])
def sendEndpoint():
  current_app.logger.info("Sending message via POST")
  internalSendMessage(request.json['spaceId'], request.json['message'])
  return Response(status=200)

# Construct a message leveraging the Generic Annotation template andd call send method
def buildAndSend(spaceId, text, title, color):
  message = {
      "type": "appMessage",
      "version": 1.0,
      "annotations": [
          {
              "type": "generic",
              "text": text,
              "color": color,
              "title": title,
              "version": "1.0"
          }
      ]
  }

  return sendMessage(spaceId, message)

# Leverage the default title and color values to send a simple message to Watson Work Services
def sendSimpleMessage(spaceId, text):
  title = current_app.config.get('MESSAGE_TITLE')
  color = current_app.config.get('MESSAGE_COLOR')
  buildAndSend(spaceId, text, title, color)

# Call Send Message API to send message to Watson Work Services
def sendMessage(spaceId, message):
  send_message_api = '%s/v1/spaces/%s/messages' % (
      current_app.config.get('WATSON_WORK_SERVICES'), spaceId)

  payload = json.dumps(message)
  accessToken = authenticateApp()
  headers = {'Authorization': 'Bearer %s' % accessToken}

  r = requests.post(send_message_api, json=message, headers=headers)

  current_app.logger.info(r.json())
