import pandas as pd
import streamlit as st

# reading the database
data = pd.read_csv

# printing the top 10 rows
display(data.head(10))
