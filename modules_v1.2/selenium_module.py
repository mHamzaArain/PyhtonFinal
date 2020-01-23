# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('https://automatetheboringstuff.com')
# browser.find_element_by_css_selector()    # paste specific CSS field
# ele.click()                        # To enter 
# send_keys()                     # input
# button.submit()               # submit (login)                     
# browser.back()               # To backward
# browser.forward()          # To forward
# browser.refresh()           # To refresh browser
# browser.quit()                # To quit browser

# ################Login facebook
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# user = "hamzaarain1999@gmail.com"
# pwd = "hamza123!@#"
  
# browser = webdriver.Firefox()
# browser.get("http://www.facebook.com")
  
# username = browser.find_element_by_id("email")
# password = browser.find_element_by_id("pass")
# submit   = browser.find_element_by_id("loginbutton")
  
# username.send_keys(user)
# password.send_keys(pwd)
  
# submit.click()