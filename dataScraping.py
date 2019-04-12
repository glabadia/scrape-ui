from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from results import expandVehicleInfoIdirect, retrieveInfoUpd
from utils import errorCheckUpd, printDict
from traversePage import nextResults
from time import time, sleep
import asyncio


def getAllInfo(driver):
    # expandVehicleInfoIdirect(driver)

    # start = time()
    # infoList = retrieveInfoUpd(driver)
    # end = time()

    # printDict(infoList)
    # print(f"Finished in {end-start} seconds.")

    # start = time()
    # checkErrorList = errorCheckUpd(infoList)

    # print(checkErrorList[1])

    nextResults(driver)
    # print(f"There are {getErrorCount(checkErrorList[1])} errors found.")
    # end = time()
    # print(f"Finished in {end-start} seconds.")


def getErrorCount(errorDict):
    errorCount = 0
    for key, value in errorDict.items():
        errorCount += len(value)
    return errorCount
