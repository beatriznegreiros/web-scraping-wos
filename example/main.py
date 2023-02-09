from wos_scraper import html_parser
from wos_scraper import setup_page
from wos_scraper import parse_soup

from bs4 import BeautifulSoup


# search = 'https://www.webofscience.com/wos/woscc/summary/ff7d7f65-1ac6-4213-b788-f3caf673d7fd-6c336e02/relevance/1'
# page_driver = setup_page.setup_wos_driver(link=search)
# is_still_missing, driver = setup_page.scroll_and_click_showmore(indexes_to_loop=range(1, 11), driver=page_driver)
# html = driver.page_source


file = 'test-pagesource.html'
htmlfile = open(file, 'r', encoding='utf-8').read()
# soup = BeautifulSoup(html, 'html.parser')
soup = BeautifulSoup(htmlfile, 'html.parser')
df = parse_soup.get_df(soup)
df.to_csv('df-trial.csv')