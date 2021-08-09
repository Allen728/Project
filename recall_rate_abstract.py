import os
import pandas as pd
from string import digits
import re

csv_file = os.path.join('./output_1.xlsx')
content = pd.read_excel(csv_file,keep_default_na=False)
trans = content.copy()

for index, row in trans.iterrows():
    actual = row['kw_zh']
    list_actual = re.split(";",str(actual))
    # print(list_actual)

    predicted= row['TextRank_abstract-300']
    # print(predicted)
    if(predicted==" "):
        continue
#將內容處理成純文字
    a=predicted.replace(" ","")
    # print(a)
    remove_digits = str.maketrans('', '', digits)
    res = a.translate(remove_digits)
    # print(res)
    list_predicted=re.split(r"_.;",res)
    list_predicted.remove("")
    # print(list_predicted)

    # print(len(list_predicted))

    list1_as_set = set(list_actual)
    intersection = list1_as_set.intersection(list_predicted)
    intersection_as_list = list(intersection)

    # print(intersection_as_list)
    len_abstract=len(intersection_as_list)
    
    # print(len_abstract) 
    len_kw=len(list_actual)
    # print(len_kw)  

    recall_rate=str(len_abstract/len_kw)
    # print(recall_rate)

    trans.loc[index,'abstract_300_查全率']=recall_rate
    # print(recall_rate)
trans.to_excel('./output_1.xlsx')