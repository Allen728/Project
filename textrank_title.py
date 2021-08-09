# encoding=utf-8
from textrank4zh import TextRank4Keyword, TextRank4Sentence
import os
import pandas as pd
import jieba
import jieba.analyse

csv_file = os.path.join('./GRB_testing_20200720.xlsx')
content = pd.read_excel(csv_file)
trans = content.copy()

def judge_pure_english(keyword):
    return all(ord(c) < 128 for c in keyword) 

jieba.load_userdict('./path_dict_zh.txt')
tr4w = TextRank4Keyword()
for index, row in trans.iterrows():
    X = row['seg_title_zh']
    # print(X)
    list_seg_content = X.split(' ')
    for i, seg in enumerate(list_seg_content):
        # print(i)
        if judge_pure_english(seg):
            list_seg_content[i] = ''
    X = ' '.join(list_seg_content)
    # print(X)
    tr4w.analyze(text=X, lower=True, window=2)
    Textrank_title=' '
    for item in tr4w.get_keywords(20, word_min_len=2):
        Textrank_title += item['word']+'_'+ str(item['weight'])+';'
    trans.loc[index,'Textrank_title']=Textrank_title
    print(Textrank_title)      
        # print(item)
# trans.to_excel('./GRB_testing_20200720.xlsx')