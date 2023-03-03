from text_analysis.config import *


def txt_punc_rmv(text, nan_value):
    """custom function to remove the punctuation and lower case words"""
    PUNCT_TO_REMOVE = string.punctuation
    f = str(text)
    if f == nan_value:
        return nan_value
    else:
        return text.translate(str.maketrans('', '', PUNCT_TO_REMOVE))


def txt_stopwords_rmv(text, nan_value):
    """custom function to remove the stopwords"""
    STOPWORDS = set(stopwords.words('english'))
    if str(text) == nan_value:
        return nan_value
    else:
        return " ".join([word for word in str(text).split() if word not in STOPWORDS])


def most_frequent_words(df, target_col, nan_values='nan', n=10):
    cnt = Counter()
    for text in df[target_col].values:
        if str(text) != nan_values:
            for word in text.split():
                cnt[word] += 1
    return cnt.most_common(n)


def txt_specific_word_rmv(text, words2rmv, nan_value='nan'):
    if str(text) == nan_value:
        return nan_value
    else:
        return " ".join([word for word in str(text).split() if word not in words2rmv])


def stem_words(text, nan_value='nan'):
    if str(text) == nan_value:
        return nan_value
    else:
        stemmer = PorterStemmer()
        return " ".join([stemmer.stem(word) for word in text.split()])


def lemmatize(text, nan_value='nan'):
    if str(text) == nan_value:
        return nan_value
    else:
        lemmatizer = WordNetLemmatizer()
        wordnet_map = {"N": wordnet.NOUN, "V": wordnet.VERB, "J": wordnet.ADJ, "R": wordnet.ADV}
        pos_tagged_text = nltk.pos_tag(text.split())
        return " ".join([lemmatizer.lemmatize(word, wordnet_map.get(pos[0], wordnet.NOUN)) for word, pos in pos_tagged_text])


def prepro(df, target_col, nan_values='nan', **kwargs):
    # First we lowercase all words
    df[target_col] = df[target_col].str.lower()

    # If a list of specific words to remove is passed, remove them with priority
    for kw in kwargs.items():
         if 'specific_word2rmv' in kw[0]:
            df[target_col] = df[target_col].apply(lambda text: txt_specific_word_rmv(text, kw[1], nan_values))
    df[target_col] = df[target_col].apply(lambda text: txt_punc_rmv(text, nan_values))
    df[target_col] = df[target_col].apply(lambda text: txt_stopwords_rmv(text, nan_values))
    df[target_col] = df[target_col].apply(lambda text: stem_words(text))
    df[target_col] = df[target_col].apply(lambda text: lemmatize(text))
    return df