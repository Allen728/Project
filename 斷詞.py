# encoding=utf-8
import jieba
import os
import pandas as pd
# import re

csv_file = os.path.join('./GRB_testing_20200720.xlsx')
content = pd.read_excel(csv_file)
trans=content.copy()
jieba.load_userdict('./path_dict_zh.txt')
for index, row in trans.iterrows():
        # print(index)
        # print(row)
    title_seg = jieba.cut(trans['title_zh'][index])
    trans.loc[index,'title_zh_seg']=(' ').join(title_seg)
    abs_seg = jieba.cut(trans['abstract_zh'][index])
    trans.loc[index,'abstract_zh_seg']=(' ').join(abs_seg)

trans.to_excel('./GRB_testing_20200720.xlsx')
