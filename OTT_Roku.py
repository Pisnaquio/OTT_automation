#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from bs4 import BeautifulSoup
import requests

usernameStr = ''
passwordStr = ''
browser = webdriver.Chrome()
browser.get(('https://my.roku.com/index'))
# fill in username and hit the next button
username = browser.find_element_by_name('email')
username.send_keys(usernameStr)
password = browser.find_element_by_name('password')
password.send_keys(passwordStr)
sleep(5)
browser.get(('https://developer.roku.com/developer-channels/analytics/channel/75619'))

