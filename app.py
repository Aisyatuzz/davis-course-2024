import pandas as pd
import streamlit as st

# reading the database
data = pd.read_csv("https://raw.githubusercontent.com/Aisyatuzz/davis-course-2024/main/tips.csv")

# printing the top 10 rows
display(data.head(10))
