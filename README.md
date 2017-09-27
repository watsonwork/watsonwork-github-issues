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

5. The **Last Execution Result** block will take you to the App dashboard for the newly deployed app.

  ![App Dashboard](https://user-images.githubusercontent.com/10982483/28998301-66f645aa-79f5-11e7-82ae-d717f28f7b0d.png)

  This dashboard shows the status of the app, the URL to access the app and provides the ability to interact with the app ( set environment variables, view logs, etc).

  **Take note of the app name at the top.** The app name is used to contruct the URL for the running app: `https://<appname>.mybluemix.net`.

  For example, in the screenshot above, the URL would be: `https://watsonwork-github-issues-20170805194040469.mybluemix.net`

  Now let's register this app in Watson Work Services!

### Register app with Watson Work Services
An app must be registered with Watson Work Services in order to interact with the platform. The registration process provides the app with an id, secret and enables the app to request certain capabilities, such as listening to events in the system.

To register an app, navigate to the Watson Work Services developer experience: https://developer.watsonwork.ibm.com.

1. Once logged in, select the **Your Apps** link at the top right.

  ![WWS](https://user-images.githubusercontent.com/10982483/28998391-c69fd91a-79f7-11e7-9a17-b604b977b622.png)

2. From here, you should see a button to **Create new app**, as well as a list of apps if you have already created some.

  ![AppsList](https://user-images.githubusercontent.com/10982483/28998395-19411d8c-79f8-11e7-8210-e02127d0c2bf.png)

3. Click on **Create new app**.

  ![CreateNewApp](https://user-images.githubusercontent.com/10982483/28998413-69216064-79f8-11e7-9cef-50a6c2ae888c.png)

  Provide any `App name` and `Description` that you'd like for your app and then click **Create**. This name will show up in Watson Work Services as the display name for your app.  

4. Once registered, you will be presented with the `id` and `secret` for the app.

  **Copy both the id and secret for later use.**

  ![SuccessDialog](https://user-images.githubusercontent.com/10982483/28998467-7ef435be-79f9-11e7-8acc-cb6483e14ec7.png)

5. After copying the id and secret, you will be sent to the App Dashboard for the newly registered Watson Work Services app.

  ![AppDashboard](https://user-images.githubusercontent.com/10982483/28998480-455d3b9c-79fa-11e7-8625-4c52ff53236e.png)

  This dashboard contains all of the information for your app, as well configuration options for listening to events, enabling your app to run as a user, and much more!

### Listen to events in Watson Work Services
Now that your app is registered with Watson Work Services, we can enable it with a variety of different capabilities.

For now we're going to focus on **Listen to Events** to set our app up to retrieve messages from Watson Work Services.

1. Click on the **Listen to Events** tab on the side menu in your Apps Dashboard.

  ![ListenToEvents](https://user-images.githubusercontent.com/10982483/28998495-923006b6-79fa-11e7-87d9-e60288a993ee.png)

2. Click on **Add an outbound webhook**.

  ![AddWebhook](https://user-images.githubusercontent.com/10982483/28998544-959527ae-79fb-11e7-8334-5c3007200c55.png)

  * Provide any `Webhook Name` that you would like. This name won't be displayed anywhere.
  * For the `Webhook URL`, provide the following URL, based on the **app name** that was copied above from Bluemix.
    * **Webhook URL:** `<appname>.mybluemix.net/webhooks/`.
      * Example: `watsonwork-github-issues-20170805194040469.mybluemix.net/webhooks/`.

      Note the `/` at the end is required for this particular sample app. Also, the form includes the `https://`, so no need to include that in the input box.  

  * For the **Events** section, check the `message-created` option.

3. Once you click **Save**, a confirmation dialog will appear with your `Webhook Secret`. **Copy this secret.** We will need it for configuring our Bluemix app.

  ![WebhookConfirmation](https://user-images.githubusercontent.com/10982483/28998792-e8f88fac-7a01-11e7-94cf-3f66b1106c71.png)

  **Note:** Even though we have saved the webhook, the webhook is not enabled until we update our app to use the webhook secret. We will come back to the **Listen to Events** panel to enable it after updating these values in Bluemix.

4. Navigate back to you Bluemix app dashboard to input the ids and secrets. In your Bluemix app dashboard, navigate to **Runtime** on the side menu, and then the **Environment variables** tab.

  ![BluemixAppVar](https://user-images.githubusercontent.com/10982483/28998758-bf6da27c-7a00-11e7-93c2-2c4cc1cbf084.png)

5. Add the following environment variables:
  * Name: `APP_ID`, Value: `Id copied from app registration success dialog`
  * Name: `APP_SECRET`, Value: `Secret copied from app registration success dialog`
  * Name: `WEBHOOK_SECRET`, Value: `Secret copied from webhook registration`

  ![EnvVariables](https://user-images.githubusercontent.com/10982483/28998768-1c9d00aa-7a01-11e7-9106-4317c6387ed2.png)

  Click **Save** and the app will automatically restart.

6. Once the app has restarted. Navigate back to the **Listen to Events** page for your app in the Watson Work Services developer experience. Select the **Enable** button on your webhook.

  ![EnableWebhook](https://user-images.githubusercontent.com/10982483/28998805-1ed3cff6-7a02-11e7-8bae-d85b13113718.png)

  The button should then turn to **Disable** if enablement of the webhook was a success.

  ![EnabledWebhook](https://user-images.githubusercontent.com/10982483/28998812-3cfda600-7a02-11e7-80eb-4d0cbfeff71f.png)

  Now your app is connected to Watson Work Services, and can both post messages and listen to `message-created` events! Let's try it out.

### Try out your app in Workspace

After the app is registered and configured to listen to events, we can try it out by adding it to a space in Workspace.

1. Open [Watson Workspace](https://workspace.ibm.com) in a new tab.

  ![Workspace](https://user-images.githubusercontent.com/10982483/28998883-07076598-7a04-11e7-8c6a-e556dc062082.png)

2. Create a new space to add the app to. You can click on the `Create a Space` button or the `+` icon next to the **Spaces** title.

  ![WorkspaceNewSpace](https://user-images.githubusercontent.com/10982483/28998892-46004756-7a04-11e7-8fb5-6c68ab4e2b8f.png)

3. Click on the space name at the top to go to the Space Settings panel. From here you can click on the **Apps** link on the left to view apps to add.

  ![AppsPanel](https://user-images.githubusercontent.com/10982483/28998911-8dfba64a-7a04-11e7-8655-ae97ae8f93d7.png)

4. Click on the app to add it to the space.

  ![AddApp](https://user-images.githubusercontent.com/10982483/28998915-a5cdaf2a-7a04-11e7-9fdb-947dee7c75b3.png)

5. Now we can try to interact with the app. First let's send a message to see if the app can echo it back. The app is configured to listen for `@py-echo <message>`.

   Attempt to send in `@py-echo This is a test`. The app should respond.

   ![AppResponse](https://user-images.githubusercontent.com/10982483/28998975-f6d7e614-7a05-11e7-9509-d8c7d00b9c71.png)

   The app is able to listen for a message containing `@py-echo` and post a message back into the space!

   Let's set this up with Github now! Make note of your `spaceId`, which you can find in the URL of the space: `https://workspace.ibm.com/space/598639bfe4b07d4cbf448742`, with the id being `598639bfe4b07d4cbf448742`.

### Setup Github Webhook
Our app is now registered in Watson Work Services and running in Bluemix. The next step is to set up our app with a Github repository so that we can see the actual app functionality in motion!

1. Navigate to any Github repository where you have access to configure webhooks.
2. In your Github repo, head to the Settings page

  ![GithubSettings](https://user-images.githubusercontent.com/10982483/28998983-653e4210-7a06-11e7-85b3-2c69cbec7635.png)

3. Select the **Hooks & services** from the side menu.

  ![WebhookSettings](https://user-images.githubusercontent.com/10982483/28998994-ac48d6ac-7a06-11e7-83cf-39e8cf6742aa.png)

4. Select **Add Webhook**.

  ![ConfigureWebhook](https://user-images.githubusercontent.com/10982483/28999010-27008d9a-7a07-11e7-8887-9b941602d104.png)

  For the `Payload URL`, put in your Bluemix URL that we've used above (`https://<appname>.mybluemix.net`), with the context root of `/github/{spaceId}`.

  For example: `https://watsonwork-github-issues-20170805194040469.mybluemix.net/github/598639bfe4b07d4cbf448742`

  Select `application/json` for the `Content-Type`.

5. The app is only configured to listen to events related to `issues`, so we can select the **Let me select individual events** option, and pick `issues`.

  ![EventSettings](https://user-images.githubusercontent.com/10982483/28999029-83e466d0-7a07-11e7-82c6-7fb18738f7e1.png)

6. Save the webhook and create a new issue to see the event posted back to your Workspace space!

  ![NewIssue](https://user-images.githubusercontent.com/10982483/28999036-be9e83c8-7a07-11e7-9d8a-2456f5763dbd.png)

  And a post back in Workspace!

  ![GitIssuePost](https://user-images.githubusercontent.com/10982483/28999047-f91a93f2-7a07-11e7-992f-43c24de37909.png)

  If you close the issue, that will be reflected as well.

  ![GitIssuePost2](https://user-images.githubusercontent.com/10982483/28999055-1ec75ac2-7a08-11e7-9c7f-d9665cb57cd0.png)

Now we have an app that integrates with Github and posts useful updates to our spaces! 
