import streamlit as st

from streamlit_image_coordinates import streamlit_image_coordinates
import streamlit as st
import pandas as pd
import numpy as np
import json
import os

import os
folder_path = 'いじる用'
t=0

# フォルダ内の .jpg ファイルを探してループ
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg'):
        if t==0:
            print("1回目")
            # .jsonファイルを取得して並び替え（オプション）
            jpg_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]
            jpg_files.sort()  # ソートすると見やすい順に並ぶ

            folder_path2=folder_path+'/'    
            a2=0
            a=jpg_files[a2]
            stra=str(a)
            c=folder_path2+stra
            d = [c,]
        else:
            a2+=1
            a=jpg_files[a2]
            stra=str(a)
            c=folder_path2+stra
            d.append(c)
        t+=1
print(d[1]) 
e=0
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg'):       
        value = streamlit_image_coordinates(d[e])
        e+=1

