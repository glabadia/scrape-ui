from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
from errorCheck import hasNoResults
from utils import printDict, convert_to_text, trimm_list, ah_table, trimm_list_v2, sorted_auctionHouses

SLEEP_TIME: int = 20


def open_dropdownbox(driver):
    buttonPath = "//span[@data-toggle='tooltip']//button"
    # buttonPath = "//span[@data-toggle='tooltip']//button[@title='None selected']"
    auctionHouseButton = WebDriverWait(driver, SLEEP_TIME).until(
        EC.presence_of_element_located((By.XPATH, buttonPath)))
    auctionHouseButton.click()


def auctionHouseSearch(driver):
    auctionPath = "//div[@id='auctionsitecontainer']/span[@style='cursor: help; width: 100%;']/div[@class='btn-group open']/ul[@class='multiselect-container dropdown-menu']/li/a/label"

    auctionHouses = WebDriverWait(driver, SLEEP_TIME).until(
        EC.presence_of_all_elements_located((By.XPATH, auctionPath)))
    return auctionHouses


def unselect_AH(driver):
    active_AH = active_AH_list(driver)

    for ah in active_AH:
        sleep(.4)
        ah.click()


def active_AH_list(driver):
    auctionActivePath = "//div[@id='auctionsitecontainer']/span[@style='cursor: help; width: 100%;']/div[@class='btn-group open']/ul[@class='multiselect-container dropdown-menu']/li[@class='active']/a/label"

    active_AH = WebDriverWait(driver, SLEEP_TIME).until(
        EC.presence_of_all_elements_located((By.XPATH, auctionActivePath)))
    return active_AH


def auctionHouseClick(driver, auction_houses):
    #   list of auction houses
    converted_AH = convert_to_text(auction_houses)
    #   trimmed names of auction houses
    trimmed_list = trimm_list(converted_AH, "-")
    #   trimmed number of units from the list of auction houses
    num_units = trimm_list_v2(converted_AH, "-", "Units")
    #   dictionary with key = trimmed auction house names, and value = web element from auction_houses list
    ah_web_element = ah_table(trimmed_list, auction_houses)
    #   dictionary with key = trimmed auction house names, and value = num_units
    ah_units = ah_table(trimmed_list, num_units)

    # print(ah_web_element)

    #   sorted auction houses depending on number of units
    sorted_ah = sorted_auctionHouses(ah_units)
    print(f"Sorted Auction houses: {sorted_ah}")
    # printDict(f"{sorted_ah}")

    for auction_house in sorted_ah:
        sleep(.7)
        ah_web_element[auction_house].click()

#   conditionButton = "//select[@name='conditiongradefrom']"
#   driver.find_element_by_xpath(conditionPath).click()
#   options = "//select[@name='conditiongradefrom']/option"
#   driver.find_elements_by_xpath(options)[-1].click()


def sorted_auction_search(driver):
    auction_houses = auctionHouseSearch(driver)
    converted_AH = convert_to_text(auction_houses)
    trimmed_list = trimm_list(converted_AH, "-")
    num_units = trimm_list_v2(converted_AH, "-", "Units")
    ah_units = ah_table(trimmed_list, num_units)
    ah_web_element = ah_table(trimmed_list, auction_houses)
    sorted_ah = sorted_auctionHouses(ah_units)
    return sorted_ah, ah_web_element


def auctionHouse_webElement(driver):
    auction_houses = active_AH_list(driver)
    converted_AH = convert_to_text(auction_houses)
    trimmed_list = trimm_list(converted_AH, "-")
    num_units = trimm_list_v2(converted_AH, "-", "Units")
    ah_units = ah_table(trimmed_list, num_units)
    ah_web_element = ah_table(trimmed_list, auction_houses)
    sorted_ah = sorted_auctionHouses(ah_units)
    return sorted_ah, ah_web_element


def conditionGrade(driver):
    # form.idmain-search > div.row > div.col-lg-12 col-md-12 col-sm-12 fern-bg > div.panel panel-default col-lg-9 col-md-9 col-sm-10 search-panel basic-search radius-bottom-left radius-top-left > div.panel-body radius-bottom-left > div.row > div.col-lg-4 col-md-4 col-sm-4 form-align basic-search-second-panel > div.width-100per margin-left-right-none form-adjust

    conditionButton = "//form[@id='main-search']/div[@class='row']/div[@class='col-lg-12 col-md-12 col-sm-12 fern-bg']/div[@class='panel panel-default col-lg-9 col-md-9 col-sm-10 search-panel basic-search radius-bottom-left radius-top-left ']/div[@class='panel-body radius-bottom-left']/div[@class='row']/div[@class='col-lg-4 col-md-4 col-sm-4 form-align basic-search-second-panel']/div[@class='width-100per margin-left-right-none form-adjust']/select[@class='form-control width-40per fromconditiongrade conditiongradefrom']"

    print(driver.find_element_by_xpath(conditionButton).click())
    options = "/option"
    elements = driver.find_elements_by_xpath(conditionButton+options)
    # print(f"{elements[0].text}")
    elements[-1].click()


def searchFunc(driver):
    '''
    One role: Clicks the search button
    '''
    sleep(10)    # delay for 3 seconds to load more info

    try:
        searchPath = "//button[@class='btn btn-primary btn-search search']"
        searchButton = WebDriverWait(driver, SLEEP_TIME).until(
            EC.presence_of_element_located((By.XPATH, searchPath)))
        while searchButton:
            searchButton.click()
            searchButton = driver.find_element_by_xpath(searchPath)
        print("Search button clicked!")

    except Exception as e:
        print(f"Search function failed..[{e}]")

    sleep(10)  # regular value is 3
    # check if there are no results
    # noResultsPath = "div.no-result-message "
    # noResultsCheck = True if driver.find_element_by_css_selector(
    #     noResultsPath).get_attribute("style") == "display: none;" else calibrateSearch(driver)
    noResultsCheck = calibrateSearch(
        driver) if hasNoResults(driver) else True
    print(noResultsCheck)


def calibrateSearch(driver):
    '''
    if previous search yields a no-result-message status, initiate recalibration sequence
    '''
    # btsPath = "button.btn.btn-default.margin-left-15px.back-to-search"
    # btsButton = driver.find_element_by_css_selector(btsPath)
    print("Initiate Calibrate Search...")
    btsPath = "//div[contains(@class,'no-result-message')]//button[@type='button'][contains(text(),'Back to Search')]"
    btsButton = driver.find_element_by_xpath(btsPath)
    sleep(3)
    btsButton.click()

    marketReportPath = "input#marketreport.search-option"
    marketReportButton = driver.find_element_by_css_selector(marketReportPath)
    marketReportButton.click()

    sleep(2)  # delay by 2 seconds

    idirectAuctionPath = "input#idirectauction.search-option"
    idirectAuctionButton = driver.find_element_by_css_selector(
        idirectAuctionPath)
    idirectAuctionButton.click()

    sleep(2)

    mainSearchPath = "button.btn.btn-primary.btn-search.search"
    mainSearchButton = driver.find_element_by_css_selector(mainSearchPath)
    mainSearchButton.click()
