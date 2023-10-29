from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Firefox()



browser.get('https://8weapons-leipzig.de/kontakt/')

time.sleep(5)


elem = browser.find_element(By.CLASS_NAME, "wpforms-field-name-first")
print(elem.location)


# browser.get('https://stadt.muenchen.de/terminvereinbarung_/terminvereinbarung_abh.html?cts=1000116')
# try:
#     webobject1 = browser.find_element_by_class('terminbuchung')
#     print(webobject1.location)
# except:
#     print('Captcha could no be found on site.')
