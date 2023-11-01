from table_example import html
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import re

# Öffnungszeiten KVR
# 7:30
# 8:30
# 7:30
# 8:30
# 7:30



browser = webdriver.Firefox()
# Parse the HTML with BeautifulSoup
# soup = BeautifulSoup(html, 'html.parser')

def pass_captcha():
    print('test pass_captcha')
    # needs work
    # connect to captcha solver api

def check_for_termin(): 
    # display full calendar, this is useful for debugging  
    js_script = '''            
        // Select all elements with the class name "htmlCalendarMonth"
        var elements = document.querySelectorAll(".htmlCalendarMonth");

        // Now 'elements' is a NodeList containing all elements with the specified class name
        // You can loop through the NodeList to access each element
        for (var i = 0; i < elements.length; i++) {
            elements[i].style.display = "block"
        }
    '''
    browser.execute_script(js_script)
    
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # Use the 'select' method to find all <td> elements
    td_elements = soup.select("td")

    # Loop through and print the contents of each <td> element
    free_termine_numbers = []
    date_pattern = r"\d{1,2}\.\d{1,2}\.\d{4}"
    for i, td in enumerate(td_elements):
        # exclude empty table fields
        if(not td.text):
            print('empty place holder table field')
        elif('Keine freien Termine am' not in td.text):
            # we have found a free termin
            print('Valid Termin?')
            print(td)
            print(i)
            # Extract date pattern from the td text
            date_string = re.search(date_pattern, td.text).group()
            print(f'Free Termin. Index: {i} Date: {date_string}')
            free_termine_numbers.append(i)
        else:
            # Find all matches of the date pattern in the text
            date_string = re.search(date_pattern, td.text).group()
            print(f'{i}: {date_string}')

    if(free_termine_numbers):
        # Find all the <td> elements on the page
        td_selenium_elements = browser.find_elements(By.TAG_NAME, "td")
        # first free termin
        nth_td = td_selenium_elements[free_termine_numbers[0]]
        print(f'first termin is: {nth_td.text}')

        # notify me via email that a free termin was found

        # extend script to automatically book a termin
        # ...
    else:
        print('there are no free termine currently')
                

def driver():
    browser.get('https://terminvereinbarung.muenchen.de/abh/termin/index.php?')
    browser.maximize_window()

    # select Notfalltermin/ Emergency Appointment (students, scientists, blue card & family)
    # CASETYPES[Notfalltermin UA 35]
    select_element = browser.find_element(By.NAME, "CASETYPES[Notfalltermin UA 35]")

    # Initialize a Select object for the select element
    select = Select(select_element)

    # Set the desired value by its visible text
    select.select_by_visible_text("1")

    # give time to manually solve the captcha
    time.sleep(10)
    
    # pass_captcha()
    
    check_for_termin()

    # browser.close()




driver()