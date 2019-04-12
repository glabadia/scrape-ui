from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

SLEEP_TIME: int = 10


def userLogin(un, pw, driver):
    """
    automates userLogin
    """
    # UserId, Password, btnlogin
    driver.find_element_by_id("UserId").send_keys(un)
    driver.find_element_by_id("Password").send_keys(pw)
    driver.find_element_by_id("btnlogin").click()


def userLoginIdirect(un, pw, driver):
    """
    automates userLogin
    """
    # Chrome
    # loginPath = "//div[@class='login_ipad visible-md visible-sm login_form']//a[@class='btn btn-primary'][contains(text(),'Login')]"
    # Firefox
    loginPath = "//div[@id='login_container_web']//a[@class='btn btn-primary'][contains(text(),'Login')]"
    # loginPath = "a.btn.btn-primary"
    loginButton = WebDriverWait(driver, SLEEP_TIME).until(
        EC.presence_of_element_located((By.XPATH, loginPath)))
    # loginButton = WebDriverWait(driver, SLEEP_TIME).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, loginPath)))
    loginButton.click()

    driver.find_element_by_id("username").send_keys(un)
    driver.find_element_by_id("password").send_keys(pw)
    driver.find_element_by_id("login-command").click()
