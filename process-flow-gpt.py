# Kllama Chat Bot for running open LLMs on local machine
import ollama
import streamlit as st
from datetime import datetime

# App title
st.title("ProcessFlow 💬: Your Local & Private GPT ✅")

# Message with timestamp | NOT Used
def format_message(sender, message, timestamp):
    return f"[{timestamp.strftime('%Y-%m-%d  %H:%M:%S')}] {sender}: {message}"

# Initialising the chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Clear Chat history
def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you?"}]

### App Sidebar Section Starts ###
with st.sidebar:
    st.title('💬 PF GPT Settings ⚙️')

    # Get user settings
    user_username = st.sidebar.text_input("Username", "Your Name")
    
    st.sidebar.markdown("---")

    ## Initialising models
    st.subheader('Open LLM Models')
    if "model" not in st.session_state:
        st.session_state["model"] = ""

    ## To select a LLM models from a list of available models
    models = [model["name"] for model in ollama.list()["models"]]
    st.session_state["model"] = st.selectbox("Choose a Model via Ollama Framework", models)
    model_chosen = st.session_state["model"]

   
    st.sidebar.markdown("---")
    st.subheader('Chat History')
    st.sidebar.button('Click to Clear Chat History', on_click=clear_chat_history)

    st.sidebar.markdown("---")
    st.sidebar.write(f"Logged in as: {user_username}")
    st.markdown('📖 Opensource Code and ReadMe available app via this [Github Repo](https://github.com/kunalsuri/ProcessFlowGPT/)!')
### App Sidebar Section Ends ###


## Generator funtion to show the generated result of LLMs
def model_result_generator():
    stream = ollama.chat(
        model=st.session_state["model"],
        messages=st.session_state["messages"],
        stream=True,
    )
    for chunk in stream:
        yield chunk["message"]["content"]

## Display chat messages from history on app rerun
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Show the selected Model
st.write("NOTE: You have selected the following LLM model via the Ollama Framework:  " + model_chosen)

# string_dialogue = "You only respond as 'Assistant. You do not pretend to be be a 'User' or respond as 'User'."
## Input for the promt
if prompt_input := st.chat_input("How may I assist you?"):

    string_dialogue = ""
    prompt = string_dialogue + prompt_input

    # add latest message to history in format {role, content}
    st.session_state["messages"].append({"role": "user", "content": prompt_input})
    
    # Show the chat history on the page
    with st.chat_message("user"):
        st.markdown(prompt_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking ..."):
            message = st.write_stream(model_result_generator())
            st.session_state["messages"].append({"role": "assistant", "content": message})

