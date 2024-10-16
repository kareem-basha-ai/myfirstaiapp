from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import streamlit as st
import os

os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']

# Create prompt template for generating tweets

tweet_template = "Give me {number} tweets on {topic}"

tweet_prompt = PromptTemplate(template = tweet_template, input_variables = ['number', 'topic'])

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")


# Create LLM chain using the prompt template and model
tweet_chain = tweet_prompt | gemini_model


import streamlit as st
# Inject custom CSS for page border
page_border_style = """
    <style>
        /* Add border around the entire page */
        .main {
            border: 5px solid black; /* Adjust thickness and color here */
            padding: 20px; /* Optional: Add padding inside the border */
            margin: 20px; /* Optional: Add margin outside the border */
        }
        .stApp {
            background-color: #f0f0f5; /* Optional: Change background color */
        }
    </style>
"""

# Inject the CSS into Streamlit app
st.markdown(page_border_style, unsafe_allow_html=True)
# Your app content
st.title("Streamlit Page with Border")
st.write("This page has a custom border using injected CSS.")
st.header("Tweet Generator-BAASHI")

st.subheader("Generate tweets using Generative AI")

topic = st.text_input("Topic")

number = st.number_input("Number of tweets", min_value = 1, max_value = 10, value = 1, step = 1)

if st.button("Generate"):
    tweets = tweet_chain.invoke({"number" : number, "topic" : topic})
    st.write(tweets.content)
    
