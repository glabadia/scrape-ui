from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from time import sleep, time
from utils import errorCheckUpd, printErrors, dictErrors, getAuctionHouse, printToFile, createDirectory, convert_time, createDirectory, errorCheck_ibc_shuppin, dictErrors_shuppin, printToFile_shuppin, errorCheckMoreInfo, dataVerification
from results import expandVehicleInfoIdirect, retrieveInfoTest, retrieveInfoUpd, retrieveInfoDetail, retrieveAllInfo

from errorCheck import hasNoResults

import asyncio
WAIT_TIME: int = 5  # 10
SLEEP_TIME: int = 3  # 5


def nextResults(webdriver):
    '''
    #1  Get current page number
    #2  Get Next page number reference
    '''
    import os
    getActiveLink = "//ul[@class='pagination margin-top-bottom-none']//li[@class='active']"
    getNextLink = "/following-sibling::li[1]//a"

    infoList = []
    retrievedInfo = None
    # addInfoList = []

    startDC = time()
    isEnd = False
    # createDirectory()

    auctionHouseName = ""

    while not isEnd:
        print("Incur python to sleep..")

        sleep(SLEEP_TIME)

        expandVehicleInfoIdirect(webdriver)

        results = hasNoResults(webdriver)

        if not auctionHouseName:
            auctionHouseName = getAuctionHouse(webdriver)

        if time() - startDC >= 300:
            print("DC reached 3 minute limit")
            back_to_search(webdriver)
            break

        if results:
            print("No results displayed..")
            print(f"Data collection for [{auctionHouseName}]: incomplete")
            back_to_search(webdriver)
            isEnd = True
            break

        startRetrieve = time()
        # infoList.extend(retrieveInfoUpd(webdriver))
        retrievedInfo = retrieveAllInfo(webdriver)
        infoList.extend(retrievedInfo)
        # print(retrievedInfo) #comment
        # addInfoList.extend(retrieveInfoDetail(webdriver))
        endRetrieve = time()

        activePage = WebDriverWait(webdriver, WAIT_TIME).until(
            EC.presence_of_element_located((By.XPATH, getActiveLink)))
        nextPage = WebDriverWait(webdriver, WAIT_TIME).until(
            EC.presence_of_element_located((By.XPATH, f"{getActiveLink}/{getNextLink}")))

        print(f"Checking [Page {activePage.text}]..")

        if nextPage.text == "»":
            isEnd = True
            print("Traverse reached last page..")
            print(f"Data collection of [{auctionHouseName}]: completed")
            print()
        else:
            print(
                f"Finished checking [{auctionHouseName}, Page {activePage.text}] in {(endRetrieve-startRetrieve):.1f} seconds.")
            print()
            print(f"Next is [Page {nextPage.text}]..")
            try:
                nextPage.click()
            except Exception as e:
                print(f"Error: {e}")
                print(f"No Next page..")
                back_to_search(webdriver)
                break
    else:
        print("Traverse has been stopped..")
        back_to_search(webdriver)
        print()

    endDC = time()

    timeDC = endDC-startDC
    print(f"Finished collecting data in {convert_time(timeDC)} seconds.")

    print(f"Will now check for errors..")
    print()
    startEC = time()
    # checkErrorList = errorCheckUpd(infoList)
    # checkErrorList = errorCheck_ibc_shuppin(infoList)
    # checkErrorList = errorCheckMoreInfo(infoList, addInfoList)
    checkErrorList = dataVerification(infoList)

    # populate_errors = dictErrors(checkErrorList[1])
    populate_errors = dictErrors_shuppin(checkErrorList)
    # print(populate_errors)
    print("----------------------------------------------------------")
    printErrors(populate_errors)
    endEC = time()
    timeEC = endEC - startEC
    # printToFile((timeDC, timeEC),
    #             auctionHouseName, populate_errors)
    printToFile_shuppin((timeDC, timeEC),
                        auctionHouseName, populate_errors)

    print(f"Error checking done in {convert_time(timeEC)} seconds.")


def back_to_search(webdriver):
    backToSearchPath = "//button[@class='btn btn-default margin-left-15px back-to-search']"
    backToSearchButton = WebDriverWait(webdriver, WAIT_TIME).until(
        EC.presence_of_element_located((By.XPATH, backToSearchPath)))
    for i in range(4, 0, -1):
        sleep(1)
        print(f"Returning in {i}..")
        i -= 1
    backToSearchButton.click()

    # check if //div[@id='loader'][contains(@style,'display: block;')] wait until display: none
    #   loader style --> display: block; top: 0px; bottom: 0px; left: 0px; right: 0px; position: fixed; background-color: rgba(255, 255, 255, 0.7); overflow: hidden; outline: none 0px; z-index: 999; text-align: center; margin-left: -15px; margin-right: -15px;
