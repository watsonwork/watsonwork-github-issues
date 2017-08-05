# Github Issues Sample
This `watsonwork-github-issues` sample application showcases a variety of capabilities and easy-to-use features with Watson Work Services. In particular it shows authentication with Watson Work Services, posting a message to a Work Services space and integration with a third party service.

This app will listen to newly created or closed Github issues for a particular repository and post the status back to Watson Work Services.

## Quickstart with IBM Bluemix
Let's get started! The steps below will outline the process from getting the app running within Bluemix to enabling the app to post within a space based on the status of a github issue, and everything in between.

Before jumping in, try accessing the links below to make sure you have access to Workspace, the developer experience for Watson Work Services, and Bluemix.
* [Watson Workspace](https://workspace.ibm.com)
* [Watson Work Services](https://developer.watsonwork.ibm.com)
* [Bluemix](https://bluemix.net)

### Deploy  to Bluemix
First, let's get this app up and running on Bluemix. This will provide us with a publicly accessible endpoint that we can register with Watson Work Services to get events pushed to. To deploy to Bluemix, you can simply click the button below. This will create your own [Bluemix DevOps toolchain](https://console.bluemix.net/devops/getting-started?env_id=ibm:yp:us-south) in addition to deploying the app. As part of the toolchain, Bluemix will create a git-based repository for source control and a pipeline for building, testing and deployment.

[![Deploy to Bluemix](https://bluemix.net/deploy/button.png)](https://bluemix.net/deploy?repository=https://github.com/watsonwork/watsonwork-github-issues)

Once you've clicked the button, you'll get prompted with the following screens:

1. Define your `App name`, `Region`, `Organization` and `Space`.

  Most of the time you can keep the default values, but if you have multiple accounts/organizations/spaces in Bluemix, please make note of the values here to make sure the app is deployed where you'd like it to be.

  ![Configure Pipeline](https://user-images.githubusercontent.com/10982483/28998008-7e43bc84-79ef-11e7-989e-4822dd25bfac.png)

  Click the **Deploy** button at the bottom of the screen to continue to the next step.

2. Once deployment and configuration has begun, you will be sent to the DevOps toolchain dashboard for your app:

  ![DevOps Dashboard](https://user-images.githubusercontent.com/10982483/28998071-80ecc056-79f0-11e7-8052-37363e88ff65.png)

  This will show you each of the "tools" that are provided in the tool chain.
  * The **Issues** block will take you to your own git-based repository for this app. It will bring you to the issues section of this repository.
  * The **Git** block will also take you to the git repository. This repository can be used like any git repository, included with the ability to automatically run the pipeline for any `git push`.
  * The **Eclipse Orion Web IDE** will take you to Eclipse's web-based editor, with the project connected to the git repository referenced above.
  * The **Delivery Pipeline** block will bring you to Bluemix's pipeline dashboard, which outlines each stage configured for the pipeline.

3. Click on the **Delivery Pipeline** block to see the current status of the deployment.

   When the deployment is done, the deploy stage will appear as below, with a green `Stage Passed` confirmation box.

   ![Delivery Pipeline](https://user-images.githubusercontent.com/10982483/28998124-c46f8358-79f1-11e7-8638-8cb7d6e18a8c.png)

   **Note:** It may take a minute or two to deploy.

4. After the app is done deploying, click on the box under **Last Execution Result** to navigate to the deployed app.

  ![AppBlock](https://user-images.githubusercontent.com/10982483/28998156-65bb5a84-79f2-11e7-95bd-8355b0e0b461.png)

5. At this stage, you should have an application that is up and running on Bluemix. The

Once the code is live, make note of the URL (e.g. http://watsonwork-github-issues.mybluemix.net) as you'll need this later.

### Register your app in Work Services
