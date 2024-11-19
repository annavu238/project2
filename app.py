import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
import seaborn as sns
import plotly.express as px

data = pd.read_csv('https://raw.githubusercontent.com/annavu238/project2/refs/heads/main/gym_members_exercise_tracking.csv', on_bad_lines='skip')
st.table(data.head())
# Analyze the percentage change in suicide rates since 2010 by year
both_sexes = data[data['sex'] == 'BTSX']
both_sexes['year'] = both_sexes['year'].astype(int)
both_sexes = both_sexes.sort_values(by='year')

# Plotting the average suicide rate change over the years
plt.figure(figsize=(10, 6))
plt.plot(both_sexes['year'], both_sexes['Suicide Rate % change since 2010'], marker='o', linestyle='-', color='b')
plt.title('Average Suicide Rate Change Over the Years')
plt.xlabel('Year')
plt.ylabel('Suicide Rate % Change Since 2010')
plt.grid(True)
plt.xticks(both_sexes['year'], rotation=45)
plt.tight_layout()
plt.show()
