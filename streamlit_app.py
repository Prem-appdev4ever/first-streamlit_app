import streamlit
import pandas

streamlit.title('FAVOURITES')




streamlit.header ('🥣 🥗 🐔 🥑Breaky Menu🥣 🥗 🐔 🥑')
streamlit.text('🥗Bread & Omlette')
streamlit.text('🐔Hungry Jacks Burger & happy meal')
streamlit.text ('🥣Mc donalds haapy meal🥣')


streamlit.header('🥑Fruit Smoothie🥑')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
