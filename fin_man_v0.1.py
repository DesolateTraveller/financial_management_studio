#---------------------------------------------------------------------------------------------------------------------------------
### Authenticator
#---------------------------------------------------------------------------------------------------------------------------------
import streamlit as st
#---------------------------------------------------------------------------------------------------------------------------------
### Import Libraries
#---------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#----------------------------------------
from io import BytesIO, StringIO
from PIL import Image
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objs as go
#----------------------------------------
import scipy.stats as stats
from scipy.stats import gaussian_kde
#---------------------------------------------------------------------------------------------------------------------------------
### Title and description for your Streamlit app
#---------------------------------------------------------------------------------------------------------------------------------
st.set_page_config(page_title="Financial Management Studio | v0.1",
                    layout="wide",
                    page_icon="📊",            
                    initial_sidebar_state="auto")
#---------------------------------------
st.markdown(
    """
    <style>
    .title-large {
        text-align: center;
        font-size: 35px;
        font-weight: bold;
        background: linear-gradient(to left, red, orange, blue, indigo, violet);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .title-small {
        text-align: center;
        font-size: 20px;
        background: linear-gradient(to left, red, orange, blue, indigo, violet);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .version-badge {
        text-align: center;
        display: inline-block;
        background: linear-gradient(120deg, #0056b3, #0d4a96);
        color: white;
        padding: 2px 12px;
        border-radius: 20px;
        font-size: 1.15rem;
        margin-top: 8px;
        font-weight: 600;
        letter-spacing: 0.5px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    }
    </style>
    <div style="text-align: center;">
        <div class="title-large">Financial Management Studio</div>
        <div class="version-badge"> Play with Money | v0.1 </div>
    </div>
    """,
    unsafe_allow_html=True
)
st.divider()

