import hmac
import hashlib
import json

from flask import current_app, request, Response, Blueprint
from sendmessage import sendSimpleMessage

# Define blueprint module
webhooks = Blueprint('webhooks', __name__, url_prefix='/webhooks')

# Expose endpoint for Watson Work Services webhooks
@webhooks.route("/", methods=['POST'])
def webhook():
  if not request:
    raise Exception('Invalid Request')

  body = request.json

  # Call verification function if request type is verification, else process message
  if str(body['type']) == 'verification':
    return verification(body)
  elif str(body['type']) == 'message-created':
    return parseMessage(body)

# Return verification response for webhooks with Watson Work Services
def verification(body):
  current_app.logger.info('Processing webhook verification')
  responseBody = {'response': str(body['challenge'])}
  response = Response(response=json.dumps(responseBody),
                      content_type='application/json', status=200)
  response.headers['X-Outbound-Token'] = hmac.new(current_app.config.get(
      'WEBHOOK_SECRET'), msg=str(json.dumps(responseBody)), digestmod=hashlib.sha256).hexdigest()
  return response

# Process message and send respond back to Watson Work Services for test 
def parseMessage(body):
  current_app.logger.info('Parsing incoming message')
  spaceId = body['spaceId']
  splitContent = body['content'].split(' ')
  if current_app.config.get('WEBHOOK_TRIGGER') in splitContent:
    sendSimpleMessage(spaceId, ' '.join(splitContent[1:]))
  return Response(status=200)
