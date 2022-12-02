import streamlit as st
import pandas as pd
import numpy as np
import networkx as nx
import plotly.graph_objs as go
from  PIL import Image

#Add a logo (optional) in the sidebar
#logo = Image.open(r'C:\Users\13525\Desktop\Insights_Bees_logo.png')
logo = Image.open(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1zQyqOwMHGHnk708NVPhoMIKO3rtX3bd74vVVU4rIiQ&s')

st.sidebar.image(logo,  width=120)

#Add the expander to provide some information about the app
with st.sidebar.expander("About the App"):
     st.write("""
        This network graph app was built by Sharone Li using Streamlit and Plotly. You can use the app to quickly generate an interactive network graph with different layout choices.
     """)

#Add a file uploader to the sidebar
uploaded_file = st.sidebar.file_uploader('',type=['csv']) #Only accepts csv file format

#Add an app title. Use css to style the title
st.markdown(""" <style> .font {                                          
    font-size:30px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
st.markdown('<p class="font">Upload your data and generate an interactive network graph instantly...</p>', unsafe_allow_html=True)
