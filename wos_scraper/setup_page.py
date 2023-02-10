from .config import *


def setup_wos_driver(link):
    """
    Preparation of the web browser (driver) preceding the dynamic enabling of paper abstracts
    :param link: str, link containing the search made on Web f Science
    :return: WebDriver object, web browser opened on the web search made
    """
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
    """
    Scrolls through papers of the specific page and clicks on "show more" button,
    which opens the paper's full-text abstracts
    :param indexes_to_loop: list of paper-indexes to loop, e.g., Web of Science prompts 50 papers per page.
    :param driver: WebDriver object, browser opened on specific page
    :return: paper indexes (list) where abstract "show more" button was
    blocked and couldn't be clicked, WebDriver object (updated and ready to be parsed)
    with all "show more buttons" clicked
    """
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

        try:
            driver.execute_script("arguments[0].scrollIntoView(true);", paper_div)
            btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element)))

            # Try to click
            try:
                btn.click()

            # If this exception is raised, it means a pop-up opened that we need to get rid off
            except ElementClickInterceptedException:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'pendo-button-f8b7283d')))
                remind_button = driver.find_element(By.ID, value='pendo-button-f8b7283d')
                remind_button.click()
            except NoSuchElementException:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'pendo-close-guide-7176fce7')))
                newsort_button = driver.find_element(By.ID, value='pendo-close-guide-7176fce7')
                newsort_button.click()
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


def get_html_through_paginations(search, pags):
    """
    Get and save html in the working directory, ready-to-be-parsed, of each web driver (pagination)
    :param search: str, link containing the search made on Web f Science
    :param pags: list, list of pages to iterate. If the code should iterate
    through the first 10 search result pages, then pags = range(1, 11)
    :return: list of html per pagination, list of filenames (.html) saved
    """
    list_html_per_pagination = []
    file_list = []
    for i in pags:
        link_of_pagination = search[0:-1]+str(i)
        page_driver = setup_wos_driver(link=link_of_pagination)
        is_still_missing, driver = scroll_and_click_showmore(indexes_to_loop=range(1, 51), driver=page_driver)
        html = driver.page_source
        filename = 'html_source_page_{}.html'.format(i)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        list_html_per_pagination.append(html)
        file_list.append(filename)
    return list_html_per_pagination, file_list

