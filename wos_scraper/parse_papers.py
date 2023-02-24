from wos_scraper.config import *
from wos_scraper.setup_page import setup_wos_driver
from wos_scraper.parse_soup import get_text_or_NA


def get_texts(elements):
    """
    Gets a result set from the BeautifulSoup method find_all() and return a
    comma-separated string of the texts contained in the result set
    :param elements: bs4.element.ResultSet, list containing strings to extract
    :return: str, comma-separated words
    """
    list = []
    for e in elements:
        txt = get_text_or_NA(e)
        list.append(txt)
    return ','.join(list)  # From list to comma-separated string


def parse_single_paper_from_url(url):
    """
    Scrapes specific metadata of a given paper (input as url to the WoS link of the paper),
    see in return the output data.
    :param url: str, url to the WoS link of the paper
    :return: tuple of strings of size 5, containing the DOI, keywords, plus-keywords,
    research areas, and corresponding address of the paper
    """
    driver = setup_wos_driver(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    doi = soup.find(id='FullRTa-DOI')
    keywords = soup.find_all(class_='mat-tooltip-trigger authorKeywordLink-en ng-star-inserted')
    plus_keywords = soup.find_all(class_='mat-tooltip-trigger keywordsPlusLink')
    rareas = soup.find(id='CategoriesTa-subjectsLabel').find_all(class_='value-wrap ng-star-inserted')
    caddress = soup.find(id='AiinTa-RepAddressFull-0')

    # From list to comma-separated string
    doi = get_text_or_NA(doi)
    kw_final = get_texts(keywords)
    plus_kw_final = get_texts(plus_keywords)
    rareas_final = get_texts(rareas)
    caddress = get_text_or_NA(caddress)
    driver.close()
    return doi, kw_final, plus_kw_final, rareas_final, caddress


def parse_papers_from_urls(df, column):
    """
    Appends a dataframe with more specific data on the papers (DOI, keywords, plus-keywords, research areas,
    corresponding address), which are accessible under the WoS paper link.
    :param df: pd.Dataframe, dataframe containing papers urls (WoS links) to scrape more specific information
    :param column: str, name of the column that contains the urls
    :return: pd.Dataframe, a dataframe appended with the more specific data of each paper
    """

    df['doi'] = ''
    df['Keywords'] = ''
    df['Plus keywords'] = ''
    df['Research areas'] = ''
    df['Corresponding address'] = ''
    for index, row in df.iterrows():
        doi, kw, plus_kw, areas, address = parse_single_paper_from_url(row[column])
        df.loc[index, 'doi'] = doi
        df.loc[index, 'Keywords'] = kw
        df.loc[index, 'Plus keywords'] = plus_kw
        df.loc[index, 'Research areas'] = areas
        df.loc[index, 'Corresponding address'] = address

    return df
