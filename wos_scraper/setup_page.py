from .config import *


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
    time.sleep(2)
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
    # Init list with items that couldnt be opened due to sophisticated web blocking
    is_not_clicked = []

    # Loop through all papers in the current page (50 in total)
    for i in indexes_to_loop:
        # Find Div element containing the paper records
        paper_div = driver.find_element(By.XPATH,
                                        '/html/body/app-wos/main/div/div/div[2]/div/'
                                        'div/div[2]/app-input-route/app-base-summary-component/'
                                        'div/div[2]/app-records-list/app-record[{}]/div/div/div[2]/'
                                        'div[1]'.format(i))
        # Defining the XPATH for the button of the iterating paper
        element = '/html/body/app-wos/main/div/div/div[2]/div/div/div[2]/' \
                  'app-input-route/app-base-summary-component/div/div[2]/' \
                  'app-records-list/app-record[{}]/div/div/div[2]/div[1]/' \
                  'div[2]/div/span[2]/button'.format(i)
        print('/html/body/app-wos/main/div/div/div[2]/div/'
                                        'div/div[2]/app-input-route/app-base-summary-component/'
                                        'div/div[2]/app-records-list/app-record[{}]/div/div/div[2]/'
                                        'div[1]'.format(i))
        try:
            driver.execute_script("arguments[0].scrollIntoView(true);", paper_div)
            btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element)))

            # Try to click
            try:
                btn.click()

            # If this exception is raised, it means a pop-up opened that we need to get rid off
            except ElementClickInterceptedException:
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'pendo-button-f8b7283d')))
                remind_button = driver.find_element(By.ID, value='pendo-button-f8b7283d')
                remind_button.click()
            time.sleep(random.randint(1, 10))

        # If timeout, then save the items that needed to be jumped and continue with the next paper
        except TimeoutException:
            print('Could not fetch item {} . I will scroll up before moving '
                  'forward with the next items.'.format(i))
            is_not_clicked.append(i)
            # Scroll to the top of the page to reset the automated scroll-down
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.UP)
            driver.execute_script("window.scrollBy(0,250);")

            # Sleep for 2 sec to make sure resetting took place
            time.sleep(2)
    return is_not_clicked, driver
