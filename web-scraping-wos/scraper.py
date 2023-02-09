from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

# Open a firefox windoe
driver = webdriver.Firefox()
driver.maximize_window()

# Send GET request for the given http protocol (link)
driver.get('https://www.webofscience.com/wos/woscc/summary/ff7d7f65-1ac6-4213-b788-f3caf673d7fd-6c336e02/relevance/1')

# Wait approx 3 seconds to enable the consent cookies to show up
time.sleep(3)

# Find consent cookies by button ID
consent_button = driver.find_element(By.ID, value='onetrust-accept-btn-handler')
consent_button.click()  # click on accept cookies

# Find "Remind Later" cookie, if prompted, and click on "remind later"
try:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'pendo-button-f8b7283d')))
    remind_button = driver.find_element(By.ID, value='pendo-button-f8b7283d')
    remind_button.click()
# If the cookie was not prompted, then just proceed
except TimeoutException:
    pass

# Find all "Show more" buttons to open full-text abstracts
element = 'show-more.show-more-text'
btns = driver.find_elements(By.CSS_SELECTOR, element)

# Click on all buttons
for btn in btns:
    btn.click()
    print(btn)
    time.sleep(3)

#
# html = driver.page_source
#
# soup = BeautifulSoup(html)
#
# for tag in soup.find_all('title'):
#     print(tag.text)
