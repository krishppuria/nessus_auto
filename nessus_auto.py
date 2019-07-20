#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 21:28:38 2019

@author: krishna
"""

from selenium import webdriver
from time import sleep
import os

uname='root'
pass1='root'
driver = webdriver.Chrome("/home/krishna/Desktop/Nesseus_auto/chromedriver")

driver.get("https://parrot:8834/")
sleep(2)
user=driver.find_element_by_xpath('/html/body/div/form/div[1]/input')
user.send_keys(uname)
pass2=driver.find_element_by_xpath('/html/body/div/form/div[2]/input')
pass2.send_keys(pass1)

log_in=driver.find_element_by_xpath('/html/body/div/form/button')
log_in.click()

sleep(3)

new_scan=driver.find_element_by_xpath('//*[@id="titlebar"]/a[1]')
new_scan.click()
sleep(2)
advan_scan=driver.find_element_by_xpath('//*[@id="content"]/section/div[1]/a[2]')
advan_scan.click()
sleep(3)
scan_name='nessus_scan'
name=driver.find_element_by_xpath('//*[@id="editor-tab-view"]/div/div[1]/section/div[1]/div[1]/div[1]/div[1]/div/input')
name.send_keys(scan_name)

file_path='/a.txt'
sleep(3)
upload_ele=driver.find_element_by_xpath('//*[@id="editor-tab-view"]/div/div[1]/section/div[1]/div[1]/div[1]/div[6]/div/input')
upload_ele.send_keys(os.getcwd()+file_path)
sleep(2)
drop=driver.find_element_by_xpath('//*[@id="content"]/section/form/div[2]/i')
drop.click()
launch_scan=driver.find_element_by_xpath('//*[@id="content"]/section/form/div[2]/ul/li')
launch_scan.click()