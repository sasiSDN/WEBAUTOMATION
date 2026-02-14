import time
import allure
import pytest
from selenium import webdriver
from tests.pageobjects.loginpage import LoginPage
from tests.pageobjects.dashboardpage import Dashboard_page
@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    return driver

@allure.epic("LOGIN Test")
@allure.feature("TC1-Negative TC")
@pytest.mark.negative
def test_login_negative(setup):
    driver=setup
    login_page=LoginPage(driver)
    login_page.Login_page(user="s.sasinaidu@gmail.com",pwd="admin")
    time.sleep(5)
    error_message=login_page.get_error_message_text()
    assert error_message == "Your email, password, IP address or location did not match"
    driver.close()

@allure.epic("LOGIN Test")
@allure.feature("TC2-Positive TC")
@pytest.mark.positive
def test_login_positive(setup):
    driver=setup
    login_page=LoginPage(driver)
    login_page.Login_page(user="naidu681999@amazon.com",pwd="Naidu@123")
    time.sleep(10)
    dashboardpage=Dashboard_page(driver)
    assert "Login - VWO" in driver.title
    # assert "sz" in dashboardpage.user_logged_in_text()

    # f --alluredir = allure_result