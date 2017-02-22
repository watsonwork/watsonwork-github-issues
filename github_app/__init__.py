from flask import Flask, Blueprint, render_template

# Import local modules
from github_app.webhooks import webhooks
from github_app.sendmessage import sendmessage
from github_app.github import github

# Define Flask application
app = Flask(__name__)

# Pull in configuration from config file
app.config.from_object('config')

# Register blueprint(s)
app.register_blueprint(webhooks)
app.register_blueprint(sendmessage)
app.register_blueprint(github)
