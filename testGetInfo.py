import requests

from bs4 import BeautifulSoup as sabaw
from selenium import webdriver
# driver = webdriver.Chrome(
#     executable_path=r"C:\Users\glabadia\Desktop\VS\selenium drivers\Chrome\chromedriver")
# # driver = webdriver.Firefox(executable_path=r"C:\Users\glabadia\Desktop\VS\selenium drivers\Firefox\geckodriver")

url = 'http://citwebdev033:1010/api/mcvehicle/vehicles?t=59511'
# driver.get(url)


# page = requests.get(url).text
# print(page)

dictionary = {x: 100 + x*2 for x in range(10)}

first = {"a": 10}
second = {"b": 12, "r": 9}
third = {**first, **second, "t": 33}
print(third)

sentence = "The quick brown fox jumped over the lazy dog."
another_tence = "This is a common interview question"


def most_char(input_text):
    char_count = {}
    for char in input_text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    most_used = {key: value for key, value in sorted(
        char_count.items(), key=lambda items: items[-1], reverse=True)}

    print("Most used char: ", *most_used.items())


most_char(sentence)
print()
most_char(another_tence)
