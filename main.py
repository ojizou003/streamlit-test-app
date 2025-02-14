import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# df = pd.DataFrame({"カラム１": [1, 2, 3, 4], "カラム２": [5, 6, 7, 8]})
# df # マジックコマンド
# st.write(df) # writeメソッド

# 折れ線グラフ
chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=["データ１", "データ２", "データ３"]
)
st.line_chart(chart_data)

# ヒストグラム
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)

st.divider()

# マップ
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [35.69, 139.70], columns=["lat", "lon"]
)
st.map(map_data)

# スライダー
x = st.slider("xの値を選択してください")
st.write(x, "の２乗は、", x * x, "です")

# チェックボックス
if st.checkbox("Show dataframe"):
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.write(chart_data)

# セレクトボックス
option = st.selectbox("どちらか選んでください", ["A", "B"])
"You selected: ", option

# サイドバー
add_selectbox = st.sidebar.selectbox("好きな数字を選んでね", ["1", "2", "3"])
st.sidebar.write("あなたが選んで数字は", add_selectbox, "です")

# カラム
left_column, right_column = st.columns(2)

left_column.button("ボタン")

with right_column:
    chosen = st.selectbox("選んでください", ["A", "B", "C"])
    st.write(f"{chosen}が選ばれました")

# # キャッシュ機能...関数の前に@st.cacheをつけると、キャッシュ機能が有効になる
# @st.cache
# def fetch_and_clean_data(url):
#     df = pd.read_csv(url)
#     return df
