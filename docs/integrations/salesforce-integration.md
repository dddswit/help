# Salesforce Integration

**Swit and Salesforce.com Integration** 

 The purpose of this article is to demonstrate how to connect Swit to Salesforce.com (hereafter SFDC). The workspace master or admin of all the tiers of the Swit platform—Free, Standard, Advanced, and Advanced Plus—can make integrations between Swit and SFDC. SFDC users also can make integrations with Swit, only when they belong to the following tiers of the SFDC platforms: Enterprise, Unlimited, Developer, and Performance. So, are you ready to make the integration? Let’s start!

 

***1.***

***From Creation to Authorization***

  Choose a workspace that you want to integrate with SFDC and click on it. I will choose the “Swit Tech” workspace to demonstrate.

 Once you have clicked on the selected workspace, you will be directed to the inside of the workspace. Locate the “Store” button on the bottom left corner and click on it to proceed.

 Now, a new screen will appear. Please locate the “Salesforce” link on the left corner and click on it.

 Once you have clicked on the “Salesforce” link, the following screen will appear. Click the “Connection” link to proceed.

 You will be directed to a screen entitled “Salesforce,” where you can begin to synchronize SFDC and Swit.

 Locate the “+Add Connection” button on the upper right corner and click on it. Then, a new box entitled “New Connection” will appear, asking you to name the connection that you desire to make. I will name the connection “Walkthrough (Test)” to demonstrate.

 Once you have clicked on the “Confirm” button, the indicator that you have tried to make SFDC and Swit integration will appear on a screen, but with a “Not Authorized” label under “Status”.

 Please click the “Authorize” link in order to make the integration.

 The “Authorize Connection” box will then appear and ask you to choose your SFDC environment: (1) Production, (2) Sandbox. Please choose one that fit your needs. I will choose “Production” to demonstrate. Once you have made your choice, click the “Authorize” button to continue.

 You will be directed to the SFDC’s login page. A SFDC account is required to integrate SFDC with Swit, and, here, you will first login to connect your account. After entering your login information, you will be asked to choose either deny or allow access. Click “Allow” to grant access. 

 You are now ready to integrate SFDC with Swit. Please return to the screen entitled “Salesforce,” where you previously saw the “Not Authorized” label. Now, the label is changed to “Authorized,” ensuring SFDC and Swit’s synchronization.

 If you want to revoke access for SFDC and Swit’s connection on this object, click on the “Revoke Access” button, then follow the instructions.

 It should be noted that there is a hidden feature in the “Salesforce” section. Once you bring the cursor on the right side of “Revoke Access,” Swit will display an icon with three dots. Clicking the icon will give you two options: (1) Edit, (2) Disconnect.

 The “Edit” button allows you to change the name of the SFDC and Swit connection.

 The “Disconnection” button will enable you to disconnect the SFDC and Swit link. Note that this feature will disconnect all associated tasks on the object.



***2.***

***From Authorization to Configuration*** 

 Users can specify the objects and corresponding fields in SFDC—i.e. Account, Contacts, Lead, Opportunity, Task, Case, List Email, Report, Group, Note, Content Document—that they can access through this connection. Click the “Configure” link to specify the objects and corresponding fields in SFDC.

 Once you have clicked on the “Configure” button, the “Available Salesforce Objects” screen will appear for you to add or remove SFDC objects.

 Locate the “+ Add Salesforce Object” link on the upper right corner and click on it.

 The “Add Salesforce Object” box will then appear on your screen. Bring the cursor to the gray box, where it says “Please select an object.” Click on it to proceed.

 The dropdown will provide you several SFDC objects that are not currently in your “Available Salesforce Objects” screen.

 Please choose one that fits your need, one at a time. I will select “Content Document” to demonstrate.

 Click the “Confirm” button to proceed.

 As you will see below, the “Content Document” object is now included in the “Available Salesforce Objects” screen.

 You have successfully added an object!

  If you want to remove any objects from the “Connect Salesforce Objects” screen, simply click the “Remove” button under “Operations.” The following warning then will appear to make sure you want to disconnect the connection: 

 “Once disconnected, all linked SFDC objects on the Swit task card will disappear.”

 As you know, every SFDC object has fields attached to it. Swit allows you to add fields to the object by simply clicking the “Fields” button under “Operations.” I will choose “Content Document” to demonstrate.

  Once you have clicked on the “Fields” button, the window entitled “Content Document Fields” will appear on your screen. Bring the cursor on the gray box, where it says “Available Field,” and click on it.

 The dropdown provides available fields, allowing you to choose one value from a list. Here, you can specify corresponding fields of the object in SFDC that you can access through this connection. I will choose “Title” to demonstrate.

  One you have clicked on “Title,” the “+Add” button which was grayed out on the right side of the box will turn blue, indicating that the “Title” is ready to be add on the object you have selected. Click on the “+Add” button to proceed.

 Now, you see that the “Title” field is bumped up to the parent node: selected fields. Click on the “Confirm” button to finalize your choice.

 Once you have clicked the “Confirm” button, the following message will appear on your left bottom screen: “The field has been updated successfully.”

  



***3.***

***From Configuration to Application***

 If you want to go back to your “Workspace List” screen, click the “Home” button on the bottom of the left-hand menu. Click the icon to proceed.

 The browser will then be redirected back to the “Workspace List” screen.

 Since you have chosen the “Swit Tech” workspace to demonstrate, click the workspace to check its synchronization with SFDC.

 Once you have clicked on the selected workspace, you will be directed to the inside of the workspace. Locate the “Project Box” button and click on it.

 Now, we need to create a project. Locate the “+” button in the “Projects” box and click on it. This feature will give you two options: (1) Create Project and (2) Create Folder. Click the “Create Project” button.

 Once you have clicked on the “Create Project” button, the following box will appear on your screen so that you can name the project. I will name the project “Integration Walkthrough” to demonstrate and confirm it.

 As you see, the “Integration Walkthrough” project has been created.

 It is time to create a project card. Locate the “+Add a Card” button and name the card. Then, click on the “Enter/Return” button to proceed. I will name the card “Example” to demonstrate.

 The Project card entitled “Example” has been successfully created.

 Please double-click the card to display the card’s details.

 The screen above demonstrates the card’s details. As you see, the SFDC logo appears on the bottom of the right-hand side of the page in the card, ensuring that the “Swit Tech” workspace has been successfully integrated with SFDC. The logo is displayed when there is at least one authorized connection. Yet, notice that no Salesforce objects have not yet linked with this card. Hence, it is time to link the SFDC objects with this card. 

 Click the “Associate” link. The following screen entitled “Associate” will appear on your screen.

  First, we need to choose a connection. Click the “Please select a connect” dropdown. This will provide a list of available connections. Click the “Walkthrough (test)” connection and confirm it.

 Secondly, you must select a SFDC object. Please locate the “Please Select an Object Type” dropdown and click on it. The dropdown will give you available object types for you to choose. I will choose “Opportunity” to demonstrate.

 Third, you can also choose an object data in the dropdown entitled “Please Select an Object Data.” Click the dropdown to see what is available for you to add.

  I will choose “Pyramid Emergency Generators” to demonstrate. Please click the “Confirm” button to proceed.

 Now, you will be able to see that “Opportunity 1: Pyramid Emergency Generators” is added on the integration box.

 The “Detail” link in the integration box provides more information about the contact you have made. 

  Here, you can change details.

 All Swit users can make a change from the dropdown information. 

 The change made here can be reflected in the SFDC by clicking on the “Apply to SFDC” link. A few things need to be pointed out. First, changes made in Swit are reflected in the SFDC, and

*vice versa*. Second, when a new activity—(1) Connecting an object, (2) Disconnecting an existing object, and (3) Making an update to an existing object—occurs a notification is sent to the assigned members and followers. 

 Look! Congratulations! Your Swit and SFDC have been connected successfully!

 Guess what? You can make a change from the SFDC, and the change made over there can be reflected in Swit. I will show you how to make a change from the SFDC. First, go to your SFDC and locate the “App Launcher” button on the top left corner.

 Once you have clicked on the button, the following screen will appear. Locate the “Opportunities” button and click on it to proceed.

 As you see, the “Pyramid Emergency Generators” that you have connected via Swit is listed under the “Opportunities” section.

 Click the “Pyramid Emergency Generators” link to proceed. 

 Now, a new screen will appear. Please, locate the “Details” button and click on it.

 In the following screen, locate “Type” button and click on it. 

 The dropdown will provide you several options for you to choose. 

 I will choose the “New Customer” option to demonstrate.

 Now, go back to “Opportunity 1: Pyramid Emergency Generators” in your Swit card, and click the “Detail” link. Yes! As you see, you have successfully made a change from the SFDC!

