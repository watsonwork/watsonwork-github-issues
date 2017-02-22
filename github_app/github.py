import hmac
import hashlib
import json

from flask import current_app, request, Response, Blueprint
from sendmessage import buildAndSend

# Define blueprint module
github = Blueprint('github', __name__, url_prefix='/github')

# Expose endpoint for Github webhooks
@github.route("/<spaceId>", methods=['POST'])
def githubWebhook(spaceId):
  current_app.logger.info('Processing webhook from github')

  body = request.json

  # If body is valid, build message and send to Watson Work Services
  if body != None:
    buildGithubMessage(spaceId, body)
  else:
    raise Exception('Could not process github webhook')

# Build message and send to Watson Work Services
def buildGithubMessage(spaceId, body):
  # Extract information from Github webhook request
  action = body["action"]
  repo = body['repository']
  issue = body["issue"]

  # Build title and message based on Github webhook information
  title = "%s - Issue %s" % (repo["full_name"], action)
  message = "[#%s - %s](%s)\n" % (issue['number'],
                                  issue['title'], issue["html_url"])

  if action == "opened":
    color = "#3d8b38"
    return buildAndSend(spaceId, message, title, color)
  elif action == "closed":
    color = "#cc0000"
    return buildAndSend(spaceId, message, title, color)
  else:
    current_app.logger.info("Unsupported request: %s" % str(body))
    return None
