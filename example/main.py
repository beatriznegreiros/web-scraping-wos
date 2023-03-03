from wos_scraper import setup_page
from wos_scraper import parse_soup
from wos_scraper import parse_papers
import pandas as pd

# search = "https://www.webofscience.com/wos/woscc/summary/dfca8c06-a62a-4bf8-b350-f286cf1f5359-6f9083c2/relevance/1"
# Link for peer review articles (both researcha nd review papers)
# search = "https://www.webofscience.com/wos/woscc/summary/f96571ae-a383-4a5f-adb9-1be0f91dfe77-729d773d/relevance/1"
# html_list, html_save_files = setup_page.get_html_through_paginations(search, range(1, 41))
# html_files = setup_page.save_htmls(html_list)

# for i in range(1, 41):
#     f = './connectivity-OR-exchange-OR-coupling-AND-river-OR-stream-OR-hyporheic-peerreview/' \
#         'html_source_page_{}.html'.format(i)
#     htmlfile = open(f, 'r', encoding='utf-8').read()
#     df = parse_soup.parse_html_get_table(htmlfile)
#     df.to_csv('./connectivity-OR-exchange-OR-coupling-AND-river-OR-stream-OR-hyporheic-peerreview/df-{}.csv'.format(i))


for i in range(26, 41):
    f = './connectivity-OR-exchange-OR-coupling-AND-river-OR-stream-OR-hyporheic-peerreview/df-{}.csv'.format(i)
    df = pd.read_csv(f)
    df_new = parse_papers.parse_papers_from_urls(df, column='wos_link')
    df_new.to_csv('./connectivity-OR-exchange-OR-coupling-AND-river-OR-stream-OR-hyporheic-peerreview/df-appended-{}.csv'.format(i))