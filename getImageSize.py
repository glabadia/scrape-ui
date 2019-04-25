import requests
from time import sleep

#   Unknown YOR List:
#   6385 bytes = image not available
#   2151 bytes = no foto
#   900 > x > 15 = YOR not clear

#   make a function that traverses through a number of operations, e.g.
#   if imageFileSize = 6385, then set as 'YOR image not available status', and break, else
#   if imageFileSize 900 > x > 15 = YOR not clear, then set as 'YOR image not clear/visible', and break, else
#   return -1


def getImageFileSize(link):
    # imgLink = requests.get(link).text
    # print(len(imgLink))
    # return len(imgLink)
    # sleep(.7)
    # sleep(.2)
    # return -1 if link == -1 or link == '/images/atnzauctions_nf_large.gif' or link == '/images/atnzauctions_nf_small.gif' else len(requests.get(link).text)
    # print(f"Image size: {len()/1024} bytes")
    return (
        -1 if link == -1 else
        len(requests.get("http://auctions.autoterminal.co.nz"+link).text) if (link ==
                                                                              '/images/atnzauctions_nf_large.gif' or link == '/images/atnzauctions_nf_small.gif') else len(requests.get(link).text)
    )


def isYorNotCLear(imageSize):
    return 1000 > imageSize > 15


def isInvalidRequest(imageSize):
    return 15 >= imageSize > 0


def isAucSheetIncomplete(aucSheet):
    # return 230 >= aucSheet >= 227 or aucSheet == 301
    return 230 >= aucSheet > 227 or aucSheet == 301


def isAucSheetNoFoto(aucSheet):
    return 219 >= aucSheet >= 217


def isAucSheetNoFotoHref(aucSheet):
    # ref: http://auctionimages.autoterminal.co.nz/gixlarge_atnz.php?&op=hFKqIaIKIagKIlt0A3UC7ZJq2YS08YAr4uGZgfn*CRVn7*PKIQ1KdaPF7*YFIQeqMOHNhFn*4bADLfnFgRtX48tYYnAS7SV8AYYq8B0dLvVsh5nr4K&time=201904251840
    return 193 == aucSheet


def isNoFoto(foto):
    return 2151 == foto


def isNoFotoHref(foto):
    return 223 == foto


def noMainImg(foto):
    return 4484 == foto


def imgProcessed_moreImg(foto):
    return 4457 == foto


def imgProcessed(foto):
    return 33573 == foto


def imgProcessedBlank(foto):
    return 152 == foto


def isImageNotAvailable(foto):
    # http://auctions.autoterminal.co.nz/images/atnzauctions_nf_large.gif
    # http://auctions.autoterminal.co.nz/images/atnzauctions_nf_small.gif
    # in atnz, choose src, not href
    return foto == 151


# link = "http://img1.jcarinfo.net/gix.php?&op=ifPqIaIKIagKIltNg5IqcltcAY4XCvAsCF3sVnd0AZTuIa3UIaPtd8T6dut6COn*Cfd1MRXDif4HLbAn7SV8AYYqAS.AV8tch3XsMOGuCRUB&time=201902151020&inya=true"
# print(getImageFileSize(link))
