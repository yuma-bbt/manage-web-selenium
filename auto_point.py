# coding:utf-8
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


for i in range(1,30):
    driver = webdriver.Chrome()
    driver.get("http://test")
    driver.find_element_by_id("u").send_keys("username")
    driver.find_element_by_id("p").send_keys("pass")
    driver.find_element_by_id("loginButton").click()
    driver.find_element_by_class_name("bnrBoxInner").click()
    sleep(3)
    driver.close()
    driver.quit()

