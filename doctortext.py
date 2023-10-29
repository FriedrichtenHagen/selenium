from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Firefox()



browser.get('https://www.doctolib.de/allgemeinmedizin/muenchen')

time.sleep(5)

# click past consent banner
consent_banner = browser.find_element(By.ID, "didomi-notice-disagree-button")
consent_banner.click()

termin_vereinbaren = browser.find_element(By.CLASS_NAME, "Tappable-inactive.dl-button-primary.dl-button.dl-button-size-medium")

print(termin_vereinbaren.location)
termin_vereinbaren.click()