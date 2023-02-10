from wos_scraper import setup_page
from wos_scraper import parse_soup

search = 'https://www.webofscience.com/wos/woscc/summary/ff7d7f65-1ac6-4213-b788-f3caf673d7fd-6c336e02/relevance/1'

html_list, html_save_files = setup_page.get_html_through_paginations(search, range(1, 50))
# html_files = setup_page.save_htmls(html_list)
# html_save_files = []
# for i in range(1, 23):
#     html_save_files.append('html_source_page_{}.html'.format(i))

# for f in html_save_files:
#     htmlfile = open(f, 'r', encoding='utf-8').read()
#     df = parse_soup.parse_html_get_table(htmlfile)
#     df.to_csv('df-{}.csv'.format(f))