import streamlit as st
from PIL import Image

image = Image.open('static/me.JPG')
image = image.rotate(270)
image2 = Image.open('static/me2.jpg')
image3 = Image.open('static/me3.jpg')



def home_page():
    st.title("🎉 Hey there, I'm Arjun! 🚀 ")
    st.write("\n")
    myImg,myDesc = st.columns(2)
    with myImg:
        st.image(image2)
    with myDesc:
        st.write("""

    I'm a final-year student at SRM Easwari Engineering College, where I'm on a thrilling journey pursuing my B.Tech in Artificial Intelligence and Data Science 🤖📊.

    My love story with programming began when I first laid eyes on Python during my 12th grade, and it was love at first code! 💻❤️

    As I dove deeper into Python's vast universe, I stumbled upon the enchanting realms of Data Science, Machine Learning, and even web development using Python. 🌐🤯

    Learning about Data Science and Django was like discovering hidden treasures, and I fell in love with Python all over again! 💖✨

    Currently, I'm on an exciting quest to delve into the world of AI models, researching Machine Learning Algorithms, and crafting scalable backends using Python frameworks. 🧠🌟

    Oh, and did I mention that I've also mastered React to tame the wild frontends? 🚀🎨

    Join me on this epic journey through the digital cosmos as I continue to explore, innovate, and create! 🌌🚀🔥""")
    
    st.caption('👈 have a look at other pages')