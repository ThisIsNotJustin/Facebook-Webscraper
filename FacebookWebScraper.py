from twilio.rest import Client
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time

## twilio and chrome driver information make sure to provide your own
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)
service = Service('')
driver = webdriver.Chrome(service=service)


def scraper():
    ## go to facebook
    driver.get("https://www.facebook.com/")
    
    ## log in
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))
    username.clear()
    username.send_keys("") ## make sure to provide your username
    password.clear()
    password.send_keys("") ## make sure to provide your password
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    
    ## wait 30 seconds to give time to approve initial login
    time.sleep(30) 
    ## go to the Asoro's Goldens group
    driver.get("https://www.facebook.com/groups/asorosgoldens")
    while True:
        time.sleep(300)
        driver.refresh()
        
        ## check for keywords in potential posts in the facebook group
        puppy = driver.find_element_by_xpath("//*[contains(text(), 'puppy') or contains(text(), 'born') or contains(text(), 'pregnant')]")
        ## if puppy is mentioned, send a text that the word puppy was used in a post
        if "puppy" in puppy.text:
            ## create text
            ## make sure to provide your twilio number in the from section 
            ## and provide the number you want to text in to to section
            message = client.messages.create(
                from_='', 
                body='Puppy was mentioned in the Asoro\'s Goldens Group!',
                to=''
            )
            ## send this message
            print(message.sid)
        ## if born is mentioned, send a text that puppies were born
        if "born" in puppy.text:
            ## create text
            ## make sure to provide your twilio number in the from section 
            ## and provide the number you want to text in to to section
            message = client.messages.create(
                from_='',
                body='Golden Retriever puppies were born!!!',
                to=''
            )
            ## send this message
            print(message.sid)
        ## if pregnancy is mentioned, send a text that pregnancy was mentioned in the group
        if "puppy" in puppy.text:
            ## create text
            ## make sure to provide your twilio number in the from section 
            ## and provide the number you want to text in to to section
            message = client.messages.create(
                from_='',
                body='Pregnancy was mentioned in the Asoro\'s Goldens Group!',
                to=''
            )
            ## send this message
            print(message.sid)
scraper()