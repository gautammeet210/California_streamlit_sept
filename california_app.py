import numpy as np
import joblib
import streamlit as st
from pathlib import Path

#------------------------------------------------------------------
model_path = Path(__file__).parent / "california.joblib"
obj = joblib.load(model_path)
model = obj['model']
cols = obj['columns']
#------------------------------------------------------------------
st.title('california app')
In=[]
for i in cols:
    v = st.number_input(f'Enter {i} :')
    In.append(v)
if st.button('click'):
    out = model.predict([In])
    st.success(out)  