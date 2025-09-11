import streamlit as st

from streamlit_image_coordinates import streamlit_image_coordinates
import streamlit as st
import pandas as pd
import numpy as np
import json
import os

import os
folder_path = 'いじる用'
o=0
t=0

for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
            t+=1
 
            # .jsonファイルを取得して並び替え（オプション）
            json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
            json_files.sort()  # ソートすると見やすい順に並ぶ

            folder_path2=folder_path+'/'    
            a2=0
            a=json_files[a2]
            stra=str(a)
            c=folder_path2+stra
            json_open=open(c, 'r',encoding='utf-8') 
            json_load = json.load(json_open)

            keido=json_load['geoData']['longitude']
            ido=json_load['geoData']['latitude']
            keido2=str(keido)
            ido2=str(ido)
            keido3="経度"+keido2
            ido3="緯度"+ido2

            st.write(keido3)
            st.write(ido3)
            print(t)
    

      