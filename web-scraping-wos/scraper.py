from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get('https://www.webofscience.com/wos/woscc/summary/ff7d7f65-1ac6-4213-b788-f3caf673d7fd-6c336e02/relevance/1')
# mycookies = driver.get_cookies()
# print(mycookies)
# print(len(mycookies))
# driver.delete_all_cookies()
time.sleep(3)
consent_button = driver.find_element(By.ID, value='onetrust-accept-btn-handler')
consent_button.click()
time.sleep(10)
try:
    remind_button = driver.find_element(By.ID, value='pendo-button-f8b7283d')
    remind_button.click()
finally:
    element = 'show-more.show-more-text'
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, element)))
    for btn in driver.find_elements(By.CLASS_NAME, element):
        btn.click()
#
# html = driver.page_source
#
# soup = BeautifulSoup(html)
#
# for tag in soup.find_all('title'):
#     print(tag.text)
