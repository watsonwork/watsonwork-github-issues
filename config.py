import os

# Server port
PORT = os.getenv('PORT', 8080)

# Watson Work Services API
WATSON_WORK_SERVICES = 'https://api.watsonwork.ibm.com'

# Applicaion ID
APP_ID = os.getenv('APP_ID')

# Application secret
APP_SECRET = os.getenv('APP_SECRET')

# Webhook secret
WEBHOOK_SECRET = os.getenv('WEBHOOK_SECRET')

# Webhook trigger word
WEBHOOK_TRIGGER = '@py-echo'

# Send message color
MESSAGE_COLOR = '#006600'

# Send message title
MESSAGE_TITLE = 'Echo test'
