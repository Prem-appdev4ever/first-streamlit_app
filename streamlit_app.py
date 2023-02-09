import streamlit
import pandas

streamlit.title('FAVOURITES')




streamlit.header ('🥣 🥗 🐔 Breaky Menu🥣 🥗 🐔')


streamlit.text('🥗Bread & Omlette')
streamlit.text('🐔Hungry Jacks Burger & happy meal')
streamlit.text ('🥣Mc donalds haapy meal🥣')




streamlit.header('🥑Fruit Smoothie🥑')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect ("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberrries'])
streamlit.dataframe(my_fruit_list)
