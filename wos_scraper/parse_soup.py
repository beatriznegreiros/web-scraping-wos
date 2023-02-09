from .config import *


def get_df(soup):
    papers = soup.find_all('div', {'class': 'data-section'})
    abs_list = []
    title_list = []

    for paper in papers:
        title = paper.find('a', class_='title title-link font-size-18 ng-star-inserted')
        abstract = paper.find('div', class_='abstract show-more-btn ng-star-inserted expanded')
        try:
            text_abstract = abstract.text
        except AttributeError:
            text_abstract = ''
        try:
            text_title = title.text
        except AttributeError:
            text_title = ''
        abs_list.append(text_abstract)
        title_list.append(text_title)
        df = pd.DataFrame(title_list, columns=['Titles'])
        df['Abstract'] = pd.DataFrame(abs_list)
    return df


