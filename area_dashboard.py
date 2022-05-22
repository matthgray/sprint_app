# needed packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import numpy as np
import time
# read data

agile_df = pd.read_csv("Torch_mock_data.csv")
st.write("Sprint Snapshot Dashboard")
st.markdown('''DASHBOARDS FOR SOFTWARE AREAS''')

st.dataframe(agile_df)
# filters
sorted_Area = sorted(agile_df.Developer_Area.unique())
selected_from_area =st.sidebar.multiselect('Filter by functional_area',sorted_Area,
default=['Login'])
# filter for sprint
sorted_sprint = sorted(agile_df.Sprint.unique())
selected_from_sprint = st.sidebar.multiselect('Filter by sprint',sorted_sprint,default=['Sprint 22'])

# filter for
# a data frame to graph based on the users selection
selected_area =agile_df[(agile_df.Developer_Area.isin(selected_from_area))]
selected_sprint =agile_df[(agile_df.Sprint.isin(selected_from_sprint))]


# figure about stories to defect ratio
area_fig = px.bar(selected_area, x='Type',color ='Developer_Area',barmode="group",title ="Story to defect ratio by area")
area_fig
# visual for sprint data
sprint_fig = px.treemap(selected_sprint, path=['Sprint','Developer_Area'], values='Points',color='Points',title = "Developed area with the most points in this sprint")
sprint_fig

sprint_priority_fig = px.bar(selected_sprint, x='Developer_Area', y='Points',color ='Priority',barmode="group",title="Developed area by priority")
sprint_priority_fig
#df=selected_area["Points"].mode()
#st.metric(label="Average", value=agile_df)


#st.write(sorted_Area["Points"].mean())
