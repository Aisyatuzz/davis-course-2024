import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# reading the database
data = pd.read_csv("https://raw.githubusercontent.com/Aisyatuzz/davis-course-2024/main/tips.csv")

# Scatter plot with day against tip
plt.scatter(data['day'], data['tip'])

# Adding Title to the Plot
plt.title("Scatter Plot")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

# Displaying the plot in Streamlit
st.pyplot()
