# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 21:35:03 2021

@author: JINSEOK LEE
"""



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

search_INPUT = 'Apple'
filename_INPUT = search_INPUT+'.txt'

options = webdriver.ChromeOptions()
options.add_argument('window-size=1080,780')

driver = webdriver.Chrome('chromedriver',options=options)
driver.implicitly_wait(5)

driver.get(url='https://finance.yahoo.com/')
print('connected to the URL')

search_box = driver.find_element_by_xpath('//*[@id="yfin-usr-qry"]')

search_box.send_keys(search_INPUT)
search_box.send_keys(Keys.RETURN)
print('Searching...')

historicalData = driver.find_element_by_css_selector('#quote-nav > ul > li:nth-child(5)')
historicalData.click()
driver.implicitly_wait(3)
print('Clicked the Historical Data')

## Set the time period
timePeriod = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/div[1]/div/div/div')
timePeriod.click()
print('Clicked the Time Period')


timeSetMax = driver.find_element_by_xpath('//*[@id="dropdown-menu"]/div/ul[2]/li[4]/button')
timeSetMax.click()
Apply_timeSetMax = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/button')
Apply_timeSetMax.click()
print('Time Period Set to \'MAX\'')

## https://hello-bryan.tistory.com/194
## -- Scroll infinte or unknown height page -- url : https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
driver.implicitly_wait(2)

WhileFlag = True
WhilePivot = 5000

while WhileFlag:
    driver.execute_script("window.scrollTo(0,"+str(WhilePivot)+")")
    driver.implicitly_wait(1)
    try:
        WhileFlagDriver=driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr['+WhilePivot+']/td[1]')
        WhileFlag = False
        print('Scroll End')
    except: 
        WhileFlag = True
        WhilePivot = WhilePivot + 5000
        print('keep scrolling...')

## Get scroll height 
# SCROLL_PAUSE_TIME = 0.5
#last_height = driver.execute_script("return document.body.scrollHeight")
#
#while True:
#    #scroll down to bottom
#    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
#    
#    #Wait to load page
#    driver.implicitly_wait(SCROLL_PAUSE_TIME)
#    
#    #Calculate new scroll height and compare with last scroll height
#    new_height = driver.execute_script("return document.body.scrollHeight")
#    if new_height == last_height:
#        break
#    last_height = new_height
#//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[2609]/td[1]
    #//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[2610]/td[1]/span
### ------------------------------------------------------------------------
Table_stockprice = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table')

tbody = Table_stockprice.find_element_by_tag_name("tbody")
rows = tbody.find_elements_by_tag_name("tr")

for element in rows :
    print(element.text)
    print(element.text, file=open(filename_INPUT,'a',encoding='utf-8'))
    
