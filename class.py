from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

class InternetSpeedTwitterBot:
    SPEED_TEST_LINK = "https://www.speedtest.net/"
    TWITTER_LINK = "https://x.com/home"

    def __init__(self, promised_download, promised_upload, twitter_email, twitter_password, twitter_username):
        self.promised_download = promised_download
        self.promised_upload = promised_upload
        self.twitter_email = twitter_email
        self.twitter_password = twitter_password
        self.twitter_username = twitter_username
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.download_speed = 0
        self.upload_speed = 0

    def get_internet_speed(self):
        self.driver.get(self.SPEED_TEST_LINK)
        time.sleep(5)

        continue_button = self.driver.find_element(By.CSS_SELECTOR, value="#onetrust-accept-btn-handler")
        continue_button.click()
        print("Continue Button clicked")

        time.sleep(3)

        go_button = self.driver.find_element(By.CSS_SELECTOR, value="[aria-label='start speed test - connection type multi']")
        go_button.click()
        print("Go button clicked")

        time.sleep(50)

        download_speed_element = self.driver.find_element(By.CSS_SELECTOR, ".result-data-large.number.result-data-value.download-speed")
        self.download_speed = float(download_speed_element.text)
        print(f"Download Speed: {self.download_speed}")

        upload_speed_element = self.driver.find_element(By.CSS_SELECTOR, ".result-data-large.number.result-data-value.upload-speed")
        self.upload_speed = float(upload_speed_element.text)
        print(f"Upload Speed: {self.upload_speed}")

    def tweet_at_provider(self):
        if self.download_speed < self.promised_download or self.upload_speed < self.promised_upload:
            self.driver.get(self.TWITTER_LINK)
            time.sleep(5)

            sign_in = self.driver.find_element(By.CSS_SELECTOR, value='[data-testid="loginButton"]')
            sign_in.click()
            print("Sign in button clicked")
            time.sleep(5)

            email_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='text']")
            email_input.send_keys(self.twitter_email)
            print("Email entered successfully!")

            time.sleep(2)
            next_button = self.driver.find_element(
                By.CSS_SELECTOR,
                "button.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-ywje51.r-184id4b.r-13qz1uu.r-2yi16.r-1qi8awa.r-3pj75a.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l"
            )
            next_button.click()
            print("Next button clicked successfully!")

            time.sleep(5)

            user_name = self.driver.find_element(By.CSS_SELECTOR, value=".css-175oi2r.r-1mmae3n.r-1e084wi input")
            user_name.send_keys(self.twitter_username)
            print("User name entered successfully!")

            time.sleep(2)
            next_button = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="ocfEnterTextNextButton"]')
            next_button.click()
            print("Next button clicked successfully!")

            time.sleep(5)

            password_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
            password_input.send_keys(self.twitter_password)
            print("Password entered!")

            time.sleep(2)
            password_input.send_keys(Keys.RETURN)
            print("Logged in to Twitter")

            time.sleep(5)

            tweet_textarea = self.driver.find_element(By.CSS_SELECTOR, "div[data-testid='tweetTextarea_0']")
            tweet_textarea.clear()

            tweet_text = (f"Hey @provider Internet Provider, why is my internet speed "
                          f"{self.download_speed} down/{self.upload_speed} up when I pay for "
                          f"{self.promised_download} down/{self.promised_upload} up?")
            tweet_textarea.send_keys(tweet_text)
            print("Tweet entered")

            post_button = self.driver.find_element(By.CSS_SELECTOR, value='[data-testid="tweetButtonInline"]')
            post_button.click()
            print("Tweet posted!")
        else:
            print("Speed is desirable!")

# Usage
PROMISED_DOWNLOAD = 150
PROMISED_UPLOAD = 10
TWITTER_EMAIL=os.getenv('TWITTER_EMAIL')
TWITTER_PASSOWRD=os.getenv('TWITTER_PASSWORD')
TWITTER_USERNAME = "Speed_test3944"

bot = InternetSpeedTwitterBot(PROMISED_DOWNLOAD, PROMISED_UPLOAD, TWITTER_EMAIL, TWITTER_PASSOWRD, TWITTER_USERNAME)
bot.get_internet_speed()
bot.tweet_at_provider()
