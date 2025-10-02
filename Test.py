import streamlit as st
from PIL import Image

st.title("画像ファイルを表示")

uploaded_file = st.file_uploader("画像を選んでください", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="アップロードした画像")