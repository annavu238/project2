import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
import seaborn as sns
import plotly.express as px

data = pd.read_csv('https://raw.githubusercontent.com/annavu238/project2/refs/heads/main/social-media-impact-on-suicide-rates.csv', on_bad_lines='skip')
st.table(data.head())

