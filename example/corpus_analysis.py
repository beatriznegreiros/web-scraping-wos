from text_analysis.text_prepro import prepro, most_frequent_words
from text_analysis.config import *

df = pd.DataFrame([])
for i in range(1, 41):
    f = './../example/connectivity-OR-exchange-OR-coupling-AND-river-OR-stream-OR-hyporheic-peerreview/df-{}.csv'.format(i)
    df_just_read = pd.read_csv(f)
    df = pd.concat([df, df_just_read], ignore_index=True)

df['Abstract'] = df['Abstract'].str[:-9]
specific_word2rmv = ['elsevier', '[1]', '[2]', '[3]', 'all rights reserved']
df_cleaned = prepro(df, target_col='Abstract', specific_word2rmv=specific_word2rmv)
words = most_frequent_words(df_cleaned, target_col='Abstract', n=50)
print(words)

df_cleaned.to_csv('test_clean.csv')