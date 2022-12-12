import numpy as np
import pandas as pd
from pathlib import Path
import streamlit as st

class PartB:
    def __init__(self):
        self.data_dict = {}
        self.data_fld = Path().absolute() / 'Data' / 'Part-B'

    @st.cache
    def load_data(self):
        return self.data_dict