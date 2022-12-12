import streamlit as st
from streamlit_option_menu import option_menu

from home import Home
from part_a import PartA
from part_b import PartB

page_title = 'DIT161-Project | Anastasios Kotronis (itp22104)'
page_icon=':bar_chart:'

st.set_page_config(
    page_title=page_title,
    # https://www.webfx.com/tools/emoji-cheat-sheet/
    page_icon=page_icon,
    layout='wide',
)

hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

with st.sidebar:
    main_selected = option_menu(
        menu_title=None,
        options = ['Home', 'Part A', 'Part B'],
        # https://icons.getbootstrap.com/
        icons = ['house', '', ''],
        menu_icon=None,
        orientation='vertical',
        default_index=0,
    )

if main_selected == 'Home':
    hm = Home()
    hm.load_page()
elif main_selected == 'Part A':
    pa = PartA()
    if pa.selected == 'Data Info':
        pa.display_info_page()
    elif pa.selected == 'A) Preparation':
        pa.display_preparation_page()
    elif pa.selected == 'B) Analysis':
        pa.display_analysis_page()
    
elif main_selected == 'Part B':
    pb = PartB()
    data_dict = pb.load_data()
