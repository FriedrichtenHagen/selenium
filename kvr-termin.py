from table_example import html

from bs4 import BeautifulSoup

# https://terminvereinbarung.muenchen.de/abh/termin/index.php?

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Firefox()


def pass_captcha():
    
    # needs work
    # connect to captcha solver api
    
    print('test')



def check_month_for_termin():
    
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
                


def driver():
    browser.get('https://terminvereinbarung.muenchen.de/abh/termin/index.php?')
    
    pass_captcha()
    
    check_month_for_termin()






check_month_for_termin()
