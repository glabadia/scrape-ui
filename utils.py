from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from getImageSize import getImageFileSize, isAucSheetIncomplete, isNoFoto, noMainImg, isNoFotoHref, imgProcessedBlank, imgProcessed_moreImg
from jpChecker import find_japanese_char as catchJap

SLEEP_TIME: int = 10

errorList = {"main_img": 2151, "yearMakeModel": "unknown", "chassisPrefix": "unknown",
             "transColorFuel": "| --", "equipment": "| --"}  # 6385 #2151 for no foto  "auc_sheet": 2151, "more_images": 2151 #NZE151-1076863

# 3386 -> image not available
moreErrorList = {"auc_sheet": 228, "more_images": 2151}
# moreErrorList = {"more_images": 2151}
errorReturnValue = {"main_img": "no main image", "jap_char": "japanese characters", "yearMakeModel": "unknown year/make/model", "chassisPrefix": "unknown chassis prefix",
                    "transColorFuel": "no transmission/color/fuel type", "equipment": "no equipment", "nofoto": "Image show no foto", "auc_sheet": "no auction sheet", "more_images": "additional photos show 'no foto'"}
errorCounter = {"jap_char": [], "yearMakeModel": [], "chassisPrefix": [],
                "transColorFuel": [], "equipment": [], "yorText": [], "yorImage": [], "more_images": [], "auc_sheet": []}


def error_init():
    return {"main_img": [], "jap_char": [], "yearMakeModel": [], "chassisPrefix": [],
            "transColorFuel": [], "equipment": [], "more_images": [], "auc_sheet": []}


def printList(list):
    count = 1
    for item in list:
        print("Element: ", count, ":")
        print(item.text, "class name = ", item.get_attribute("class"))
        print("--------------------------------------------------------------------------------------")
        count += 1


def printDict(dict):
    count = 1
    for item in dict:
        print("Element: ", count, ":")
        print(item)
        print("--------------------------------------------------------------------------------------")
        count += 1


def destructure(vehicles, ibcNums):
    # make a list of dictionaries
    ibcVehicles = []

    for ibcNum in ibcNums:
        ibcNumDict = {}
        ibcNumDict["atnznum"] = ibcNum.text
        ibcVehicles.append(ibcNumDict)

    for i in range(len(vehicles)):
        print(vehicles[i])
        vehicle = vehicles[i].text.splitlines()
        ibcVehicles[i]["yearMakeModel"] = vehicle[0]
        ibcVehicles[i]["chassisPrefix"] = vehicle[1].split()[-1]
        ibcVehicles[i]["transColorFuel"] = vehicle[2]
        ibcVehicles[i]["equipment"] = vehicle[6]
        ibcVehicles[i]["yor"] = vehicle[9]

    return ibcVehicles

# exec(open(r"C:\Users\glabadia\Desktop\VS\scripts\dataCollectionFiles\init.py").read())


def getAuctionHouse(dc_driver):
    auctionHousePath = "//span[starts-with(@id,'ATNZNum')]"
    try:
        auctionHouseContainer = WebDriverWait(dc_driver, SLEEP_TIME).until(
            EC.presence_of_element_located((By.XPATH, auctionHousePath))).text[:-10]
    except Exception as e:
        auctionHouseContainer = f"Dummy Auction house{e}"
    # auctionHouseContainer = dc_driver.find_element_by_xpath(auctionHousePath)
    return auctionHouseContainer


def destruct_info_upd(containerPath):
    atnzNumPath = ".//span[starts-with(@id,'ATNZNum')]"
    yearMakeModelPath = ".//span[@class='text-bold pull-left width-100per']"
    chassisPrefixPath = ".//a[@class='text-primary pull-left width-70per chassis-amkenya chassis-wd']"

    transColorFuelPath = ".//div[@class='data-container']/dl/dd[2]/span[1]"

    shuppinPath = ".//span[@id='shuppin']"

    equipPath = ".//div[@class='data-container']/dl/dd[3]/span[1]"

    mainImgPath = ".//img[@class='imgsize front-image-small']"

    vehicleInfo = {}

    vehicleInfo["main_img"] = containerPath.find_element_by_xpath(
        mainImgPath).get_attribute('src')
    # vehicleInfo["main_img"] = getImageFileSize(containerPath.find_element_by_xpath(
    #     mainImgPath).get_attribute('src'))
    vehicleInfo["atnznum"] = containerPath.find_element_by_xpath(
        atnzNumPath).text[-9:]
    vehicleInfo["shuppin"] = containerPath.find_element_by_xpath(
        shuppinPath).text
    vehicleInfo["yearMakeModel"] = containerPath.find_element_by_xpath(
        yearMakeModelPath).text
    vehicleInfo["chassisPrefix"] = containerPath.find_element_by_xpath(
        chassisPrefixPath).text.split()[-1]
    vehicleInfo["transColorFuel"] = containerPath.find_elements_by_xpath(
        transColorFuelPath).text
    vehicleInfo["equipment"] = containerPath.find_element_by_xpath(
        equipPath).text

    # yorTextImage = "None"

    # try:
    #     yorTextImage = containerPath.find_element_by_xpath(
    #         yorImagePath).get_attribute('src')
    #     # yorTextImage = getImageFileSize(containerPath.find_element_by_xpath(
    #     #     yorImagePath).get_attribute('src'))
    #     vehicleInfo["yorText"] = ""
    #     vehicleInfo["yorImage"] = yorTextImage

    # except:
    #     yorTextImage = containerPath.find_element_by_xpath(yorTextPath).text
    #     vehicleInfo["yorText"] = yorTextImage.split()[-1]
    #     vehicleInfo["yorImage"] = -1

    return vehicleInfo


def deconstruct_details(containerPath):

    auctionSheetPath = ".//a[starts-with(@id,'auction-sheet-image-container')]"
    moreImages = ".//div[contains(@class,'additional-image-container hide-in-mobile')]//img"
    more_details = {}

    more_details["auc_sheet"] = containerPath.find_element_by_xpath(
        auctionSheetPath).get_attribute('href')  # for ahref
    # more_details["auc_sheet"] = getImageFileSize(containerPath.find_element_by_xpath(
    #     auctionSheetPath).get_attribute('href'))  # for ahref
    # get only the 2nd element, but do not include the last element
    # March 19, 2019: Get only the inner elements, not the outer ones
    pictureLinks = containerPath.find_elements_by_xpath(moreImages)[1:-1]
    # more_details["more_images"] = [
    #     picture.get_attribute("src") for picture in pictureLinks]
    more_details["more_images"] = [
        getImageFileSize(picture.get_attribute("src")) for picture in pictureLinks]

    return more_details


def traverseKeys():
    return None


def dataVerification(vehicles, speed, lookout=errorList, moreLookOut=moreErrorList, reportLog=errorReturnValue):
    # if parameter=standard->proceed with search verification
    atnznumKey = "atnznum"
    shuppinKey = "shuppin"
    japanese = "jap_char"
    errorCount = error_init()
    for vehicle in vehicles:
        basic, advance = vehicle
        for key in lookout:
            # for key in basic:
            if speed == "slow":
                if key == 'main_img':
                    # fast search
                    main_img_size = getImageFileSize(basic[key])
                    # if lookout[key] == main_img_size or 4484 == main_img_size:
                    if lookout[key] == main_img_size or noMainImg(main_img_size) or imgProcessed_moreImg(main_img_size):
                        # if lookout[key] == basic[key]:  # standard search
                        errorCount[key].append(
                            (basic[atnznumKey], basic[shuppinKey]))
            if key == 'yearMakeModel':
                if catchJap(basic[key]):
                    errorCount[japanese].append(
                        (basic[atnznumKey], basic[shuppinKey]))
            if key != 'main_img':
                # print(f"Key is {key}")
                if lookout[key].lower() in basic[key].lower():
                    errorCount[key].append(
                        (basic[atnznumKey], basic[shuppinKey]))
        if speed == "slow":
            for key in moreLookOut:
                if key == 'more_images':
                    imagesList = [getImageFileSize(img)
                                  for img in advance[key]]
                    # imagesList = advance[key]
                    for image in imagesList:
                        if isNoFoto(image) or noMainImg(image) or imgProcessed_moreImg(image):
                            errorCount[key].append(
                                (basic[atnznumKey], basic[shuppinKey]))
                            break
                if key == 'auc_sheet':
                    auc_sheet_img = getImageFileSize(advance[key])
                    if isAucSheetIncomplete(auc_sheet_img) or isNoFotoHref(auc_sheet_img) or imgProcessedBlank(auc_sheet_img):
                        errorCount[key].append(
                            (basic[atnznumKey], basic[shuppinKey]))
                    break
    return errorCount


def dictErrors(error_list):
    displayOutput = {}

    for key in error_list:  # error_list.items() => returns a tuple, not a key, even if you have a "for key in error_list.items()"
        if len(error_list[key]) == 0:
            displayOutput[errorReturnValue[key]] = "No issues"
        else:
            displayOutput[errorReturnValue[key]] = error_list[key]

    return displayOutput


def dictErrors_shuppin(error_list):
    displayOutput = {}

    for key in error_list:  # error_list.items() => returns a tuple, not a key, even if you have a "for key in error_list.items()"
        if len(error_list[key]) == 0:
            displayOutput[errorReturnValue[key]] = "No issues"
        else:
            displayOutput[errorReturnValue[key]] = error_list[key]

    return displayOutput


def printErrors(error_list):
    for key in error_list:
        print(key.title())
        # print(error_list[key])
        value = error_list[key]
        if type(value) is list:
            for content in value:
                print(f"{content},")
        else:
            print(value)
        print("-------------------------------------------------------------------------------")


def getAuctionHouseTest(text=""):
    text = "Honda Tokyo-110175756"
    print(text[:-10])


def getTimeStamp():
    from datetime import datetime as dt
    return dt.now().strftime("%A, %d. %B %Y %I:%M%p")


def tuple_to_list(listOfTuples):
    iL, sL = [], []
    for item in listOfTuples:
        ibc, shuppin = item
        iL.append(ibc)
        sL.append(shuppin)

    return iL, sL


def printToFile(duration, fileName="testFile", contentList=""):
    # import os
    # os.chdir(workingDirectory)
    dc_time, check_time = duration
    with open(f"{fileName}.txt", "w") as writer:
        writer.write(
            "#############################################################\n")
        writer.write(f"{fileName} Errors: \n")
        writer.write("\n")
        # writer.write(f"Data Collection lasted for {convert_time(duration):.1f} seconds.\n")
        writer.write(
            f"Data Collection lasted for {convert_time(dc_time)} seconds.\n")
        writer.write(
            f"Error checking completed within {convert_time(check_time)} seconds.\n")
        writer.write(f"Finished checking on {getTimeStamp()} \n")
        writer.write(
            "#############################################################\n\n")
        for content in contentList:
            writer.write(f"{content.title()}:\n")
            value = contentList[content]
            # print(f"Value: {value}")
            if type(value) is list:
                for entry in value:
                    # writer.write(f"{entry[-9:]},\n")
                    writer.write(f"{entry},\n")
            else:
                # writer.write(f"{value[-9:]}\n")
                writer.write(f"{value}\n")
            writer.write(
                "-------------------------------------------------------------\n")


def printToFile_shuppin(duration, fileName="testFile", contentList=""):
    dc_time, check_time = duration
    with open(f"{fileName}.txt", "w") as writer:
        writer.write(
            "#############################################################\n")
        writer.write(f"{fileName} Errors: \n")
        writer.write("\n")
        writer.write(
            f"Data Collection lasted for {convert_time(dc_time)} seconds.\n")
        writer.write(
            f"Error checking completed within {convert_time(check_time)} seconds.\n")
        writer.write(f"Finished checking on {getTimeStamp()} \n")
        writer.write(
            "#############################################################\n\n")
        for content in contentList:
            writer.write(f"{content.title()}:\n")
            value = contentList[content]
            if type(value) is list:
                atnznum, shuppin = tuple_to_list(value)
                for entry in atnznum:
                    writer.write(f"{entry}, ")
                writer.write("\n\n")
                writer.write("Shuppin: \n")
                writer.write("\n")
                for entry in shuppin:
                    writer.write(f"{entry}, ")
                writer.write("\n")

            else:
                writer.write(f"{value}\n")
            writer.write(
                "-------------------------------------------------------------\n")


def createDirectory():
    """
    create directory for data collection
        if directory already exists, return false
        else, create directory in strftime('%Y_%b_%d') format
        or create nesting directory : year/Month/day, e.g. 2019/March/5
    """
    import os
    from datetime import datetime as dt

    timeStampList = ["%Y", "%B", "%d"]
    for time in timeStampList:
        current_directory = os.getcwd()
        newFolder = dt.now().strftime(time)
        newDirectory = os.path.join(current_directory, newFolder)
        if not os.path.exists(newDirectory):
            os.makedirs(newDirectory)
        else:
            print(f"Folder '{newDirectory}' already exists!")
        try:
            # Change the current working Directory
            os.chdir(newFolder)
            # print("Directory changed")
        except OSError:
            print("Can't change the Current Working Directory")

    return os.getcwd()


def convert_time(time_sec):
    NUM_SECONDS = 60
    return_val = ""
    raw_time = time_sec // NUM_SECONDS
    remain_time = time_sec % NUM_SECONDS
    if raw_time > 0:
        return_val += f"{int(raw_time)} "
        if raw_time == 1:
            return_val += "minute "
        else:
            return_val += "minutes "
        return f"{return_val}and {remain_time:.1f}"
    return f"{remain_time:.1f}"


def convert_to_text(web_element):
    return [element.text for element in web_element]


def sorted_auctionHouses(raw_dict):
    # for key, value in sorted(ah_units.items(), key=lambda items: items[-1]):
    #     sorted_ah[key] = value
    # , reverse=True
    return {key: value for key, value in sorted(raw_dict.items(), key=lambda items: items[-1])}


def trimm_list(input_list, element_to_trim):
    newlist = []
    for item in input_list:
        endpoint_index = item.index(element_to_trim)
        newlist.append(item[:endpoint_index].strip())
    return newlist


def trimm_list_v2(input_list, left, right):
    newlist = []
    for item in input_list:
        left_index = item.index(left)
        right_index = item.find(right)
        newlist.append(int(item[left_index+1:right_index].strip()))
    return newlist


def ah_table(key_list, value_list):
    hash_table = {}
    for k, v in zip(key_list, value_list):
        hash_table[k] = v
    return hash_table


def fancy_print(value):
    import math
    num = value
    sqrt = math.sqrt(num)
    sqrt_flr, sqrt_cel = math.floor(sqrt), math.ceil(sqrt)
    side = sqrt_flr if abs(
        sqrt_flr**2 - num) < abs(sqrt_cel**2 - num) else sqrt_cel
    return side
