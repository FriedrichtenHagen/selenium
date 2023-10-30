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
    
    # needs work
    # connect to captcha solver api
    
    print('test')



def check_month_for_termin():

    current_url = browser.current_url

    # Send an HTTP GET request to the URL
    response = requests.get(current_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the HTML content
        html = response.text
    else:
        print(f"Failed to retrieve the web page. Status code: {response.status_code}")

    soup = BeautifulSoup(html, 'html.parser')
    # Use the 'select' method to find all <td> elements
    td_elements = soup.select("td")
    
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

    # Loop through and print the contents of each <td> element
    for i, td in enumerate(td_elements):
        # exclude empty table fields
        if(not td.text):
            print('td is empty')
        elif('Keine freien Termine am' not in td.text):
            print('Valid Termin?')
            print(td)
            # access the correct month


        else:
            print(f'{i}: {td.text}')
                

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