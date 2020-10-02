import streamlit as st
import numpy as np
import pandas as pd
#import time
from PIL import Image

st.title("My Fifth WebApp")
st.header("COP4813")
st.subheader("Learning Streamlit")

#st.text("Basics")
#st.write("Tutorial")

table1 = {
    "first_column" : [1,2,3,4],
    "second_column": [1,4,9,16]
}

st.write(pd.DataFrame(table1))

chart_data = pd.DataFrame(
    np.random.rand(20,3),
    columns = ["A","B","C"]
)

chart_data

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.array([[25.76, -80.4],]),
    columns=['lat','lon']
)

st.map(map_data)

st.write("Congratulations")
selection = st.checkbox("Cong")
if selection:
    st.success("Congrats!")

st.write("Warning")
selection = st.checkbox("Warn")
if selection:
    st.warning("Uh oh!")

st.write("Error")
selection = st.checkbox("Err")
if selection:
    st.error("No! Try again!")

options = st.selectbox("What is your major?", ["IT", "CS", "Cyber Security"])

st.write("You selected {}.".format(options))

options2 = st.sidebar.selectbox("What year are you in the program?",
                                ["", "1st", "2nd", "3rd", "4th", "5th", "6th"])

#latest_iteration = st.empty()

#bar = st.progress(0)

#for i in range(100):
#    latest_iteration.text(f'Iteration {i+1}')
#    bar.progress(i+1)
#    time.sleep(0.1)

image1 = Image.open('mordhau.png')

st.image(image1, caption="Gigahau",use_column_width=True)