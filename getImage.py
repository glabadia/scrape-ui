from time import sleep
import requests
from bs4 import BeautifulSoup as Soup

# url='https://en.wikipedia.org/wiki/Agent_Orange'
# url = 'http://img2.jcarinfo.net/gix.php?&op=ifPqIaIKIagKIltNg5IqcltAYXIsYFSKhOGuLuTuIa3UIaPtIuTwIa3X7bVJCfdNhFVXLRXUM5SqMRYqAS.AV8tO2YtQV8tQ46XsMOGuhK&time=201902131250&inya=true'
# url = 'http://img1.jcarinfo.net/gix.php?&op=ifPqIaIKIagKIltNg5IqcltAYXIs8FGl48TuIa3UIaPtIuTXIaYw7bVJCfdNhFVXLRXUM5SqMRYqAS.AV8tO2YtQV8tch3XsMOGuCRUB&time=201902131520&inya=true'


# html = Soup(requests.get(url).text, features="lxml")
# html = requests.get(url, stream=True)
# html = requests.get(url)
# data = html.text
# print(f"Image size: {len(data)} bytes")

# image_links = [(url + a['href'])
#                for a in html.find_all('a', {'class': 'image'})]

# for img_url in image_links:
#     response = requests.get(img_url)
#     try:
#         print(
#             f"Size of image {img_url} = {response.headers['Content-Length']} bytes")
#     except KeyError:
#         print(f"Server didn't specify content length in headers for {img_url}")
#     sleep(0.5)


urlList = [
    "http://138.201.52.234/imgs/dyJ2O5ZnVGaLpjCgSr4JtiXYvulKsUtDrHbHJEvczM",
    "http://138.201.52.236/imgs/dyJ2O5ZnVGaLpjCgSr4JtiXYvulKsUtEeQNQigrh7z",
    "http://138.201.52.234/imgs/dyJ2O5ZGYxX3QVFVucXdYkUoGQvH3jVfVM7DukZlTg",
    "http://img1.jcarinfo.net/gixlarge.php?&op=CRKqIaIKIagKIltNg5IqcltcAYS076UHh53sImetWQe*Ia1sIQeUIut6COn*Cfd1MRXDif4HLbAn7SV8AYYqV1SIY6Yq8B0dLvVsh5nr4K&time=201903082320",
    "http://img3.jcarinfo.net/gix.php?&amp;op=4BIqIaIKIagKIltNg5IqcltcAYS076UHh53sImetWQe*Ia1sIQeXI8t6COn*Cfd1MRXDif4HLbAn7SV8AYYqV1SIY6Yq8B0dLvVsh5nr4K&amp;time=201903082340",
    "http://img1.jcarinfo.net/gix.php?&op=ifPqIaIKIagKIltNg5Iqclta2Y3s25SU7*PKIQ1KI*3*7*kKIaY*7bVJCfdNhFVXLRXUM5SqMRYqAS.AV8tO2YtQV8tch3XsMOGuCRUB&time=201903131640&inya=true",
    "http://img1.jcarinfo.net/gix.php?&op=hvIqIaIKIagKIltNg5Iqclta2Y3s25SU7*PKIQ1KI*3*7*kKIaY*7bVJCfdNhFVXLRXUM5SqMRYqAS.AV8tO2YtQV8tch3XsMOGuCRUB&time=201903131640",
    "http://138.201.52.234/imgs/9I3PnMMQPlsKJY7SMtAJoQUpPupIhJUjEujYykXmoxWDoAi-ETxGBvgdwmvSwT-7",
    "http://img1.jcarinfo.net/gix.php?&op=ifPqIaIKIagKIltNg5IqcltcAYS076n*COnpgfMH7*PKIQ1KI*3*7*3KIQeqMOHNhFn*4bADLfnFgRtX48tYYnAS7340QSdS7S0uL6NHhOSr&time=20190313170&inya=true"
]
# url = "http://138.201.52.234/imgs/dyJ2O5ZnVGaLpjCgSr4JtiXYvulKsUtDrHbHJEvczM"
# url = "http://138.201.52.236/imgs/dyJ2O5ZnVGaLpjCgSr4JtiXYvulKsUtEeQNQigrh7z"
# url = "http://138.201.52.234/imgs/dyJ2O5ZGYxX3QVFVucXdYkUoGQvH3jVfVM7DukZlTg"


def getImageFileSize(link):
    import requests
    imgLink = requests.get(link).text
    return len(imgLink)


# for url in urlList:
#     print(getImageFileSize(url))

#  urls = ['http://img1.jcarinfo.net/gixlarge.php?&altUrl=http://88.99.218.95/imgs/aKxY8utwMCwJGK2s2DLsoigf5jwE11l38dHec1SG1ThdkLpqrrNj',
#         "http://img2.jcarinfo.net/gixlarge.php?&altUrl=http://88.99.218.95/imgs/aKxY8utwMCwJGK2s2DLsoigf5jwE11l3NbMwtDKF04O5WTWRjnf4",
#         "http://img3.jcarinfo.net/gixlarge.php?&altUrl=http://88.99.218.95/imgs/aKxY8utwMCwJGK2s2DLsoigf5jwE11l21gQf0CSyAbolIVEqz007",
#         "http://img0.jcarinfo.net/gixlarge.php?&altUrl=http://88.99.218.95/imgs/aKxY8utwMCwJGK2s2DLsoigf5jwE11l2Pew7maNfOx6aiQ5piNnq",
#         'http://img1.jcarinfo.net/gixlarge.php?&altUrl=http://88.99.218.95/imgs/aKxY8utwMCwJGK2s2DLsoigf5jwE11l4na9M0jVvxMkjWqLz6WBp',
#         "http://img2.jcarinfo.net/gixlarge.php?&op=hFKqIaIKIagKIltNg5IqcltPLFU1g8GPLFDpgRn1LuTuIa3UIaItWZT*IaeFIut6COn*Cfd1MRXDif4HLbAn7SV8AYYqAS.AV8tch3XsMOGuCRUB&time=201903181740",
#         "http://img3.jcarinfo.net/gixlarge.php?&op=hFKqIaIKIagKIltNg5IqcltPLFU1g8GPLFDpgRn1LuTuIa3UIaItWZT*IaevIlt6COn*Cfd1MRXDif4HLbAn7SV8AYYqAS.AV8tch3XsMOGuCRUB&time=201903181740",
#         "http://img0.jcarinfo.net/gixlarge.php?&altUrl=http://88.99.218.95/imgs/aKxY8utwMCwJGK2s2DLsoigf5jwE11l5G7rQpBjUrohl960YfHbs"]

urls = ['http://idirect.ibcjapan.co.jp/images/idirect_nf_small.gif',
        'http://idirect.ibcjapan.co.jp/images/idirect_nf_large.gif',
        'http://img1.jcarinfo.net/gixlarge.php?&op=45KqIaIKIagKIltNg5IqcltPVA.97XdHCfVHLR3sImetWQe6IaIsImPFdlt6COn*Cfd1MRXDif4HLbAn7SV8AYYqAS.AV8tch3XsMOGuCRUB&time=201904021840']


# def getReq(link):
#     resp = requests.head(link)
#     return len(resp.text)


for url in urls:
    # auctionsheet out of focus: 228
    print(getImageFileSize(url))

# for url in urls:
#     print(getReq(url))


def sample_function(x=433):
    # if 900 > x > 15:
    #     print("true")
    # else:
    #     print("false")
    return 900 > x > 15


# print(sample_function())


def tuple_to_list():
    lot = [('110531366', '10287'), ('110534139', '75023'), ('110532618', '50564'), ('110531299', '10220'), ('110531112', '10025'), ('110532586', '50535'), ('110531651', '18155'), ('110531227', '10143'), ('110534219', '85056'), ('110539467', '75041'), ('110531288', '10209'), ('110534140', '75024'), ('110534129', '75013'), ('110531543', '18048'), ('110531717', '18220'), ('110542900', '75043'), ('110532621', '50567'), ('110532581', '50530'), ('110531714', '18217'), ('110534119', '75003'), ('110539477', '85080'), ('110534146', '75030'), ('110531377', '10298'), ('110531384', '10304'), ('110531647', '18151'), ('110532608', '50555'), ('110531632', '18136'), ('110534126', '75010'), ('110539161', '10335'), ('110531361', '10282'), ('110531135', '10048'), ('110531641', '18145'), ('110534131', '75015'), ('110531645', '18149'), ('110531539', '18044'), ('110539169', '10345'), ('110531933', '30002'), ('110534117', '75001'), ('110531265', '10185'), ('110531939', '30009'), ('110531289', '10210'), ('110531353', '10274'), ('110538834', '10137'), ('110531226', '10142'), ('110531225', '10141'), ('110531541', '18046'), ('110534118', '75002'), ('110539188', '10368'), ('110532654', '5082'), ('110534142', '75026'), ('110556625', '75047'), ('110532658',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   '5087'), ('110556631', '75054'), ('110532615', '50561'), ('110534124', '75008'), ('110532604', '50551'), ('110532610', '50557'), ('110534148', '75032'), ('110531566', '18071'), ('110556296', '30073'), ('110556315', '5144'), ('110532585', '50534'), ('110556627', '75049'), ('110539468', '75042'), ('110531220', '10135'), ('110534132', '75016'), ('110532617', '50563'), ('110532601', '50549'), ('110532579', '50529'), ('110534145', '75029'), ('110534128', '75012'), ('110531222', '10138'), ('110531110', '10023'), ('110531143', '10056'), ('110532587', '50536'), ('110531404', '10324'), ('110531812', '18314'), ('110534136', '75020'), ('110556628', '75050'), ('110532611', '50558'), ('110534130', '75014'), ('110534143', '75027'), ('110534152', '75036'), ('110556221', '18404'), ('110534127', '75011'), ('110556623', '75045'), ('110556632', '75055'), ('110534155', '75039'), ('110539263', '5138'), ('110531829', '18331'), ('110556626', '75048'), ('110531229', '10145'), ('110556232', '18415'), ('110533986', '70768'), ('110531113', '10026'), ('110531653', '18157'), ('110531805', '18307'), ('110531688', '18192'), ('110534135', '75019'), ('110539176', '10354'), ('110533664', '70446'), ('110531736', '18239'), ('110539200', '10383')]

    iL, sL = [], []
    for item in lot:
        ibc, shuppin = item
        iL.append(ibc)
        sL.append(shuppin)

    return iL, sL


def print_square(num):
    import math
    # num = 21
    sqrt = math.sqrt(num)
    sqrt_flr, sqrt_cel = math.floor(sqrt), math.ceil(sqrt)
    side = sqrt_flr if abs(
        sqrt_flr**2 - num) < abs(sqrt_cel**2 - num) else sqrt_cel

    return side


def writeToFile(stream):
    length = print_square(len(stream))
    with open("even_print.txt", "w") as writer:
        for element in stream:
            content = ""
            for i in range(length):
                content += f"{element}, "
            writer.write(content)


# val = tuple_to_list()[0]
# val = ["54", "23", "23", "23", "23", "23", "23", "23", "23",
#        "23", "23", "23", "23", "23", "23", "23", "23", "23"]
# print(tuple_to_list()[-1])

# writeToFile(val)


def testFetch():
    from urllib.request import urlopen
    req = urlopen("http://idirect.ibcjapan.co.jp/Images/ibcjapan-web-logo.png")
    metadata = req.getheader('Content-Length')
    try:
        stream = int(metadata)
    except:
        stream = -1
    print(f"Data is: {stream}")


testFetch()
