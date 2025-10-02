import streamlit as st




from streamlit_image_coordinates import streamlit_image_coordinates
import streamlit as st

import pandas as pd
import numpy as np
import json
import os
import streamlit as st
from PIL import Image
import os
import streamlit as st
from PIL import Image

import glob
import os

# 読み込みたいフォルダのパス

# フォルダ内のjpgファイルをすべて取得
# jpg_files = glob.glob(os.path.join(folder_path, "*.jpg"))
# st.set_page_config(
#     page_title="佐鳴湖のごみの写真",
#     layout="wide",
# )
st.title("画像ファイルを表示")

uploaded_file = st.file_uploader("画像を選んでください", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="アップロードした画像")


folder_path = "いじる用"

# フォルダ内のjpgファイルをすべて取得
jpg_files = glob.glob(os.path.join(folder_path, "*.jpg"))

count=len(jpg_files)
y=0
z=jpg_files[y]

for y in range(count):
        img = Image.open(z)
        st.image(img)
        z=jpg_files[y]
        st.write
import streamlit as st
from PIL import Image


