# Importing packages

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

driver = webdriver.Chrome('chromedriver.exe')
query = 'iPhone'
driver.get('https://www.amazon.com.br/s?k=' + query)

preffix = '//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div['
suffixName = ']/div/span/div/div/div[2]/h2/a/span'
suffixPriceWhole = ']/div/span/div/div/div[4]/div/div/a/span[1]/span[2]/span[2]'
suffixPriceWholeKindle = ']/div/span/div/div/div[3]/div/div/a/span[1]/span[2]/span[2]'
suffixPriceDec = ']/div/span/div/div/div[4]/div/div/a/span[1]/span[2]/span[3]'
suffixPriceDecKindle = ']/div/span/div/div/div[3]/div/div/a/span[1]/span[2]/span[3]'
suffixPriceMany = ']/div/span/div/div/div[4]/div/span[2]'

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

listaProdutos = []
listaPreços =[]
keep = True
current = 1

while(keep):

    xpathName = preffix + str(current) + suffixName
    xpathPriceWhole = preffix + str(current) + suffixPriceWhole
    xpathPriceWholeKindle = preffix + str(current) + suffixPriceWholeKindle
    xpathPriceDec = preffix + str(current) + suffixPriceDec
    xpathPriceDecKindle = preffix + str(current) + suffixPriceDecKindle
    xpathPriceMany = preffix + str(current) + suffixPriceMany

    if(check_exists_by_xpath(xpathName)):
        listaProdutos.append(driver.find_element_by_xpath(xpathName).text)

        priceTotal = "--"
        if(check_exists_by_xpath(xpathPriceWhole)):
            priceWhole = driver.find_element_by_xpath(xpathPriceWhole).text
            priceDec = driver.find_element_by_xpath(xpathPriceDec).text
            priceTotal = "R$" + priceWhole + "," + priceDec

        elif (check_exists_by_xpath(xpathPriceWholeKindle)):
            priceWhole = driver.find_element_by_xpath(xpathPriceWholeKindle).text
            priceDec = driver.find_element_by_xpath(xpathPriceDecKindle).text
            priceTotal = "R$" + priceWhole + "," + priceDec

        elif(check_exists_by_xpath(xpathPriceMany)):
            priceTotal = driver.find_element_by_xpath(xpathPriceMany).text

        listaPreços.append(priceTotal)

        current += 1
    else:
        keep = False


df = pd.DataFrame.from_dict({'Produto': listaProdutos, 'Preço': listaPreços})
df.to_excel('amazon.xlsx', header=True, index=False)

#
# for i in range(len(listaPreços)):
#     print(listaProdutos[i])
#     print(listaPreços[i])
#     print("_____________________")

'//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[11]/div/span/div/div/div[3]/div[2]/div/a/span/span[2]/span[2]'
'//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[4]/div/span/div/div/div[4]/div[2]/div/a/span/span[2]/span[2]'

