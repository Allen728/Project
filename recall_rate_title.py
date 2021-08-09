import os
import pandas as pd
from string import digits
import re
import numpy as np

csv_file = os.path.join('./output_1.xlsx')
content = pd.read_excel(csv_file,keep_default_na=False)
trans = content.copy()

for index, row in trans.iterrows():
    actual = row['kw_zh']
    list_actual = re.split(";",str(actual))                  # 將資料轉為list格式
    # print(list_actual)

    predicted = row['TextRank_title-300']
    if(predicted==" "):
        continue
#將內容處理成純文字
    a = predicted.replace(" ","")
    # print(a)
    remove_digits = str.maketrans('', '', digits)       
    res = a.translate(remove_digits)
    # print(res)
    list_predicted = re.split(r"_.;",res)
    list_predicted.remove("")
    # print(list_predicted)
    # print(len(list_predicted))

# 招出相同的詞
    list1_as_set = set(list_actual)                         
    intersection = list1_as_set.intersection(list_predicted)
    intersection_as_list = list(intersection)

    # print(intersection_as_list)
    len_title = len(intersection_as_list)   # 分子長度    
    # print(len_title)  
    len_kw = len(list_actual)               # 分母長度
    # print(len_kw)

    recall_rate = len_title/len_kw
    # print(recall_rate)
    
    trans.loc[index,'title_300_查全率']=str(recall_rate)

trans.to_excel('./output_1.xlsx')