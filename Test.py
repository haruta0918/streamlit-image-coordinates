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
import streamlit as st
from PIL import Image
import streamlit as st

file_id = "11HEtRxLGCxqLWsO2vEW22kMLSw4byOkP"  # あなたの画像IDに置き換えて
image_url = f"https://drive.google.com/file/d/11HEtRxLGCxqLWsO2vEW22kMLSw4byOkP/view?usp=drive_link={file_id}"

st.image(image_url, caption="Google Driveから表示", use_column_width=True)

# folder_path = "実験中"
# 

# フォルダ内のjpgファイルをすべて取得
# jpg_files = glob.glob(os.path.join(folder_path, "*.jpg"))

# count=len(jpg_files)
# y=0
# z=jpg_files[y]

# for y in range(count):
#         img = Image.open(z)
#         st.image(img)
#         z=jpg_files[y]

# st.title("画像ファイルを表示")

# uploaded_file = st.file_uploader("画像を選んでください", type=["png", "jpg", "jpeg"])

# if uploaded_file is not None:
#     img = Image.open(uploaded_file)
#     st.image(img, caption="アップロードした画像")