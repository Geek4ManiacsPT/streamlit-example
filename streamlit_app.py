import streamlit as st
import pandas as pd
import matplotlib as plt
import seaborn as sns
import plotly.express as px
import pydeck as pdk

# Function to load data (you might need to adjust the path)
def load_data():
    data = pd.read_excel('campanha_marketing_superfruits_Limpa.xlsx')
    # Add any data preprocessing here
    return data

# Load the data
data = load_data()

# Setting up the layout
st.title("Marketing Campaign Analysis Dashboard")

# Top Line Visuals
st.header("Top Line Visuals")



# Bar Chart for Age Group
st.subheader("Visitor Distribution by Age Group")
age_group_data = data['age'].value_counts()
fig_age = px.bar(age_group_data, x=age_group_data.index, y=age_group_data.values, labels={'x':'Age Group', 'y':'Number of Visitors'})
st.plotly_chart(fig_age)

# Line Chart for Interactions Over Time
st.subheader("Interactions Over Time")
# You might need to preprocess the data to get the desired format
# interaction_time_data = ...
# fig_interaction_time = ...
# st.plotly_chart(fig_interaction_time)

# Bottom Line Visuals
st.header("Bottom Line Visuals")

# Pie Chart for Source Channels
st.subheader("Visitor Sources")
source_data = data['source_channel'].value_counts()
fig_source = px.pie(source_data, values=source_data.values, names=source_data.index)
st.plotly_chart(fig_source)

# Interactive Table
st.subheader("Detailed Data")
st.dataframe(data)  # You can add more interactivity using st.table or st.write

# Bar Chart for Operating Systems
st.subheader("Operating System Usage Among Visitors")
os_data = data['operating_system'].value_counts()
fig_os = px.bar(os_data, x=os_data.index, y=os_data.values, labels={'x':'Operating System', 'y':'Number of Visitors'})
st.plotly_chart(fig_os)


