from .config import *


def get_text_or_NA(item):
    """
    Get and assign the text (string) of the html element or nan in case it is a nan object
    :param item: AnyResult object (beautifulsoup), item resulting from .find() function
    :return: string, string of the argument item
    """
    try:
        result = item.text
    except AttributeError:
        result = ''
    return result


def parse_html_get_table(htmlfile):
    """
    Parse html, get paper information (author, title, year, abstract), and saves as .csv
    :param htmlfile: str, path to the html file to be parsed
    :return: DataFrame object, dataframe table with tabularized parsed information
    """
    soup = BeautifulSoup(htmlfile, 'html.parser')
    papers = soup.find_all('div', {'class': 'data-section'})
    abs_list = []
    title_list = []
    auths_list = []
    year_list = []
    journal_list = []
    cit_list = []
    for paper in papers:
        # Search html elements within paper Div
        title = paper.find('a', class_='title title-link font-size-18 ng-star-inserted')
        abstract = paper.find('div', class_='abstract show-more-btn ng-star-inserted expanded')
        author = paper.find('a', class_='mat-tooltip-trigger authors ng-star-inserted')
        year = paper.find('span', class_='value ng-star-inserted')
        journal = paper.find('a', class_='mat-focus-indicator mat-tooltip-trigger font-size-14 '
                                         'summary-source-title-link remove-space no-left-padding '
                                         'mat-button mat-button-base mat-primary ng-star-inserted')
        citations = paper.find('a', class_='stat-number font-size-24 link link-color ng-star-inserted')

        # Assign text values or give nan
        text_abstract = get_text_or_NA(abstract)
        text_title = get_text_or_NA(title)
        text_author = get_text_or_NA(author)
        text_year = get_text_or_NA(year)
        text_journal = get_text_or_NA(journal)
        text_citations = get_text_or_NA(citations)

        # Append lists
        abs_list.append(text_abstract)
        title_list.append(text_title)
        auths_list.append(text_author)
        year_list.append(text_year)
        journal_list.append(text_journal)
        cit_list.append(text_citations)

        # Create and fill df
        df = pd.DataFrame({'Author': auths_list,
                           'Year': year_list,
                           'Title': title_list,
                           'Journal': journal_list,
                           'Abstract': abs_list})
    return df



