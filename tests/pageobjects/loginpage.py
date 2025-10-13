

from selenium import webdriver
from selenium.webdriver.common.by import By
class LoginPage():
    def __init__(self,driver):
        self.driver=driver

    # Page Locators
    username = (By.ID, "login-username")
    password = (By.NAME, "password")
    submit_button = (By.XPATH, "//button[@id='js-login-btn']")
    # forgot_password_button = (By.XPATH, "//button[normalize-space()='Forgot Password?']")
    error_message = (By.XPATH,"//div[@data-qa='rixawilomi']")
    free_trail = (By.XPATH, "//a[normalize-space()='Start a free trial']")

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)
    def get_password(self):
        return self.driver.find_element(*LoginPage.password)
    def get_submitbutton(self):
        return self.driver.find_element(*LoginPage.submit_button)
    def get_errormessage(self):
        return self.driver.find_element(*LoginPage.error_message)
    def get_free_trail(self):
        return self.driver.find_element(*LoginPage.free_trail)

    def Login_page(self,user,pwd):
        self.get_username().send_keys(user)
        self.get_password().send_keys(pwd)
        self.get_submitbutton().click()


    def get_error_message_text(self):
        return self.get_errormessage().text
    def get_free_trail(self):
        return self.get_free_trail().click()


