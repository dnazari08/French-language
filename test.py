import streamlit as st

st.title("French Language Self Assessment Tool")
st.header('Question 1')
st.subheader('Part 1')
st.text('This assessment tool helps students understand their level of profeciency in different skill sets')
st.caption('caption')
st.code('for i in range(20): print i')
st.markdown('# *heading 1*')



btn = st.button('back')
if btn:
    st.write('I was clicked')

#with open('image.png', 'rb') as file: 
    #st.download_button(label='Download Image', data=file, file_name = 'image.png', mime='png')

ch = st.checkbox('I agree with the terms and conditions')
if ch:
    st.write('Thanks for agreeing')

st.radio('choose a category', ('Beginner', 'Intermediate', 'Advanced'))

st.selectbox('Choose a category', ['Beginner', 'Intermediate', 'Advanced'])
st.multiselect('Choose a category', ['Beginner', 'Intermediate', 'Advanced'])
st.slider('Choose a range', 0, 100)
st.select_slider('Choose a range',['Beginner', 'Intermediate', 'Advanced'])


st.text_input('Your name here')
st.text_area('your message')
st.number_input('Your age')
st.time_input('time')
st.date_input('Date')
st.color_picker('Color')
st.file_uploader('Your file')
