import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
import seaborn as sns
import plotly.express as px

data = pd.read_csv('https://raw.githubusercontent.com/annavu238/project2/refs/heads/main/gym_members_exercise_tracking.csv', on_bad_lines='skip')
st.table(data.head())

# Title and description
st.title("Gym Members Exercise Tracking Analysis")
st.markdown("""
This application allows you to analyze the exercise data of gym members. 
Use the interactive filters on the sidebar to explore insights.
""")

# Display original data
st.subheader("Original Dataset")
st.dataframe(data.head())

# Sidebar filters
st.sidebar.header("Filters")

# Gender filter with a unique key
gender_filter = st.sidebar.multiselect(
    "Select Gender:",
    options=data['Gender'].unique(),
    default=data['Gender'].unique(),
    key="gender_filter"
)

# Experience Level filter with a unique key
experience_filter = st.sidebar.multiselect(
    "Select Experience Level:",
    options=data['Experience_Level'].unique(),
    default=data['Experience_Level'].unique(),
    key="experience_filter"
)

# BMI filter using a slider with a unique key
if 'BMI' in data.columns:
    bmi_min, bmi_max = st.sidebar.slider(
        "Select BMI Range:",
        min_value=float(data['BMI'].min()),
        max_value=float(data['BMI'].max()),
        value=(float(data['BMI'].min()), float(data['BMI'].max())),
        key="bmi_slider"
    )
else:
    st.error("BMI column is missing!")

# Filter the data
filtered_data = data[
    (data['Gender'].isin(gender_filter)) &
    (data['Experience_Level'].isin(experience_filter)) &
    (data['BMI'] >= bmi_min) & (data['BMI'] <= bmi_max)
]

# Display filtered data
st.subheader("Filtered Dataset")
st.dataframe(filtered_data)

# Key statistics
st.subheader("Key Statistics")
st.write("Total Members:", len(filtered_data))
st.write("Average Age:", filtered_data['Age'].mean())
st.write("Average BMI:", filtered_data['BMI'].mean())
st.write("Total Workout Hours:", filtered_data['Session_Duration (hours)'].sum())

# Chart 1: Total workout hours by experience level
st.subheader("Chart 1: Total Workout Hours by Experience Level")
if 'Experience_Level' in filtered_data.columns and 'Session_Duration (hours)' in filtered_data.columns:
    experience_summary = filtered_data.groupby('Experience_Level')['Session_Duration (hours)'].sum()
    st.bar_chart(experience_summary)

# Chart 2: BMI distribution
st.subheader("Chart 2: BMI Distribution")
if 'BMI' in filtered_data.columns:
    fig, ax = plt.subplots()
    sns.histplot(filtered_data['BMI'], kde=True, ax=ax)
    st.pyplot(fig)

# Chart 3: Calories burned by workout type
st.subheader("Chart 3: Calories Burned by Workout Type")
if 'Workout_Type' in filtered_data.columns and 'Calories_Burned' in filtered_data.columns:
    calories_summary = filtered_data.groupby('Workout_Type')['Calories_Burned'].sum()
    st.bar_chart(calories_summary)

# Chart 4: Average heart rate by gender
st.subheader("Chart 4: Average Heart Rate by Gender")
if 'Avg_BPM' in filtered_data.columns and 'Gender' in filtered_data.columns:
    fig, ax = plt.subplots()
    sns.boxplot(x='Gender', y='Avg_BPM', data=filtered_data, ax=ax)
    ax.set_title("Average Heart Rate Distribution by Gender")
    st.pyplot(fig)

# Interactive feature: Highlight top N members by Calories Burned
st.subheader("Top Members by Calories Burned (Bar Chart)")
top_n = st.slider("Select Number of Top Members:", min_value=1, max_value=20, value=5, key="top_n_slider")

if 'Calories_Burned' in filtered_data.columns and 'Age' in filtered_data.columns:
    top_members = filtered_data[['Age', 'Calories_Burned', 'Experience_Level', 'Workout_Type']].sort_values(
        by='Calories_Burned', ascending=False).head(top_n)

    # Plotting the bar chart
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(
        x='Calories_Burned',
        y='Age',
        hue='Workout_Type',
        data=top_members,
        palette='viridis',
        dodge=False,
        ax=ax
    )
    ax.set_title(f"Top {top_n} Members by Calories Burned", fontsize=14)
    ax.set_xlabel("Calories Burned")
    ax.set_ylabel("Age")
    st.pyplot(fig)

    # Display the data in a table format
    st.write("Detailed Data for Top Members:")
    st.table(top_members)

else:
    st.error("Columns 'Calories_Burned' or 'Age' are missing from the dataset!")

