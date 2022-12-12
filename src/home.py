import numpy as np
import pandas as pd
from pathlib import Path
import streamlit as st

class Home:
    def __init__(self):
        pass

    def load_page(self):
        st.title("Project for DIT161 (2022-2023)")
        st.write("### Anastasios Kotronis (itp22104)")
        st.write("---")
        st.markdown(f"""
            ##### Tools used: python | streamlit, plotly-express, pandas, numpy, skelarn, dython
        """)
        return