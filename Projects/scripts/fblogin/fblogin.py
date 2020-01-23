#! python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# My info
user = "hamzaarain230@yahoo.com"
pwd = "hamza123!@#"

# TODO: Load browser with facebook site  
browser = webdriver.Firefox()
browser.get("http://www.facebook.com")

# TODO: username, password entry box widget & submit button
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit   = browser.find_element_by_id("loginbutton")

# TODO: Passing My info   
username.send_keys(user)
password.send_keys(pwd)

# TODO: Execute by submit
submit.click()
  