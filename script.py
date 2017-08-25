#import statements

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys 
import time
%config IPCompleter.greedy=True
from selenium.common.exceptions import NoSuchElementException

#Selenium part

driver=webdriver.Chrome('C:/Users/Owner/chromedriver.exe')
driver.get('https://www.rescuetime.com/dashboard')
driver.find_element_by_name("email").send_keys("vincent.vanhouke@gmail.com")
driver.find_element_by_name("password").send_keys("***************")
driver.find_element_by_name("button").click()
y=int(driver.find_element_by_class_name("score").text)
driver.close()
