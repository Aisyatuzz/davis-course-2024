import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#1
# reading the database
data = pd.read_csv("https://raw.githubusercontent.com/Aisyatuzz/davis-course-2024/main/tips.csv")

# Create a scatter plot
fig, ax = plt.subplots()
ax.scatter(data['day'], data['tip'])

# Adding Title to the Plot
ax.set_title("Scatter Plot")

# Setting the X and Y labels
ax.set_xlabel('Day')
ax.set_ylabel('Tip')

# Display the plot in Streamlit
st.pyplot(fig)
