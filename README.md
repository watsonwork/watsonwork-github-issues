# Github Issues Sample

A sample application that exposes authentication with Watson Work Services, posting a message to a space and integrating with a third party service.

This app will listen to newly created or closed Github issues for a particular repository and post the status back to Watson Work Services.

## Deploy the app
Assuming you just want to take this code and get it running before hacking it, the first step is to get it deployed to a live on a server so that Watson Work Services validates it's up and working before pushing messages to the app. To facilitate things, you can click the button below and it'll get it going to Bluemix very easily.

[![Deploy to Bluemix](https://bluemix.net/deploy/button.png)](https://bluemix.net/deploy?repository=https://github.com/watsonwork/watsonwork-github-issues)

Once the code is live, make note of the URL (e.g. http://watsonwork-github-issues.mybluemix.net) as you'll need this later.
