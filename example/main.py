from wos_scraper import setup_page
from wos_scraper import parse_soup

search = 'https://www.webofscience.com/wos/woscc/summary/ff7d7f65-1ac6-4213-b788-f3caf673d7fd-6c336e02/relevance/1'

# html_list, html_save_files = setup_page.get_html_through_paginations(search, range(1, 50))
# html_files = setup_page.save_htmls(html_list)

for i in range(1, 23):
    f = './outputs/html_source_page_{}.html'.format(i)
    htmlfile = open(f, 'r', encoding='utf-8').read()
    df = parse_soup.parse_html_get_table(htmlfile)
    df.to_csv('./outputs/df-{}.csv'.format(i))