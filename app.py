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
# Load sample dataset from Plotly Express
# df = px.data.gapminder()

# # Create scatter plot using Plotly Express
# fig = px.scatter(
#     df.query("year==2007"),
#     x="gdpPercap",
#     y="lifeExp",
#     size="pop",
#     color="continent",
#     hover_name="country",
#     log_x=True,
#     size_max=60,
# )

# # Display the plot using Streamlit in one tab
# with st.expander("Plotly Chart", expanded=True):
#     # Use the Streamlit theme (default).
#     st.plotly_chart(fig, theme="streamlit", use_container_width=True)
