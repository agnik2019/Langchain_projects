# integrate our code openAi api
import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain


import streamlit as st


os.environ['OPENAI_API_KEY'] = openai_key

# steamlit framework
st.title("Analyzing Github Repo")
input_text = st.text_input("Write the user name")


# Prompt Template
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)


# OPENAI LLMS
llm = OpenAI(temperature=0.8)


chain = LLMChain(llm = llm, prompt=first_input_prompt,verbose=True )

if input_text:
    st.write(llm(chain.run(input_text)))
