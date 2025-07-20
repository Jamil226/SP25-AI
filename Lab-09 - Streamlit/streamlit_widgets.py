import streamlit as st 
import os 

st.title('Input Widgets')

# Button
st.header('Button')
button = st.button('Button') # return true or False
if button:
    st.write('You pressed on Button')

# Checkbox (Toggle Button)
st.header('Checkbox')
checkbox = st.checkbox("Do you want to agree ?") # return bool (True or False)
if checkbox:
    st.write('You checked the box')
    
else:
    st.write('You Unchecked')


st.header('Radio Button')
# Radio Button
# from list of value, radio button give use to select one 
# value
options = ("India","USA","UK","Australia")
radio_button =st.radio("What is your Favorite Country",
                       options,index=2) # return an elemetn in a list/tuple
st.write('You Favourite country is ',radio_button)


# Select Box 
st.header('Select Box')
options = ('Email','Phone','WhatsApp')
select_box = st.selectbox('How would you like to contact',
                          options,index=1)
st.write('Your prefered mode of communication is ',
         select_box)

# Slider
slider_range = st.slider('How Old are you ?',
                         min_value=1,
                         max_value=100,
                         step=1,value=20)
st.write('You age is ',slider_range)

# Text Inputs
name = st.text_input('Enter you Name')
st.write('You name is ',name)

age = st.number_input('Enter you age',min_value=1,
                      max_value=100,step=1,value=25)
st.write('You age is ',age)

# Upload File
st.header('File Upload')
uploaded_file = st.file_uploader('Choose a File')

if uploaded_file is not None:
    st.success('File uploaded sucessfully')
    details = {'filename':uploaded_file.name,
               'filetype':uploaded_file.type,
               'filesize (bytes)':uploaded_file.size}
    
    st.json(details)
    
    # save the file
    path = os.path.join('./upload',uploaded_file.name)
    with open(path,mode='wb') as f:
        f.write(uploaded_file.getbuffer())
        st.success('File Saved successfully')
        
    

