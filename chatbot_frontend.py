# ================================================================
# FILENAME: chatbot_frontend.py
# DESCRIPTION: Streamlit front-end for the RAG chatbot.
#
# This file creates a one-page chat application that interacts with
# the user. It imports the core logic from `query_data_streamlit.py` to
# retrieve and generate responses from the local ChromaDB.
#
# To run this script, make sure you are in your virtual environment
# and have Streamlit installed.
# Execute: streamlit run chatbot_frontend.py
#
# The "missing ScriptRunContext" warning is often a sign that a Streamlit
# function is being called outside of the main Streamlit thread.
# This can happen if a library, like parts of LangChain, is running in
# a separate thread. A common cause is also running the script with
# `python chatbot_frontend.py` instead of `streamlit run chatbot_frontend.py`.
# This code is structured to avoid such issues, but it's important
# to ensure the correct command is used.
# ================================================================

import streamlit as st
import sys
import os
from query_data_streamlit import get_bot_response

# A workaround to import from the parent directory.
# This adds the project root to the Python path.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# We will assume that query_data_streamlit has been refactored to contain a function.
# The user must make a small change to query_data_streamlit.py to enable this.
# See the 'query_data_streamlit.py' section below for details.
#try:
    # Corrected import statement to match the new filename
#    from query_data_streamlit import get_bot_response
#except ImportError:
#    st.error("Could not import 'get_bot_response' from query_data_streamlit.py. "
#            "Please ensure 'query_data_streamlit.py' is in the same directory "
#             "and has been modified as instructed below.")
#    st.stop()


def main():
    """
    Main function to run the Streamlit application.
    """
    st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")

    st.title("Argus Safety ChatBot")
    st.caption("Chat with ArgusSafety Guides and Associated Documents")

    # Initialize chat history in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Ask a question about the documents..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            with st.spinner("Generating response..."):
                # Call the refactored function from query_data_streamlit.py
                response = get_bot_response(prompt)
                st.markdown(response)

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
