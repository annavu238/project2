import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
import seaborn as sns
import plotly.express as px

data = pd.read_csv('https://raw.githubusercontent.com/annavu238/project2/refs/heads/main/social-media-impact-on-suicide-rates.csv', on_bad_lines='skip')
st.table(data.head())
# Analyze the percentage change in suicide rates since 2010 by year
suicide_rate_change = data.groupby('year')['Suicide Rate % change since 2010'].mean().reset_index()

# Plotting the average suicide rate change over the years
plt.figure(figsize=(10, 5))
plt.plot(suicide_rate_change['year'], suicide_rate_change['Suicide Rate % change since 2010'], marker='o')
plt.title('Average Suicide Rate Change Since 2010')
plt.xlabel('Year')
plt.ylabel('Suicide Rate % Change')
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
