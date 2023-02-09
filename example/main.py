from wos_scraper import html_parser
from wos_scraper import setup_page
from wos_scraper import parse_soup
from bs4 import BeautifulSoup


search = 'https://www.webofscience.com/wos/woscc/summary/ff7d7f65-1ac6-4213-b788-f3caf673d7fd-6c336e02/relevance/1'

html_list = setup_page.get_html_through_paginations(search, range(1, 50))
html_files = setup_page.save_htmls(html_list)

for f in html_files:
    htmlfile = open(f, 'r', encoding='utf-8').read()
    # soup = BeautifulSoup(html, 'html.parser')
    soup = BeautifulSoup(htmlfile, 'html.parser')
    df = parse_soup.get_df(soup)
    df.to_csv('df-{}.csv'.format(f))