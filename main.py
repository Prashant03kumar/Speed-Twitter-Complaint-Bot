from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


SPEED_TEST_LINK="https://www.speedtest.net/"
PROMISE_DOWNLOAD=150
PROMISE_UPLOAD=10
TWITTER_EMAIL="prashantserver2@gmail.com"
TWITTER_PASSOWRD="kkkapilbhai"
TWITTER_LINK="https://x.com/home"
TWITTER_USERNAME="Speed_test3944"

# print(f"Password: '{TWITTER_PASSWORD}'")

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)

# 1->We will go to speed test link
driver.get(SPEED_TEST_LINK)

time.sleep(5)

continue_button = driver.find_element(By.CSS_SELECTOR, value="#onetrust-accept-btn-handler")
continue_button.click()
print("Continue Button clicked")

time.sleep(3)
#After clicking the continue pop-up click on "GO" button

go_button = driver.find_element(By.CSS_SELECTOR, value="[aria-label='start speed test - connection type multi']")
go_button.click()
print("Go button clicked")

time.sleep(50)
# for download<div class="result-item-container result-item-container-align-center">
# <span data-download-status-value="0.02" class="result-data-large number result-data-value download-speed">20.70</span>
download_speed_element = driver.find_element(By.CSS_SELECTOR, ".result-data-large.number.result-data-value.download-speed")
download_speed = float(download_speed_element.text)
print(f"Download Speed: {download_speed}")

# for upload <div class="result-item-container result-item-container-align-left">
# <span data-upload-status-value="0.01" class="result-data-large number result-data-value upload-speed">10.48</span>
upload=driver.find_element(By.CSS_SELECTOR,value=".result-data-large.number.result-data-value.upload-speed")
upload_speed=float(upload.text)
print(f"Upload Speed: {upload_speed}")
 
time.sleep(3)


## aria-label="start speed test - connection type multi"
##"[aria-label='start speed test - connection type multi']"

if download_speed<PROMISE_DOWNLOAD or upload_speed<PROMISE_UPLOAD:
#NOW GO ON THE TWITTer

    driver.get(TWITTER_LINK)

    time.sleep(5)

    #Click on SIGN IN button

    sign_in=driver.find_element(By.CSS_SELECTOR,value='[data-testid="loginButton"]')
    sign_in.click()
    print("Sign in button Clicked")

    time.sleep(5)
    # <div class="css-175oi2r r-1mmae3n r-1e084wi r-13qz1uu">flex
    email_input = driver.find_element(By.CSS_SELECTOR, "input[type='text']")  # Adjust the selector as needed
    email_input.send_keys(TWITTER_EMAIL)
    print("Email entered successfully!")


    # Wait and locate the "Next" button
    time.sleep(2)  # Wait to ensure the button is interactable
    next_button = driver.find_element(
        By.CSS_SELECTOR,
        "button.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-ywje51.r-184id4b.r-13qz1uu.r-2yi16.r-1qi8awa.r-3pj75a.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l"
    )
    next_button.click()
    print("Next button clicked successfully!")

    time.sleep(5)

    # ENTER YOUR PHONE NUMBER OR USERNAME
    user_name=driver.find_element(By.CSS_SELECTOR,value=".css-175oi2r.r-1mmae3n.r-1e084wi input")
    user_name.send_keys(TWITTER_USERNAME)
    print("User name entered successfully!")
    # <div class="css-175oi2r r-1mmae3n r-1e084wi">flex

    time.sleep(2)

    # Locate the "Next" button using the data-testid attribute
    next_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="ocfEnterTextNextButton"]')
    next_button.click()
    print("Next button clicked successfully!")


    time.sleep(5)

    # Find the password input field by its class or other attributes
    password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
    password.send_keys(TWITTER_PASSOWRD)
    print("Password Entered!")

    time.sleep(2)
    password.send_keys(Keys.RETURN)

    # # Login button
    # # <button role="button" class="css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-19yznuf r-64el8z r-1fkl15p r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l" data-testid="LoginForm_Login_Button" type="button" style="border-color: rgba(0, 0, 0, 0); background-color: rgb(239, 243, 244);">flex
    # login_button=driver.find_element(By.CSS_SELECTOR,value='[data-testid="LoginForm_Login_Button"]')
    # login_button.click()
    print("We logged in Twitter")

    # Wait for the page to load
    time.sleep(5)

    # Find the contenteditable div where text needs to be inserted
    tweet_textarea = driver.find_element(By.CSS_SELECTOR, "div[data-testid='tweetTextarea_0']")

    # Clear the current text if necessary
    tweet_textarea.clear()

    text=f"Hey @provider Internet Provider,why is my internet speed {download_speed}down/{upload_speed}up when i pay for {PROMISE_DOWNLOAD}down/{PROMISE_UPLOAD}up ?"
    tweet_textarea.send_keys(text)
    print("Text sent")

    # POST BUTTON
    post_button=driver.find_element(By.CSS_SELECTOR,value='[data-testid="tweetButtonInline"]')
    post_button.click()
    print("Tweet Posted!")
else:
    print("Speed is desirable !")