Integrating your email account
========
**Getting Started**

Connecting your email account to Public Address is simple and allows you to send pitches from your email account
on the platform.

You can skip ahead to the relevant section depending on the email provider you use:

* Gmail_
* `Microsoft Exchange 365`_
* SMTP_


**Watch Outs/Common Issues**

* `Why can’t I add my Microsoft 365 account to Public Address?`_
* `Why am I seeing a ‘This app isn’t verified’ message from Google?`_
* `How do I use the full features of Public Address with my G Suite account?`_

.. _gmail:

Connecting your Gmail Account
-------

To connect your email account, head to the settings drop down menu and select **‘Integrations’**. Select the **+** sign on the right hand side of *email address* and click **'Add my own email'** from the drop down menu.

.. image:: https://publicaddressdocs.s3.ap-southeast-2.amazonaws.com/Add+New+Integration+email.png

A pop will then appear asking you a few different email options. Select **'Connect with Google'.**

.. image:: https://publicaddressdocs.s3.ap-southeast-2.amazonaws.com/Connect+with+Google.png

A pop up will open where it will ask you to select the account you want to connect, or enter an email address if you haven’t logged in on your browser previously.

Enter your email address and select ‘Next.’ You’ll now be prompted to enter your password, and then hit ‘next’.

You’ll now be asked to **provide your permission** for Public Address to be able to read and send email on your behalf – this is an important aspect of this integration as it allows you to send emails via the Public Address platform. These emails will then show up in your outbox and we’ll be able to incorporate replies to these emails into the platform.

.. image:: https://publicaddressdocs.s3.ap-southeast-2.amazonaws.com/Send+email+on+your+behalf.png

Please hit **Continue**, and then you’ll be redirected back to the user settings page and this dialog box will close.

If your platform has been configured correctly you’re all set to go. If you see a ‘This app isn’t verified’ warning from Google your platform or domain administrator haven’t configured the application correctly. To learn more about this error view our help article here.

.. _Microsoft Exchange 365:

Connecting your Microsoft Account
-------
To connect your email account, head to the settings drop down menu and select **‘Integrations’**. Select the **+** sign on the right hand side of *email address* and click **'Add my own email'** from the drop down menu.

.. image:: https://publicaddressdocs.s3.ap-southeast-2.amazonaws.com/Add+New+Integration+email.png

Select **‘Connect a Different Account’** and then **'Connect with Microsoft'** to connect your Office365 account.

.. image:: https://publicaddressdocs.s3.ap-southeast-2.amazonaws.com/Connect+with+Microsoft%3ASMTP.png

A pop up will open where it will ask you to select the account you want to connect, or enter an email address if you haven’t logged in on your browser previously.

Enter your email address and select ‘Next.’ You’ll now be prompted to enter your password, and then hit ‘next’.

You’ll now asked to **provide your permission** for Public Address to be able to read and send email on your behalf – this is an important aspect of this integration as it allows you to send emails via the Public Address platform. These emails will then show up in your outbox and we’ll be able to incorporate replies to these emails into the platform.

.. image:: https://publicaddressdocs.s3.ap-southeast-2.amazonaws.com/Microsoft+email+behalf.png

Please hit **Yes**, and then you’ll be redirected back to the user settings page and this dialog box will close.

Congratulations! You’re all set to use Public Address with your office365 email account.

.. _SMTP:

Connecting your SMTP Account
-------
First of all, you’ll require your SMTP/IMAP settings – every email server supports these and you can find them in a couple of ways. The easiest is to head to your account settings in Outlook or your email account where they’ll be displayed.

These are also accessible on your phone – so you can head to the settings of your emails on your phone and find these there as well.

If you know your email provider, you can also search for this on the internet and they will typically have these settings displayed somewhere on their website.

Of course, the recommended way ahead here is to ask your friendly IT support person to send these settings to you. You’ll need an IMAP Host and port, SMTP Host and port, your email username and your email password.

Once you’ve received these settings, you’re ready to go!

Hit Connect your email to start the process, and fill in the required fields.

A note about your password – you can definitely use Public Address with any IMAP/SMTP account, including google or microsoft, however, you may need to set a application specific password up for these accounts depending on your organisation’s security settings. We’ve got a great article on application specific passwords here.

Once you’ve entered those details please select ‘Test Connection’ – Public Address will then test the connection with your email server, which can take up to 60 seconds, before displaying a confirmation message that we’ve been able to successfully connect to your account.

Of course if you experience any difficulty with any this set up process, our support team is standing by using the message icon in the bottom right corner or via support@publicaddress.ai

.. _`Why can’t I add my Microsoft 365 account to Public Address?`:

Why can’t I add my Microsoft 365 account to Public Address?
-------
The Public Address application requires access to be able to perform certain actions in your email account in order to provide the full benefit of a premium subscription. Microsoft refers to these actions as ‘scopes,’ for example, when you first connect your Microsoft account we request access be able to send email from your email account, inside the Public Address application.

Some of these scopes require your administrator to approve access, and until your IT administrator approves this access, you won’t be able to use Public Address to send emails from your email account. This is why you’re receiving a message asking you to contact your IT administrator.

There’s three ways that your IT administrator can rectify this problem, and we’ve included all options below for your IT administrators to help them in whitelisting our application and some more information about how we securely manage your data.

**Information for IT administrators**

To ensure the integrity of your data, we only request access to the following scopes:

- Mail.Send, in order to be able to send emails on your user’s behalf and create tracking data on opens and engagements with links
- Mail.ReadWrite, in order to be able to use the messageid associated with the message we have sent on your user’s behalf to locate replies to this message and filter these into the platform
When we access your user’s mailbox, we will only ever access emails via the threadid, which identifies emails which have been sent via our platform.

Use the Public Address consent URI

Following the consent process below will allow your users to individually connect to the Public Address application. Please note that this must be completed by a user with admin privileges for your account.

https://login.microsoftonline.com/common/adminconsent?client_id=ed801945-cd65-4ee1-a1c9-e760bc5477a2&redirect_uri=https://go.publicaddress.app/settings/azure/callback

Allow your users to consent to access
You can allow your users to consent to access to external applications:

In the admin center, go to the Settings > Org settings > `Services <https://go.microsoft.com/fwlink/p/?linkid=2053743>`_ page, and then select User consent to apps.
On the User consent to apps page, select the option to turn user consent on or off.

The user will now be able to sign in to Public Address. You can view a Microsoft Help centre article here: https://docs.microsoft.com/en-us/microsoft-365/admin/misc/integrated-apps?view=o365-worldwide

Use a consent flow to grant user access
Azure Active Directory allows for you to grant permission for users to access certain applications. When you configure this workflow you will be notified that a user has requested access to Public Address.

The instructions below reference how to grant users permission to request access:

Sign in to the `Azure portal <https://portal.azure.com/>`_ as a global administrator.

Click All services at the top of the left-hand navigation menu. The Azure Active Directory Extension opens.

In the filter search box, type “Azure Active Directory” and select the Azure Active Directory item.

From the navigation menu, click Enterprise applications.

Under Manage, select User settings.

Under Admin consent requests (Preview), set Users can request admin consent to apps they are unable to consent to to Yes.

The Microsoft help article here steps you through this process: https://docs.microsoft.com/en-GB/azure/active-directory/manage-apps/configure-admin-consent-workflow


.. _`Why am I seeing a ‘This app isn’t verified’ message from Google?`:

Why am I seeing a ‘This app isn’t verified’ message from Google?
-------
If your employer uses G Suite Enterprise and you sign up for a premium subscription, you’ll need to ask your domain administrator to whitelist the Public Address platform to enable our application to check for replies to emails you’ve sent using Public Address.

Once your employer has whitelisted Public Address, the owner of your platform will need to confirm this under Platform Management.

If your platform owner has selected ‘Verify’ without the domain being whitelisted, you may see a message form Google saying ‘This app isn’t verified.’ Don’t worry, it’s completely safe to continue to use Public Address.

In order to do so immediately, please select ‘Advanced’ and then select ‘Go to Public Address.’

Don’t worry, your data is completely safe and Public Address is built from the ground up with industry leading security and authentication mechanisms to keep your data safe and secure. Public Address will be completing the Google verification process for this integration in the future, however, Google charges in excess of $100,000 Australian dollars to do so.

If you or your users continue to see this screen when connecting their account, please log a support ticket at support@publicaddress.ai and our team will reach out to help you through the domain whitelisting process.


.. _`How do I use the full features of Public Address with my G Suite account?`:

How do I use the full features of Public Address with my G Suite account?
-------
The Public Address application requires access to be able to perform certain actions in your email account in order to provide the full benefit of a premium subscription. Google refers to these actions as ‘scopes,’ for example, when you first connect your Google account we request access to the gmail.send scope, which allows you to send email from your email account, inside the Public Address application.

Some of these scopes require your administrator to approve access, and until your IT administrator approves this access, you’ll see an application unverified warning from Google. More information about this message is available `Why am I seeing a ‘This app isn’t verified’ message from Google?`_.

When you sign up for the plan, we’ll ask only for sensitive scopes, which don’t require administrator approval. But to unlock the full features of Public Address and display replies from journalists inside the application, you’ll need your domain administrator to complete a process called Whitelisting and enable the gmail.readonly scope, which allows the application to search your inbox for messages which have been sent as replies to emails you’ve sent from the Public Address platform.

Once your administrator has followed the steps below, you’ll need to go to G Suite Enterprise Authorisation, under Platform Management, and select ‘Verify.’ You’ll be prompted to log in and out of your Google account on the Public Address platform.

Depending on your browser, you may also need to clear your cookies associated with Public Address as Google’s OAuth process stores some of these settings in your cookies.

Below is some more information for your IT administrators to help them in whitelisting our application and some more information about how we securely manage your data.

Information for IT administrators
To ensure the integrity of your data, we only request access to the following scopes:

- gmail.send, in order to be able to send emails on your user’s behalf and create tracking data on opens and engagements with links
- gmail.readonly, in order to be able to use the messageid associated with the message we have sent on your user’s behalf to locate replies to this message

When we access your user’s mailbox, we will only ever access emails via the messageid, which identifies emails which have been sent via our platform.

Authorising the Public Address application is simple and only requires a couple of minutes of your time. The details of our application are below:

- Application name: Public Address
- Application ID: 626476583093-5u438ghhb62f6dt7vl4usqhhcren0onr.apps.googleusercontent.com

To enable access, simply head to the G Suite admin panel, select security and scroll to the bottom of this list to select App Access Control – or click on this link: https://admin.google.com/u/1/ac/owl/list?tab=apps. You’ll be presented with an overview, and you should now select manage third party app access.

Select ‘Configure new app’ and select ‘OAuth App Name or Client ID’. You can now either search for Public Address or copy and paste the application ID then select Public Address.

You’ll now be asked to provide Trusted or Blocked access – please select Trusted in order to enable the full benefits of Public Address.

Now select configure and you’re all set.

For more information about whitelisting apps, please visit Google’s help centre at https://support.google.com/a/answer/7281227?hl=en

We’re available at support@publicaddress.ai to answer any of your questions on this important subject.
