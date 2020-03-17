from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

SLEEP_TIME: int = 10  # 20


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


def userLoginATNZ(un, pw, driver):
    """
    automates userLogin
    """
    # Chrome
    # Firefox
    # username = "//input[@id='UserId']"
    username = "//input[@placeholder='Email Address']"  # June 26, 2019
    # username = "//input[@placeholder='Username']"  # June 24, 2019
    # password = "//input[@id='Password']"
    # password = "//input[@placeholder='Password']"
    # September 17, 2019
    password = "//div[contains(@class,'input-group-sm flex-nowrap')]//input[@placeholder='Password']"
    password = "//input[contains(@class,'form-control p-1')]"
    # enterLoginPath = "//input[@value='Login']"
    # enterLoginPath = "//button[@id='btnlogin']"  # June 24,2019
    # June 26,2019
    # enterLoginPath = "//input[@class='btn btn-sm btn-kiwi-orange px-4 mb-3']"pypypython scraper_ui.py

    # December 18,2019
    enterLoginPath = "//input[@class='btn btn-sm btn-kiwi-orange px-5 py-0 rounded-0 mb-3']"


    loginPath = "//button[@id='login-btn']"  # June 24,2019
    # loginButton = WebDriverWait(driver, SLEEP_TIME).until(
    #     EC.presence_of_element_located((By.XPATH, loginPath)))
    loginButton = driver.find_element_by_xpath(loginPath)  # June 24, 2019
    loginButton.click()  # June 24, 2019

    driver.find_element_by_xpath(username).send_keys(un)
    # driver.find_element_by_xpath(password).send_keys(pw)
    #   update September 17, 2019
    # WebDriverWait(driver, SLEEP_TIME).until(
    #     EC.presence_of_element_located((By.XPATH, password))).send_keys(pw)
    driver.find_elements_by_xpath(password)[1].send_keys(pw)

    # driver.find_element_by_xpath(password).send_keys(u'\ue007')
    # enterLoginButton = WebDriverWait(driver, SLEEP_TIME).until(
    #     EC.presence_of_element_located((By.XPATH, enterLoginPath)))
    enterLoginButton = driver.find_element_by_xpath(enterLoginPath)
    enterLoginButton.click()
