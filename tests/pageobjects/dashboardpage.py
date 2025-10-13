
from selenium.webdriver.common.by import By

class Dashboard_page:
    def __init__(self,driver):
        self.driver=driver

    # xpath
    user_logged_in = (By.XPATH, "//span[@data-qa='lufexuloga']")

    def get_user_logiin(self):
        return self.driver.find_element(*Dashboard_page.user_logged_in)

    def user_logged_in_text(self):
        return self.get_user_logi().text()