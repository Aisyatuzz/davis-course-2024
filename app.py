import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Menampilkan teks 
st.subheader("Hello ^~^")
st.subheader("")
st.write("My Name is Aisyatuz")

#1
# reading the database
data = pd.read_csv("https://raw.githubusercontent.com/Aisyatuzz/davis-course-2024/main/tips.csv")

# printing the top 10 rows
st.write(data.head(10))

# Scatter plot with day against tip
fig, ax = plt.subplots()
scatter = ax.scatter(data['day'], data['tip'], c=data['size'], s=data['total_bill'])

# Adding Title to the Plot
plt.title("Scatter Plot")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

plt.colorbar(scatter)

st.pyplot(fig)

#2
# Select the data for each group
male_data = data[data['sex'] == 'Male']['total_bill']
female_data = data[data['sex'] == 'Female']['total_bill']

# Create a figure using Plotly Express
fig = px.histogram(data, x='total_bill', color='sex', marginal='rug')

# Plot!
st.plotly_chart(fig, use_container_width=True)
