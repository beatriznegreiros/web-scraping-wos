from .config import *


def get_text_or_NA(item):
    try:
        result = item.text
    except AttributeError:
        result = ''
    return result


def get_df(soup):
    papers = soup.find_all('div', {'class': 'data-section'})
    abs_list = []
    title_list = []
    auths_list = []
    for paper in papers:
        # Search html elements within paper Div
        title = paper.find('a', class_='title title-link font-size-18 ng-star-inserted')
        abstract = paper.find('div', class_='abstract show-more-btn ng-star-inserted expanded')
        author = paper.find('a', class_='mat-tooltip-trigger authors ng-star-inserted')

        # Assign text values or give nan
        text_abstract = get_text_or_NA(abstract)
        text_title = get_text_or_NA(title)
        text_author = get_text_or_NA(author)

        # Append lists
        abs_list.append(text_abstract)
        title_list.append(text_title)
        auths_list.append(text_author)

        # Create and fill df
        df = pd.DataFrame({'Title': title_list, 'Author': auths_list, 'Abstract': abs_list})
    return df


