
import  streamlit as st
from groq  import Groq
st.set_page_config(page_title= 'Gen Ai Project' , layout='wide')

st.title('Gen Ai Project Lamma 3.3')

st.subheader('By Pradosh')
user_input = st.text_area('Ask Any Question')
api_key = st.secrets['API_KEY']
client =  Groq(api_key= api_key)

def model_response(text: str , model_name = "llama-3.3-70b-versatile"):
    stream = client.chat.completions.create(messages= [
        {'role': 'system', 'content':'you are helpful in content creation '} ,
        {
            'role' : 'user',
            'content': text}
    ],
    
    model = model_name  , 
    stream = True)

    for chuck in stream:
        response =  chuck.choices[0].delta.content
        if response is not None: 
            yield response 
submit = st.button('Generate' , type= 'primary')

if submit:
    st.subheader('Generate data')
    st.write_stream(model_response(user_input))