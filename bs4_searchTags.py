from getImageSize import getImageFileSize
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

import re
import unicodedata


def bs4_search_elements(driver):
    '''
        Tries to search the DOM tree using BeautifulSoup
    '''
    # translates WebElement to BS4
    soup = BeautifulSoup(driver.page_source, 'lxml')
    # basicInfoPath = "//div[@class='col-lg-12 search-result-container']"
    # basic
    basic_soup = soup.find_all(
        'div', attrs={"class": "col-lg-12 search-result-container"})

    print(f"Basic Soup")
    # ibcNumPath = ".//span[starts-with(@id,'IBCNum')]"
    # yearMakeModelPath = ".//span[@class='text-bold pull-left width-55per']"
    # chassisPrefixPath = ".//a[@class='text-red pull-left width-70per chassis-amkenya chassis-wd']"
    # shuppinPath = ".//span[@id='shuppin']"
    # twoElementPath = ".//span[@class='pull-left width-55per']"
    # equipPath = ".//div[@class='pull-left width-55per']/span[1]"
    # yorImagePath = ".//span[@class='text-left width-45per yor-in-thumbnail']//img"
    # yorTextPath = ".//span[@class='text-left width-45per yor-in-thumbnail']"
    # mainImgPath = ".//img[@class='imgsize front-image-small']"
    for basic in basic_soup:
        # print(f"{basic}")
        main_img = basic.find(
            'img', attrs={'class', 'imgsize front-image-small'})
        print(main_img['src'])

        ibcnum = basic.find('span', id=re.compile('^IBCNum')).text.strip()
        print(ibcnum)

        shuppin = basic.find('span', attrs={'id': 'shuppin'}).text.strip()
        print(shuppin)

        yearMakeModel = basic.find(
            'span', attrs={'class': 'text-bold pull-left width-55per'}).text.strip()
        print(yearMakeModel)

        chassisPrefix = basic.find(
            'a', attrs={'class': 'text-red pull-left width-70per chassis-amkenya chassis-wd'}).text.strip()
        print(chassisPrefix)

        transColorFuel = basic.find(
            'span', attrs={'class': 'pull-left width-55per'}).text.strip()
        print(transColorFuel)

        equipment = basic.find(
            'div', attrs={'class': 'pull-left width-55per'}).find('span').text.strip()
        print(equipment)

        print()

    # advInfoPath = "//div[starts-with(@id,'VehicleDetail')]"
    # advanced
    adv_soup = soup.find_all('div', id=re.compile("^VehicleDetail"))

    print()
    print(f"Advanced Soup:")
    # auctionSheetPath = ".//a[starts-with(@id,'auction-sheet-image-container')]"
    # moreImages = ".//div[contains(@class,'additional-image-container hide-in-mobile')]//img"
    # more_details = {}
    # more_details["auc_sheet"] = containerPath.find_element_by_xpath(
    #     auctionSheetPath).get_attribute('href')  # for ahref
    # pictureLinks = containerPath.find_elements_by_xpath(moreImages)[1:-1]
    # more_details["more_images"] = [
    #     getImageFileSize(picture.get_attribute("src")) for picture in pictureLinks]
    count = 1
    for adv in adv_soup:
        print(f"Count #{count}")
        auction_sheet = adv.find('a', id=re.compile(
            '^auction-sheet-image-container'))
        print(auction_sheet['href'])

        moreImages = adv.find('div', attrs={
                              'class': 'additional-image-container hide-in-mobile'}).find_all('img')[1:-1]

        for img in moreImages:
            print(img['src'])
        # print(f"{adv}")
        print()
        count += 1


def destruct_basic(driver):
    '''
        Search the info from the basic div
    '''
    all_vehicles = []
    soup = BeautifulSoup(driver.page_source, 'lxml')
    basic_soup = soup.find_all(
        'div', attrs={"class": "col-lg-12 search-result-container"})
    for basic in basic_soup:
        vehicleInfo = {}

        main_img = basic.find(
            'img', attrs={'class', 'imgsize front-image-small'})

        ibcnum = basic.find('span', id=re.compile('^IBCNum')).text.strip()

        shuppin = basic.find('span', attrs={'id': 'shuppin'}).text.strip()

        yearMakeModel = basic.find(
            'span', attrs={'class': 'text-bold pull-left width-55per'}).text.strip()

        chassisPrefix = basic.find(
            'a', attrs={'class': 'text-red pull-left width-70per chassis-amkenya chassis-wd'}).text.strip()

        transColorFuel = basic.find(
            'span', attrs={'class': 'pull-left width-55per'}).text.strip()

        equipment = basic.find(
            'div', attrs={'class': 'pull-left width-55per'}).find('span').text.strip()

        vehicleInfo['main_img'] = main_img['src']
        # vehicleInfo['main_img'] = getImageFileSize(main_img['src'])
        vehicleInfo["ibcnum"] = ibcnum[-9:]
        vehicleInfo["shuppin"] = shuppin
        vehicleInfo["yearMakeModel"] = unicodedata.normalize(
            "NFKD", yearMakeModel)
        vehicleInfo["chassisPrefix"] = chassisPrefix.split()[-1]
        vehicleInfo["transColorFuel"] = transColorFuel
        vehicleInfo["equipment"] = equipment

        yorTextImage = basic.find(
            'span', attrs={'class': 'text-left width-45per yor-in-thumbnail'})

        try:
            yorTextImage = yorTextImage.find('img')['src']
            # yorTextImage = getImageFileSize(yorTextImage.find('img'))
            vehicleInfo["yorText"] = ""
            vehicleInfo["yorImage"] = yorTextImage

        except:
            yorTextImage = yorTextImage.text.strip().split()[-1]
            vehicleInfo["yorText"] = yorTextImage
            vehicleInfo["yorImage"] = -1

        all_vehicles.append(vehicleInfo)

    return all_vehicles


def destruct_adv(driver):
    '''
        Search the info from the basic div
    '''
    all_details = []
    soup = BeautifulSoup(driver.page_source, 'lxml')
    adv_soup = soup.find_all('div', id=re.compile("^VehicleDetail"))
    for adv in adv_soup:
        vehicleDetail = {}
        auction_sheet = adv.find('a', id=re.compile(
            '^auction-sheet-image-container'))

        moreImages = adv.find('div', attrs={
                              'class': 'additional-image-container hide-in-mobile'}).find_all('img')[1:-1]

        vehicleDetail["auc_sheet"] = auction_sheet['href']
        # print(vehicleDetail["auc_sheet"])
        # vehicleDetail["auc_sheet"] = getImageFileSize(auction_sheet['href'])
        vehicleDetail["more_images"] = [img['src'] for img in moreImages]
        # vehicleDetail["more_images"] = [
        #     getImageFileSize(img['src']) for img in moreImages]

        all_details.append(vehicleDetail)

    return all_details
