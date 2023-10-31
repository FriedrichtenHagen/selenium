from table_example import html
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

browser = webdriver.Firefox()
# Parse the HTML with BeautifulSoup
# soup = BeautifulSoup(html, 'html.parser')

def pass_captcha():
    print('test pass_captcha')
    # needs work
    # connect to captcha solver api

def check_month_for_termin():    
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
    for i, td in enumerate(td_elements):
        # exclude empty table fields
        if(not td.text):
            print('td is empty')
        elif('Keine freien Termine am' not in td.text):
            # we have found a free termin
            print('Valid Termin?')
            print(td)
            print(i)
            termin_date = td.text[-10:]
            free_termine_numbers.append(i)
        else:
            print(f'{i}: {td.text[-10:]}')
    target_date = "29.10.2023"
    first_termin = browser.find_element("xpath", f"//td[contains(text(), '{target_date}')]")
    print(first_termin)

    print(f'first termin is: {first_termin}')
                

# https://terminvereinbarung.muenchen.de/abh/termin/index.php?
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
    
    check_month_for_termin()

    # browser.close()




driver()