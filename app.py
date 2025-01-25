import streamlit as st
import openai

# Authenticate
openai.api_key = st.secrets['api_key']

# Title
st.title("ChatBot")

st.header("Getting you deliciously fed!")

# Input Text Area
Instruction = st.text_area(
    "Tell me what you want to eat, and I'll help you decide! Specify: Breakfast, Lunch, or Dinner"
)

# Check if the input is valid and below 1000 characters
if Instruction:  # Ensure input is not empty
    if len(Instruction) < 1000:
        if st.button("Show Options"):
            try:
                # Call OpenAI API using ChatCompletion
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",  # Use an appropriate chat model
                    messages=[
                        {"role": "system", "content": "You are a helpful personal chef."},
                        {"role": "user", "content": f"Give me food suggestions based on: {Instruction}"}
                    ],
                    temperature=0,
                    max_tokens=1000
                )
                output = response['choices'][0]['message']['content'].strip()
                st.info(output)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Input too large! Write less than 1000 characters and try again.")
else:
    st.warning("Please enter a prompt to get started.")