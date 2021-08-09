# encoding=utf-8
from textrank4zh import TextRank4Keyword, TextRank4Sentence
import os
import pandas as pd
import jieba
import jieba.analyse

csv_file = os.path.join('./output_1.xlsx')
# 遇到空白會自動跳過
content = pd.read_excel(csv_file,keep_default_na=False)
trans = content.copy()
jieba.load_userdict('./path_dict_zh.txt')

for index, row in trans.iterrows():
    df_seg=pd.DataFrame(columns=['長度','分數','字詞'])
    X = row['TextRank_abstract_300']
    if(X==" "):
        continue
    XX=X.split(';')
    words = list(filter(None, XX))
    # print(words)
    Y=words[0:300]
    # print(Y)

    for i in Y:
        # print(i)
        word=i.split('_')[0].strip()
        num=i.split('_')[1]
        # print(word)
        # print(num)
        df_seg=df_seg.append(({'長度':len(word),'分數':num, '字詞':word}),ignore_index=True)

    df_seg = df_seg.sort_values(['長度', '分數'], ascending=[False, False])
    final=df_seg[0:20]
    # print(final)
    
    mix=""
    for index2,row2 in final.iterrows():
        mix+=row2['字詞']+'_'+row2['分數']+';'
        # print(mix)
    trans.loc[index,'TextRank_abstract-300']=mix

trans.to_excel('./output_1.xlsx')
