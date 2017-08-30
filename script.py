import time
import schedule
import smtplib
from datetime import datetime
from threading import Timer
import sqlite3
import sys
import csv
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys 
#%config IPCompleter.greedy=True
from selenium.common.exceptions import NoSuchElementException
x=datetime.today()
y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
delta_t=y-x
secs=delta_t.seconds+1

def auto():
    driver=webdriver.Chrome('C:/Users/Owner/chromedriver.exe')
    driver.get('https://www.rescuetime.com/dashboard')
    driver.find_element_by_name("email").send_keys("vincentv@gmail.com")
    driver.find_element_by_name("password").send_keys("**************")
    driver.find_element_by_name("button").click()
    global a
    a=int(driver.find_element_by_class_name("score").text)
    driver.close()
    print(a)
    type(a)

def mail():
    content='productivity is'+str(a)+"%."
    mail=smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.ehlo()
    mail.login('vincentv@gmail.com','**************')
    mail.sendmail('vincentv@gmail.com','wincen@gmail.com ',content)
    mail.quit()
    print(a)
    type(a)
    
def block():
    hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
    redirect="127.0.0.1"
    redirect_v6="::1"
    website_list=["www.facebook.com","facebook.com","fb.com","instagram.com","yt.com","yt.ca","quora.com","youtube.com","https://www.quora.com"]
    while True:
        if a < 70:
            print("you need to concentrate more")
            with open(hosts_path,'r+') as file:
                content=file.read()
                for website in website_list:
                    if website in content:
                        pass   
                    else:
                        file.write(redirect+" "+ website+"\n")
                        file.write(redirect_v6+" "+website+"\n")
        else:
            with open(hosts_path,'r+') as file:
                content=file.readlines()
                file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
            print("You can visit the websites, please keep the track of time...great going")
    
schedule.every(2).minutes.do(auto)
schedule.every(2).minutes.do(mail)
schedule.every(3).minutes.do(block)

while True:
    schedule.run_pending()
    time.sleep(1)

    

