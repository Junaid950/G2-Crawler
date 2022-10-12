from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import sys
import os
url = "https://www.g2.com/"

#absolute driver path
chrome_driver_path = "C:\\Users\\dell\\Desktop\\chromedriver"

chrome_options = Options()
chrome_options.add_argument("--headless")
webdriver = webdriver.Chrome(executable_path=chrome_driver_path,options=chrome_options)
search_query = 'Asana'
if (len(sys.argv)>=2):
    search_query = sys.argv[1]
    print(search_query)
with webdriver as driver:
    #timeout
    wait = WebDriverWait(driver,10)
    #retrive the data 
    driver.get(url)
    #for search box
    search = driver.find_element_by_id("hmSearch")
    search.send_keys(search_query+Keys.RETURN)
    #wait for
    wait.until(presence_of_element_located(By.ID ,'quoteslist'))
    results = driver.find_elements_by_class_name("m-brick")
    for quotes in results:
        quoteArr = quotes.text
        print(quoteArr)
        print()

    print(results)
    driver.close()

    

