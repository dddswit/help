# SSO Authetication

 What is Single Sign-On (SSO)?
-----------------------------

   
 

* SSO authentication allows enterprise customers with large internal employees to register and manage multiple members of their domain account at once.
  

* If users use SSO, users can use Swit through an account managed by the company without registering.
  

* This reduces the risk of security such as password loss and weak password management. With SSO, system administrators no longer have to manage every employee's access to services. This can improve the efficiency of manpower utilization.
  

* Swit Premium supports SSO services through SAML 2.0, including G Suite & MS Azure and Okta.
  How to set up Single Sign-On (SSO)
----------------------------------



**Desktop** 

* After opening a Swit Premium account, Premium Master or Premium Administrator will be able to sign up employees collectively through SSO authentication setup.


* Only the Premium Master or Premium Administrator can access the Administration menu.


* Click the Administration button in the lower left corner of the screen.


* Click Authentication on the left tab.


* Users can select “Members sign in with an account and password created in Swit.” Or “Members sign in using SAML.”. Click on "Members sign in using SAML."


* The user can fill in items 1, 2, and 3 below after obtaining the information. The entry information varies depending on the IdP provider. See below for how to obtain IdP information. 
	 + If you use G Suite as your IdP Here
	 + If you use MS Azure as your IdP Here
	  


* In item 4, the Premium Master or Premium Administrator can choose whether members can “All members sign in through SSO” (which means SSO authentication only) or “Sign in using either the “Normal or “SSO”, depending on Member selection.” (which means that members are allowed to sign in using SSO and traditional ID / PW methods.)


* In the 5th Custom item, you can set the image and text that appear when logging in by company.  
Click “Upload” to upload the appropriate file. 
	 + In “Add SSO login screen text” users can fill in the text that appears when you log in.
	 + Click “Preview” to check if the registered image and text are displayed correctly.
	  


* When you have entered all the required information, click the Save button. The setting is now complete.
  Configure your identity provider: Issue and verify IdP, SSO URL, Id, certificate in G Suite
-------------------------------------------------------------------------------------------



**Desktop** 

* There are some things you need to do to set up G Suite as your identity provider. 
	 + You need to log in to the Google Admin console.
	 + You must have administrator privileges, not a regular account.
	  


* Go to admin.google.com and click Apps.


* Click the SAML apps.


* Click the plus (+) icon in the bottom right corner.


* Enable SSO for SAML Application page - Click SETUP MY OWN CUSTOM APP on the bottom left.


* On Google IdP Information page, enter information in the tab of this access route.

**Access Route**  
Sign in with Swit Premium Master or Premium Administrator account > Administration button (bottom left) > "Authentication Management" tab.

 
	 +  Copy "SSO URL" and paste it into “1. SAML 2.0 ENdpoint (HTTP)”
	
	 
	 +  Copy "Entity ID" and paste it into “2. Identity Provider Issuer”
	
	 
	 +  Click DOWNLOAD on Certificate to download the certificate file.
	
	 
	 +  Open the certificate file with “Text Edit” (the program for editing the text file) to copy the content.
	
	 
	 +  Paste the copied content into “3. Public Certificate” on the Authentication Management page. (You can paste the comments together.)
	
	 
	  


* On Custom App page, set Application Name.


* On Service Provider Details page, copy and paste the following value into each required field.

**ACS URL

**<https://saml.swit.io/saml/acs>  
**Entity ID

**[https://swit.io](https://swit.io/)

 


* On Attribute Mapping page, click ADD NEW MAPPING to create / edit the necessary information for Swit integration. usermail - Basic Information - Primary Email  
firstname - Basic Information - First Name  
lastname - Basic Information - Last Name



**Restrict entry and generation of first name and last name**  
 • 25 characters each  
 • Unable to use special characters and Unicode emoji  
 • If space is created at the beginning or end of the space, the system will delete it automatically.  
 • Treat 1 or more spaces as 1 space.



**Restrict entry Email Address**  
Local Part + 1 (@) + (Domain Part) = 254 limit

 


*  Users can check the icon of the service created by the administrator at Google Admin > Apps > SAML Apps page. 
	 + Click on the rightmost menu button and change the status to “On for everyone.”
	  


*  You can check the IdP information of the existing application in the Apps icon> Service Provider Details> Manage certificate.
  Configure your identity provider: Issue and verify IdP, SSO URL, Id, certificate in MS Azure
--------------------------------------------------------------------------------------------



**Desktop** 

* To set up Ms Azure as an identity provider, you must have an MS Azure account with administrator privileges.


* Go to portal.azure.com and log in, then click Azure Active Directory on the left tab. 
	 + On the new page that appears, click “Enterprise applications” button in the middle left.
	 + Then on the All applications page, click on ‘+ New application’ in the upper left corner.
	 + Then click Non-gallery application in the upper right corner.
	 + Enter the name of the new application in the window that appears on the right and click ‘Add’ at the bottom.
	  


* You can now set up single sign-on for your new application. 
	 + Click Single sign-on on the left tab.
	 + Click the SAML button. Then “Set up Single Sing-On with SAML page” appears.
	 + Click the pencil button in the upper right corner to enter the required information on Basic SAML Configuration. Then fill in the following information in Identifier (Entity ID) and Reply URL respectively.
	 

**Identifier

**[https://swti.io](https://swti.io/)  
**Reply URL

**<https://saml.swit.io/saml/acs>

 
	 + Click the pencil button in the upper right corner to enter / edit the required information on User Attributes & Claims. And click the “(+) Add new claim” button on the User Attributes & Claims page and enter the following information:
	  firstname - user.givename  
lastname - user.surname  
useremail - user.mail  
  
**OR**  
  
username - user.displayname  
useremail - user.mail



**Restrict entry and generation of first name and last name**  
 • 25 characters each  
 • Unable to use special characters and Unicode emoji  
 • If space is created at the beginning or end of the space, the system will delete it automatically.  
 • Treat 1 or more spaces as 1 space.



**Restrict entry Email Address**  
Local Part + 1 (@) + (Domain Part) = 254 limit

 


* Click “Download” button next to Certificate (Base 64) to download the certificate file on SAML Signing Certificate. 
	 + Open the certificate file with “Text Edit” (the program for editing the text file) to copy the content.
	 + Paste the copied content into “3. Public Certificate” on the Authentication Management page. (You can paste the comments together.)
	 + Get information from the Set up step.
	 + Copy "Login URL" and paste it into “1. SAML 2.0 ENdpoint (HTTP)”
	 + Copy "Azure AD Identifier" and paste it into “2. Identity Provider Issuer”
	  
  Check the Single Sign-On (SSO) setup screen
-------------------------------------------



**Desktop** 

* If the authentication settings you saved are correct, the screen will appear where the SSO configurator can log in to the SSO account.


* The SSO configurator must log in to the account corresponding to the SSO service.


* After you successfully log in to your SSO account, you will receive a SSO Connection Successful message.


* If there is a problem with the settings you saved, you will receive a message that the SSO configurator failed to set up SSO.
  Send Single Sign-On (SSO) activation mail
-----------------------------------------



**Desktop** 

* If the SSO configurator has correctly set up authentication, all active members will receive a binding mail.


* Members can click “Connect Accounts” button in the binding mail, and then click “Authenticate with SAML” on the subsequent page to enter the connected company's Home.


* Links within these messages are only valid for 24 hours.


* If the link in the mail expires, the user can request a premium master or administrator to resend the SSO-activated mail. (Click on Member and Groups> Member Management> Select Members> Send the SSO binding email button)

**The following functions cannot be used when using single sign-on (SSO).**  
 • Sign Up Mode  
 • Change email address  
 • Invite members to premium space  
 • Change account name

 
  