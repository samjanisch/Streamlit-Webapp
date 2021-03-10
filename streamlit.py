import streamlit as st
import pandas as pd
import numpy as np

st.title('title text goes here')

df = pd.DataFrame({
    'first column' : [1, 4, 7],
    'second column' : [12, 6, 12]
})

df

chart_data = pd.DataFrame(
    np.random.randn(60,3),
    columns=[1,2,3]
)

chart_data