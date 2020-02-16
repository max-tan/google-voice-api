from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def Start():
    global main_window, driver
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)
    driver.get("https://voice.google.com/")
    main_window = driver.current_window_handle


class Login:
    def __init__(self, email, password):
        self.email = email
        self.password = password

        driver.find_element_by_xpath("//a[@class='signUpLink']").click()
        time.sleep(0.5)
        emailField = driver.find_element_by_xpath("//input[@type='email']")
        emailField.send_keys(email)
        driver.find_element_by_xpath("//div[@id='identifierNext']").click()
        time.sleep(1)
        passwordField = driver.find_element_by_xpath("//input[@type='password']")
        passwordField.send_keys(password)

        driver.find_element_by_xpath("//div[@id='passwordNext']").click()
        time.sleep(5)


def Messages():
    driver.execute_script('''window.open("https://voice.google.com/u/0/messages","_blank");''')
    windows = driver.window_handles
    driver.close()
    driver.switch_to.window(windows[1])

class Message():
    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message

        if '\n' in message:
            message = message.split('\n')
        else:
            message_ = []
            message_.append(message)
            message = message_

        time.sleep(2)
        driver.find_element_by_xpath("//div[@aria-label='Send new message']").click()
        phoneNumberField = driver.find_element_by_xpath("//input[@id='input_1']")
        phoneNumberField.send_keys(recipient)
        phoneNumberField.send_keys(Keys.RETURN)
        messageField = driver.find_element_by_xpath("//textarea[@aria-label='Type a message']")

        for i in message:
            messageField.send_keys(i)
            messageField.send_keys(Keys.SHIFT + Keys.RETURN)
        driver.find_element_by_xpath("//gv-icon-button-ng2[@label='Send message']").click()
        time.sleep(2)
        Messages()

def Quit():
    time.sleep(2)
    driver.quit()


