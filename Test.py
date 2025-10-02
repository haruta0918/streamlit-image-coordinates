import streamlit as st
import pandas as pd

st.title("ファイル選択してインポート")

# ファイルを選択するUI（CSV限定にしている例）
uploaded_file = st.file_uploader("CSVファイルを選択してください", type=["json","jpg","jpeg"])

if uploaded_file is not None:
    # Pandasで読み込む
    df = pd.read_csv(uploaded_file)
    st.write("読み込んだデータ:")
    st.dataframe(df)