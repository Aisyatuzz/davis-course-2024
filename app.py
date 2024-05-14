import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import os

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])


st.bar_chart(chart_data)



# Initialize connection.
# conn = st.connection('mysql', type='sql', username=st.secrets["DB_USER"], password=st.secrets["DB_PASS"], host=st.secrets["HOST"], database=st.secrets["DB"])
# conn = st.connection(**st.secrets.db_credentials)
conn = st.connection("mydb", type="sql", autocommit=True)
# st.write(st.secrets["connections.mydb"]["username"])
# Perform query.
df = conn.query('SELECT EnglishPromotionName, StartDate, EndDate, MaxQty from dimpromotion limit 10;', ttl=600)

st.table(df)
# Print results.
# for row in df.itertuples():
#     st.write(f"{row.EnglishPromotionName} , {row.MaxQty} ")

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

#3
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

