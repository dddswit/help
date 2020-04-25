# Slack Import

 

 

*

**What is Slack Import?**
   

    2.  Slack Users can import all of their messages, files, user information, channel information, etc. used in Slack into Swit.  
  
 
     

 

*

**Get Started with Slack Import**
   

    2. Tiers and Qualifications: Available in all Tiers, only the Master or Admin of the Workspace will have access
  2. 

*Note: There is a difference in the Slack Import feature in the Premium Tier. Click ‘****here’**** to see the Features of the Premium Tier.

* 
  6. You can only import data from Slack Public Channels.
  2.

*Bot messages, posts, or snippets of code cannot be imported, even if it is Public Channel data.*
      

 

*

*Please refer to Use Corporate Export in [Slack's Help Cente](https://slack.com/intl/en-kr/help/articles/201658943-Export-your-workspace-data)r to export data from Private channels and direct messages.*
   

    2. Method 1 - Get data at the Workspace creation step
  2. Clicking build on the Create Workspace page takes you to a page where you can select the data to import.
 4. You can select “Slack” here to import data from Slack.
  6. Method 2 -Import data from an existing Workspace
  2. Workspace Masters and Admins can enter Workspace Settings.
 4.  You can import data by clicking Import Data and selecting Slack.  
  
 
      

 

*

**Import Slack Data 1. File Upload**
   

   2. Method 1 - Import data from an existing Workspace
  2. From your desktop, you can build a new Workspace at Swit Home by importing data from Slack.
 4. Click Build a new Workspace
 6. Enter the name of Workspace and Swit URL and click the “Build” button.
 8.  Click “Slack”, then a new page will appear in a new browser tab where you can upload your file.  
Note: You can extract the data from https://my.slack.com/services/export  
  
 
  6. Method 2 - Import data from an existing Workspace
  2. From your desktop, click your Workspace name in the top left.
 4. Select Workspace Settings from the menu below and select the name of Workspace.
 6. Click Import data.
 8.  Click “Slack”, then a new browser tab will open where you can upload your file.  
Note: You can extract the data from my.slack.com/services/export  
  
 
  10. File Upload
  2. You can upload the data file extracted from Slack on this page.
  2. Files smaller than 2GB can be uploaded by drag and drop directly or pasted with a download link.
 4. Files larger than 2 GB can only be imported by pasting the download link.
  2. Currently, Swit only supports downloading links from Dropbox, Box, and Google links.
 4.  For Dropbox, you can force download by using dl = 1 as the query parameter in the URL.   
Related Links: https://help.dropbox.com/en-us/desktop-web/force-download 
 6.  In the case of Box, only Members who use a Swit Paid Tier can use the download link function.  
Related Links: <https://community.box.com/t5/Using-Shared-Links/Shared-Link-Settings/ta-p/50250#toc-hId--1187098569> 
 8. In the case of Google Links, you need to move to 'Get Shareable Links'> 'Link Sharing'> and check ‘All web users’ for the download link to work properly.
  8. If you move tabs or close the browser while uploading files, the upload will be canceled.
  6. Upload error
  2. If the zip file is not extracted from Slack, it will not be uploaded.
 4. Even if the zip file is extracted from Slack, it will not be uploaded if reprocessed.
 6. If the download link is wrong, it will not be uploaded.
      

  

 

*

**Importing Slack Data 2. Select User Information**
  

* After uploading the file, click the Next button to move to the User Information selection screen.
  

* There are five options for importing User Information.
  

*

*Get Slack User Information as is - When one Slack User and one Swit Member are matched 1: 1*
  

* Through this option, the Member gets all User Information from Slack.
  

* If there is email information in the imported Slack data, the email information is automatically entered into Swit.
  

* If there is no email information in the Slack data, the Member must enter the email data directly.
  

* If the email address that the Member enters is already in use by a Member participating in the Swit Workspace, it will be automatically matched.
  

* If the email address that the Member enters is already associated with a Swit Account but is not yet a Member of the Workspace, entering their email will automatically invite them to the Workspace.
  

* If the email address the Member enters is not yet associated with a Swit Account, it will be automatically registered with the email and Slack User Information the User entered, and the email will be automatically invited to the Workspace.
  

* In this case, the Display Name / Timezone information that was obtained from Slack will be used. 
  

* A password generation email will be sent to the email address automatically registered in Swit.
   

       2. The password generation email contains a password generation link.
  2. The password generation link expires 24 hours after the email was sent. 
 4. If you click the password creation link, you will be redirected to the password creation screen, and you will be logged out from the browsers.
 6. When you have finished entering your new password and have confirmed it, click Confirm to complete the password creation.
   4.  Note!! In the Advanced Tier, this feature is not supported because user invitations are made at the Dashboard level.  
  
 
  4.

***Get Slack User Information as is - When multiple Slack Users and one Swit Member are matched 1:several***
  2. If the email address that the Member enters is a Member of Swit and is participating in the Workspace, the Messages except User information from multiple Users of Slack will be combined and matched to one account.
 4. If the email address that the Member enters is associated with a Swit Account that is not a participating Member of the Workspace, they will be automatically invited to join the Workspace. After that, the Messages except the user information from multiple Users of Slack will be combined and matched to one account.
       

 

*

**If the email address that the Member enters is not associated with a Swit Account, they will be automatically registered to Swit with the email and Slack User Information the Member entered, and they will automatically be invited into the Workspace.**
   

       2. In the case of automatic Member registration, the Member’s display name is automatically assigned by the imported Slack User Information.
 4. The password of an automatically registered Member's account can be verified through the “Create Password” email sent to that email address.
  4.  Note!! In the Advanced Tier, this feature is not supported because user invitations are made at the Dashboard level.  
  
  
 
  4.

***Matching with Swit Member Information - The Member must select the matching Swit Member.***
  2. If you match a Slack User to a Swit Member 1:1, all messages and files are matched to the Swit Member.
 4.  If you match the data of multiple Slack Users to one Swit Member, the messages and file information of multiple Slack Users are matched to the Swit Member.  
  
 
  8.

***Import only message & file information (no User data) without signing the Member into Swit***
  2. The Slack User will be in the “Leave State” in the Swit Workspace and only the name / message / file information will be imported.
  2.  The Member will not be invited into the Swit Workspace.  
  
 
   12.

***Do not Import Data

***
  2.  All data for this Slack User is excluded from the import.  
  
 
       

 

*

***Custom***
   

      2.  This option can be selected when you want to apply different options to each Member.  
  
 
       

 

*

**Import Slack Data 3. Select Channel Information**
  

* After selecting the User Information method, click the Next button to move to the Channel Information selection screen.
  

* There are five options for importing Channel Information.
  

* Create Imported Channels as Public Channels
   

      2. Through this option, the User turns Slack Public Channels into Swit's Public Channels. 
 4.  If the Swit Workspace has a Channel with the same name as an existing Slack Channel, it will be renamed by adding the numbers 2, 3, and 4 etc. next to the Slack Channel Name.  
  
 
       

 

*

***Create imported Channels as Private Channels***
   

     2. Through this option, the User turns Slack Public Channels into Swit Private Channels. 
 4.  If a Swit Workspace has a Channel with the same name as an existing Slack Channel, it will be renamed by adding the numbers 2, 3, and 4 etc. next to the Slack Channel Name.  
  
 
      

 

*

***Combining Channels from Slack with Channels from Swit***
  

* Through this option, the Member turns multiple Channels from Slack into a single Channel on Swit.
  

* If a Swit Workspace has a Channel with the same name as an existing Slack Channel, the name is automatically matched.
  

* Members can also directly match Channels later if they wish.
  

*  If no Swit Channels overlap with Channels from Slack, you must select the Swit Channels directly.  
  
 
  

* Do not create Channels from Swit
   

      2.  By selecting this option, the Member does not transfer Channels from Slack into Swit.  
  
 
       

 

*

***Custom***
   

      2.  This option is selected when you want to apply different options to each Channel.  
  
 
   4. The Member who imports the Channel Information must be included in the Public / Private Channel.
  2.  If the Member who initially started the import is not yet involved in a newly created Channel, he or she will be automatically invited to the Channel.  
  
 
      

 

*

**Import Slack Data 4. Review and Proceed**
   

    2. After selecting the Channel Information, click Next to move to the final step, Review and Proceed.
 4. This screen summarizes the Member Information and Channel Information set by the Member.
 6.  Check the button below in order to accept and start the import. Then, click on the “Import” button to start the import.   
  
 
     

 

*

**Import Slack Data 5. Import History**
   

    2.  This page allows Members to review all import records by Workspace  
  
 
     

 

*

**Import Slack Data 6. etc... Go back to the beginning, Forced browser shutdown, etc.**
   

   2. Go back to the beginning
  2. On the page where you select User Information or Channel Information, click Data Import in the upper left.
 4. When you click it, a warning message appears asking if you want to go back to the beginning.
 6. If you click “OK” on this warning message, your previous settings will reset and you will be returned to the first page.
  6. Forced browser shutdown
  2. If the browser is closed during the import process, follow the aforementioned steps by clicking Workspace Settings → Import → Slack Import.
  10. Swit will temporarily save your Import progress
  

**Import Slack Data to Swit**

  

 Qualifications

 

* Workspace Master and Admins


* Free, Standard, Premium, and Premium Plus plans
  Important

 

* For standard exports, only Public Channel content is available for import.


* Bot messages, posts, code or text snippets are not available for import.
   

  

 

*

**Download your Workspace data from Slack**
   

   2.  To import Members, see Slack’s [email display settings](https://get.slack.help/hc/en-us/articles/228020667-Make-email-addresses-private) and make sure the box that displays email addresses is checked and saved.  
 4.  Depending on which Slack plan you have, download your Workspace data using Slack’s [Standard Export](https://get.slack.help/hc/en-us/articles/201658943-Export-your-workspace-data#use-standard-export) or [Corporate Export](https://get.slack.help/hc/en-us/articles/201658943#-use-corporate-export). 
   

* Once you download the Workspace data, please do not edit the .zip file or it will fail to import.
   

 

*

**Upload your Workspace data to Swit**
   

   2. Option 1: Upload data to a new Workspace.
  2. On your desktop, 
 4.  
 6. Option 2: Upload data to an existing Workspace.
    

