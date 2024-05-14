import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from gtts import gTTS
import io
from pydub import AudioSegment
from pydub.playback import play

# Function to convert text to speech and play it
def text_to_speech(text):
    tts = gTTS(text=text, lang='id')  # Using Indonesian language
    # Save the audio as bytes
    audio_bytes = io.BytesIO()
    tts.write_to_fp(audio_bytes)
    # Load the audio into Pygame mixer
    audio_bytes.seek(0)
    # Convert audio bytes to AudioSegment
    audio_segment = AudioSegment.from_file(audio_bytes, format="mp3")
    # Play the audio
    play(audio_segment)

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

