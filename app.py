import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

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
# Create scatter plot using Plotly Express
fig = px.scatter(
    data,
    x="day",
    y="tip",
    color="size",
    size="total_bill",
    color_continuous_scale="reds",
)

# Display the plot using Streamlit in one tab
with st.expander("Plotly Chart", expanded=True):
    # Use the Streamlit theme (default).
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
