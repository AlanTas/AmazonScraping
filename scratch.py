# Importing packages

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.amazon.com.br/s?k=iPhone')

xpath = '//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[1]/div/span/div/div/div[4]/div/div/a/span[1]/span[2]/span[2]'
path =  '//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[2]/div/span/div/div/div[4]/div/div/a/span[1]/span[1]'

element = driver.find_element_by_xpath(xpath)
print(element.text)