import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from time import sleep
import re
from collections import Counter
import heapq
import random

for i in range(1,101):
    browser = webdriver.Chrome(ChromeDriverManager().install()) 
    browser.get("https://docs.google.com/forms/d/e/1FAIpQLSdD1MgcD7Olbt5EGOrQ_xzPvp5TemhWEkwppwmQaC35fd5Zqw/viewform")
    soup = BeautifulSoup(browser.page_source, "lxml")

    for x in random.choices(('7','10')):
        browser.find_element(By.XPATH, '//*[@id="i'+x+'"]/div[3]/div').click()
        break
    for y in random.choices(('17','20','23','26','29','32')):
        browser.find_element(By.XPATH, '//*[@id="i'+y+'"]/div[3]/div').click()
        break
    for y in random.choices(('39','42','45','48')):
        browser.find_element(By.XPATH, '//*[@id="i'+y+'"]/div[3]/div').click()
        break
    for y in random.choices(('55','58','61','64','67','70','73')):
        browser.find_element(By.XPATH, '//*[@id="i'+y+'"]/div[3]/div').click()
        break
    for y in random.choices(('80','83','86','89','92','95')):
        browser.find_element(By.XPATH, '//*[@id="i'+y+'"]/div[3]/div').click()
        break
    browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span').click()

    for y in random.choices(('5','8','11','14','17')):
        browser.find_element(By.XPATH, '//*[@id="i'+y+'"]/div[3]/div').click()
        break

    for y in random.choices(('1','2','3','4','5')):
        browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/span/div/label['+y+']/div[2]/div/div/div[3]/div').click()
        break
    for y in random.choices(('28','31','34','37','40','43','46')):
        browser.find_element(By.XPATH, '//*[@id="i'+y+'"]/div[3]/div').click()
        break
    for y in random.choices(('1','2','3','4','5')):
        browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/span/div/label['+y+']/div[2]/div/div/div[3]/div').click()
        break
    for y in random.choices(('57','60','63','66','69')):
        browser.find_element(By.XPATH, '//*[@id="i'+y+'"]/div[3]/div').click()
        break
    for y in random.choices(('1','2','3','4','5')):
        browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/span/div/label['+y+']/div[2]/div/div/div[3]/div').click()
        break
    for y in random.choices(('80','83','86','89')):
        browser.find_element(By.XPATH, '//*[@id="i'+y+'"]/div[3]/div').click()
        break
    for y in random.choices(('1','2','3','4','5')):
        browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/span/div/label['+y+']/div[2]/div/div/div[3]/div').click()
        break
    browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span').click()
    sleep(3)
