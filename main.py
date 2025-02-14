import streamlit as st
import pandas as pd
import numpy as np

# df = pd.DataFrame({"カラム１": [1, 2, 3, 4], "カラム２": [5, 6, 7, 8]})
# df # マジックコマンド
# st.write(df) # writeメソッド

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["データ１", "データ２", "データ３"]
)
st.line_chart(chart_data)