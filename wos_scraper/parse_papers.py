from wos_scraper.config import *
from wos_scraper import setup_page as sp


def get_texts(elements):
    list = []
    for e in elements:
        list.append(e.text)
    return ','.join(list)  # From list to comma-separated string


def parse_single_paper_from_url(url):
    driver = sp.setup_wos_driver(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    doi = soup.find(id='FullRTa-DOI').text
    keywords = soup.find_all(class_='mat-tooltip-trigger authorKeywordLink-en ng-star-inserted')
    plus_keywords = soup.find_all(class_='mat-tooltip-trigger keywordsPlusLink')

    # From list to comma-separated string
    kw_final = get_texts(keywords)
    plus_kw_final = get_texts(plus_keywords)
    driver.close()
    return doi, kw_final, plus_kw_final


def parse_papers_from_urls(df, column):
    # dois = []
    # kws = []
    # plus_kws = []
    df['doi'] = ''
    df['Keywords'] = ''
    df['Plus keywords'] = ''
    for index, row in df.iterrows():
        doi, kw, plus_kw = parse_single_paper_from_url(row[column])
        row['doi'], row['Keywords'], row['Plus keywords'] = doi, kw, plus_kw
        # dois.append(doi)
        # kws.append(kw)
        # plus_kws.append(plus_kw)
    return df


if __name__ == '__main__':
    print(parse_single_paper_from_url('https://www.webofscience.com/wos/woscc/full-record/WOS:000765566200001'))
