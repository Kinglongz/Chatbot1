import streamlit as st
import openai

#Authenticate
openai.api_key = st.secrets['api_key']

#Title
st.title("ChatBot")

st.header("getting you deliciously fed!")

Instruction = st.text_area(
    "Tell me what you want to eat and I'll help you decide! Specify: Breakfast, Lunch, or Dinner"
)

if len(instructions) < 1000:
    if st.button("Show Options"):
        response = openai.Completions.create(
            model = "text-davinci-001",
            prompt = "Act like my personal chef and give me food suggestions based on the following prompt: " + prompt,
            temperature = 0,
            max_tokens = 1000
        )
        output = response.choices[0].text
        st.info(output)

else:
    st.warning(
        "Input too large! Write less than 1000 words and try again"
    )