import streamlit as st
import openai

# Get gpt-3 key
f = open("key.txt", "r")
key = f.read()
f.close()
openai.api_key = key

f = open("prompt.txt", "r")
prompt = f.read()
f.close()


st.subheader('Use natural language describe the excel macro you want and get the code in return')

example = 'Ex: Create a macro that list all sheets in the workbook'
user_input = st.text_input("Describe your macro here", example)

if user_input and user_input != example:
    with st.spinner('Loading...'):

        new_prompt = f"{prompt}\n\nQ:{user_input}\n"

        response = openai.Completion.create(engine='davinci',
                                            prompt=new_prompt,
                                            stop='###',
                                            temperature=0,
                                            top_p=1,
                                            frequency_penalty=0,
                                            presence_penalty=0,
                                            max_tokens=175
                                            )
        st.text(response.choices[0].text.replace('A: ', ''))
        print(response.choices[0].text.replace('A: ', ''))