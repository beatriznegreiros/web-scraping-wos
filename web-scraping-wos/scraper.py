from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://www.webofscience.com/wos/woscc/summary/ff7d7f65-1ac6-4213-b788-f3caf673d7fd-6c336e02/relevance/1')

time.sleep(3)
consent_button = driver.find_element(By.ID, value='onetrust-accept-btn-handler')
consent_button.click()

try:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'pendo-button-f8b7283d')))
    remind_button = driver.find_element(By.ID, value='pendo-button-f8b7283d')
    remind_button.click()
except TimeoutException:
    pass

element = 'show-more.show-more-text'
btns = driver.find_elements(By.CSS_SELECTOR, element)
print(btns)
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
