import pandas as pd
import streamlit as st
from helper import main

df = pd.read_csv("customer_survey.csv")

st.title("Survey Analysis")

preview = st.toggle('Dataset Preview')

if preview:
    st.dataframe(df.head())

# query = st.text_input(label="Enter your query: ")

# if query:
#     output = main(query, df)  
#     st.header("Output:")
#     st.markdown(output)



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if query := st.chat_input("Enter your query"):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": query})
    # Display user message
    with st.chat_message("user"):
        st.markdown(query)

    response = main(query, df)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})