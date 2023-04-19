# Facebook-Webscraper for Golden Retriever Puppies!
This Python script uses Selenium to monitor a specific Facebook group, Asoro's Goldens, and sends text messages if specific keywords related to puppies are found in the posts of the group.

![](https://github.com/ThisIsNotJustin/Facebook-Webscraper/blob/main/AsoroLogo.png)

Requirements:

TWILIO (make sure to provide your own account_sid, auth_token, and phone numbers)

SELENIUM (make sure to have the chrome webdriver installed and provide the path to the executable in the service variable)

A Facebook account with access to the group you want to monitor

Usage:

Fill in your Facebook account credentials in the username.send_keys("") and password.send_keys("") lines

Fill in your Twilio account credentials and phone number in the following lines: 
account_sid = '', auth_token = '', from_='', and to=''

Fill in the path to your chrome webdriver in the service = Service('') line

Fill in the URL of the Facebook group you want to monitor in the driver.get("") line (currently this is the Asoro's Goldens group

Run the script

![](https://github.com/ThisIsNotJustin/Facebook-Webscraper/blob/main/AsoroGroup.png)

Wait for the script to find any posts with the specified keywords (currently "puppy," "born," or "pregnant") and send you a text message notification

![](https://github.com/ThisIsNotJustin/Facebook-Webscraper/blob/main/twilio.jpeg)

Note: The script waits for 30 seconds after logging in to give time to approve the initial login and refreshes the page every 5 minutes to check for new posts. You can adjust the sleep time and refresh rate to fit your needs.
