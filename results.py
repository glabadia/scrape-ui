from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils import printList, destruct_info_upd, createDirectory, deconstruct_details
from bs4_searchTags import destruct_basic, destruct_adv
from time import sleep, time
from search import calibrateSearch
from errorCheck import hasNoResults
WAIT_MORE_IMG: int = 40
EXPAND_WAIT_TIME: int = 20  # 50
WAIT_TIME: int = 25  # 25
SLEEP_TIME: int = 10
FAST_TIME: int = 5


def expandVehicleInfo(driver):

    expandPath = "//div[@id = 'home']/div[@class = 'search-results hide-in-toggle']/div[@class = 'panel panel-default search-heading']/div[@class = 'panel-heading search-result-heading']/div[@class = 'row header-content']/div[@class = 'col-lg-7 col-md-7 col-xs-7 photo-details-heading']/div[@class = 'col-lg-5 col-md-5 col-xs-5 photo-heading']/div[@class='checkbox-all-vehicle']/div[@class='visible-md visible-lg right-expand-all']"
    # /a[@class='expand-all-view']"
    # sleep for 10 seconds to allow the browser to populate data, and fill the div with desired results.
    sleep(10)

    # Purchase Report ATNZ
    # ATNZ Sales Report
    # ATNZ Sales Performance Report
    expandButton = driver.find_element_by_xpath(expandPath)

    sleep(3)  # Allow for the loader image to fade out in the browser
    expandButton.click()


def expandVehicleInfoIdirect(driver):
    # sleep for 7-15 seconds to allow the browser to populate data, and fill the div with desired results.
    # expandPath = "//div[@class='visible-md visible-lg right-expand-all']"
    # firefox
    print("Waiting to populate data..")
    print()

    # sleep(SLEEP_TIME)  # Allow for the loader image to fade out in the browser
    isLoaderPresent = False
    # while not isLoaderPresent:
    isLoaderPresent = waitLoader(driver)

    if isLoaderPresent:
        hasExpanded = False
        print("Loader gone!")
        print()
        # startExpand, endExpand = time(), time()
        while not hasExpanded:
            # check if No search results exist.
            if hasNoResults(driver):
                print("No Search results triggered in search.")
                break
            hasExpanded = expandButton(driver)

    else:
        print("Sorry. Page is still loading..")


def expandButton(driver):
    startExpand = time()
    plusSignFirefox = "//i[@class='glyphicon text-left expand-icon glyphicon-plus-sign']"
    minusSignFirefox = "//i[@class='glyphicon text-left expand-icon glyphicon-minus-sign']"
    try:
        expand = WebDriverWait(driver, EXPAND_WAIT_TIME).until(
            EC.presence_of_element_located((By.XPATH, plusSignFirefox)))
        expand.click()
        hasExpanded = driver.find_element_by_xpath(minusSignFirefox)
        print(f"Expansion Success! {(time() - startExpand):.1f} seconds.")
        return hasExpanded

    except Exception as e:
        endExpand = time() - startExpand
        print(
            f"Error: Expand button has failed to expand-- Time: {endExpand:.1f} seconds {e}")
        return False


def waitLoader(driver):
    startloader = time()
    loaderOnInvisible = "//div[@id='loader'][contains(@style,'display: none;')]"
    isLoaderPresent = False
    try:
        isLoaderPresent = WebDriverWait(driver, WAIT_TIME).until(
            EC.presence_of_element_located((By.XPATH, loaderOnInvisible)))
        print(f"Loader gone in {(time() - startloader):.1f} seconds.")
        return isLoaderPresent
    except Exception as e:
        endLoader = time() - startloader
        print(
            f"Error: Loader is still present -- Time: {endLoader:.1f} seconds {e}")
        return False


def retrieveSearchResultsOnePage(driver):
    #   vehicleListPath = 'div[id=^'vehicle']'
    # vehiclePath = "div[id=^'vehicle']"
    # vehiclePath = "//div[starts-with(@id,'vehicle')]"
    #   the info beside the main picture
    vehiclePath = "//div[@class='data-container']"
    vehicleInfoList = driver.find_elements_by_xpath(vehiclePath)
    # printList(vehicleInfoList)No Search results triggered in search.
    return vehicleInfoList


def retrieveInfo(driver):
    allVehicles = []
    vehicleInfoPath = "//div[@class='col-lg-12 search-result-container']"
    containerSelectors = driver.find_elements_by_xpath(vehicleInfoPath)
    for container in containerSelectors:
        allVehicles.append(destruct_info_upd(container))

    return allVehicles


def retrieveInfoUpd(driver):
    """
    Retrieves all info in idirect browser
    A.K.A getting the meat...
    """
    # //div[starts-with(@id,'VehicleDetail')]
    allVehicles = []
    vehicleInfoPath = "//div[@class='col-lg-12 search-result-container']"
    containerSelectors = driver.find_elements_by_xpath(vehicleInfoPath)
    for container in containerSelectors:
        allVehicles.append(destruct_info_upd(container))

    return allVehicles


def retrieveInfoDetail(driver):
    vehicleDetails = []
    vehicleDetailPath = "//div[starts-with(@id,'VehicleDetail')]"
    containerDetailList = WebDriverWait(driver, WAIT_TIME).until(
        EC.presence_of_all_elements_located((By.XPATH, vehicleDetailPath)))
    for container in containerDetailList:
        vehicleDetails.append(deconstruct_details(container))

    return vehicleDetails
    # return containerDetailList
    # for loop traverse


def retrieveAllInfo(driver):
    vehicleInfo = []
    # basicInfoPath = "//div[@class='col-lg-12 search-result-container']"
    # advInfoPath = "//div[starts-with(@id,'VehicleDetail')]"
    # basicInfoList = driver.find_elements_by_xpath(basicInfoPath)
    # advInfoList = driver.find_elements_by_xpath(advInfoPath)
    # for basic, adv in zip(basicInfoList, advInfoList):
    #     vehicleInfo.append(
    #         (destruct_info_upd(basic), deconstruct_details(adv)))
    basic = destruct_basic(driver)
    # sleep(WAIT_MORE_IMG)
    sleep(WAIT_TIME)
    adv = destruct_adv(driver)
    for b, a in zip(basic, adv):
        vehicleInfo.append((b, a))

    return vehicleInfo


def retrieveInfoTest(driver):
    """
    Tests the 100th element of the div
    """
    #
    vehicleInfoPath = "//div[starts-with(@id,'VehicleDetail')]"
    containerSelectors = driver.find_elements_by_xpath(vehicleInfoPath)

    return containerSelectors[-1].text


def vehicleDetailInfo(driver, vehiclesList):
    # info
    # //div[@class='col-lg-12 search-result-container']
    # info_onlyleftside
    # //div[@class='search-result-panel auction-detail-panel']
    # info_rightside
    # //div[@class='search-result-panel hide-in-mobile pricing-container-panel']
    # images
    # //div[contains(@class,'search-result-additional-panel additional-detail-panel')]
    vehicleDetailList = ""
    for vehicle in vehiclesList:
        vehicleDetailsPath = "div.data-container"
        vehicleDetailsPane = driver.find_element_by_css_selector(
            vehicleDetailsPath)
        vehicleDetailList = vehicleDetailsPane.text.split('\\n')

    #   span#IBCNum123456789.pull-right
    #   chassisNumPath = "//span[starts-with(@id,'IBCNum')]"
    #   year = "//span[starts-with(@id,'year')]"
    #   makeModelPath = "//span[starts-with(@id,'cInfo')]"
    #   chassisPrefix  = "//span[starts-wth(@id,'chassis')]"
    #   chassisPrefix  = "//span[starts-wth(@id,'chassis')]"

    return vehicleDetailList


def fetchIBCNum(driver):
    ibcNumSelector = "//span[starts-with(@id,'IBCNum')]"
    ibcNumbers = driver.find_elements_by_xpath(ibcNumSelector)
    # yorImagePath = "//span[@class='text-left width-45per yor-in-thumbnail']//img"
    return ibcNumbers


def fetchIBCandYOR(driver):
    ibcNum_and_yor = []
    containerSelectorPath = "//div[@class='col-lg-12 search-result-container']"
    ibcNumSelectorPath = ".//span[starts-with(@id,'IBCNum')]"
    yorImagePath = ".//span[@class='text-left width-45per yor-in-thumbnail']//img"
    yorText = ".//span[@class='text-left width-45per yor-in-thumbnail']"
    containerSelectors = driver.find_elements_by_xpath(containerSelectorPath)

    for container in containerSelectors:
        ibcnum = container.find_element_by_xpath(ibcNumSelectorPath)
        yor = "None"
        try:
            yor = container.find_element_by_xpath(
                yorImagePath).get_attribute('src')
        except:
            yor = container.find_element_by_xpath(yorText).text
            # print(f"There is no YOR for ibcnum {ibcnum.text}")
        print([ibcnum.text, yor])
        ibcNum_and_yor.append([ibcnum.text, yor])

    return ibcNum_and_yor


def vehicleDetailPix():
    # 	vehicleDetailPath = "//div[starts-with(@id,'VehicleDetail)]"
    #		auctionDetail = 'div.search-result-panel auction-detail-panel'
    #	vehicleDetailsList = driver.find_elements_by_xpath(vehicleDetailPath)
    #	for every vehicleDetail => div.search-result-additional-panel additional-detail-panel
        #		auctionsheet = "//div[starts-with(@id,'aucSheetContainer')]"
    #		div.additional-image-container hide-in-mobile
    #		additionalPix = "//div[starts-with(@id,'imageFront')]"
    #		additionalPix = "//div[starts-with(@id,'imageBack-container')]"
    #		additionalPix = "//div[starts-with(@id,'interior-image-desk')]"
    #   //div[@id='VehicleDetail110220143']
    #   //div[starts-with(@id,'VehicleDetail')] --> container
    #   //img[starts-with(@id,'imageBack')]
    #   //img[starts-with(@id,'interior-image-desk')]
    #   //img[starts-with(@id,'auction-sheet-image')]

    #   March 8, 2019
    #   For additional info on vehicle:
    #   //div[starts-with(@id,'VehicleDetail')]//div[contains(@class,'additional-image-container hide-in-mobile')]
    #   //div[starts-with(@id,'VehicleDetail')]//div[contains(@class,'additional-image-container hide-in-mobile')]//img[@class='additional-image-size']
    #   //img[starts-with(@id,'imageFront')]
    #   if imagesize < 200 == image is not displayed.
    #
    #   For auction sheet:
    #  //img[starts-with(@id,'auction-sheet-image')]
    return


def yorImages():
    #   Japanese characters
    #   /[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff66-\uff9f]/
    # yorImagePath = "//span[@class='text-left width-45per yor-in-thumbnail']//img"
    return
