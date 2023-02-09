from bs4 import BeautifulSoup
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def setup_wos_driver(link):
    # Open a firefox window
    driver = webdriver.Firefox()
    # driver.maximize_window()

    # Send GET request for the given http protocol (link)
    driver.get(link)
    # Wait approx 3 seconds to enable the consent cookies to show up
    time.sleep(3)

    # Find consent cookies by button ID
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler')))
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
    return driver


# Find all "Show more" buttons to open full-text abstracts
def scroll_and_click_showmore(indexes_to_loop, driver):
    is_not_clicked = []
    for i in indexes_to_loop:
        click_success = False
        paper_div = driver.find_element(By.XPATH,
                                        '/html/body/app-wos/main/div/div/div[2]/div/'
                                        'div/div[2]/app-input-route/app-base-summary-component/'
                                        'div/div[2]/app-records-list/app-record[{}]/div/div/div[2]/'
                                        'div[1]'.format(i))
        element = '/html/body/app-wos/main/div/div/div[2]/div/div/div[2]/' \
                  'app-input-route/app-base-summary-component/div/div[2]/' \
                  'app-records-list/app-record[{}]/div/div/div[2]/div[1]/' \
                  'div[2]/div/span[2]/button'.format(i)
        try:
            driver.execute_script("arguments[0].scrollIntoView(true);", paper_div)
            btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element)))
            btn.click()
            time.sleep(random.randint(1, 10))
        except TimeoutException:
            print('Could not fetch item {} . I will scroll up before moving forward with the next items.'.format(i))
            is_not_clicked.append(i)
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.UP)
            driver.execute_script("window.scrollBy(0,250);")
            time.sleep(2)
    return is_not_clicked


search = 'https://www.webofscience.com/wos/woscc/summary/ff7d7f65-1ac6-4213-b788-f3caf673d7fd-6c336e02/relevance/1'
page_driver = setup_wos_driver(link=search)
is_still_missing = scroll_and_click_showmore(indexes_to_loop=range(1, 51), driver=page_driver)
while len(is_still_missing) > 0:
    page_driver = setup_wos_driver(link=search)
    is_still_missing = scroll_and_click_showmore(indexes_to_loop=is_still_missing, driver=page_driver)


#
# html = driver.page_source
#
# soup = BeautifulSoup(html)
#
# for tag in soup.find_all('title'):
#     print(tag.text)
