import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
import seaborn as sns
import plotly.express as px

data = pd.read_csv('https://raw.githubusercontent.com/annavu238/project2/refs/heads/main/gym_members_exercise_tracking.csv', on_bad_lines='skip')
st.table(data.head())

plt.figure(figsize=(12,6))
sns.countplot(hue='Gender',x='Workout_Type',data=df)
plt.title('exercise preference by male and female')
plt.show()


