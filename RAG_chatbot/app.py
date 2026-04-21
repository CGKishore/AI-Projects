import streamlit as st
import tempfile
from langchain_core.messages import HumanMessage, AIMessage
from rag_chain import build_rag_chain_from_docs
from ingest import process_uploaded_file

st.set_page_config(page_title="Document Chatbot")
st.title("Upload Document & Chat")

# Upload file
uploaded_file = st.file_uploader("Upload your document", type=["pdf"])

if uploaded_file is not None:
    
    if "chain" not in st.session_state:
        with st.spinner("Processing document..."):
            docs = process_uploaded_file(uploaded_file)
            st.session_state.chain = build_rag_chain_from_docs(docs)
        st.success("Document processed! Ask questions now.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
if "chain" in st.session_state:
    if prompt := st.chat_input("Ask about the document..."):
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = st.session_state.chain.invoke({
                    "question": prompt,
                    "chat_history": st.session_state.chat_history
                })
            st.write(answer)

        st.session_state.chat_history.extend([
            HumanMessage(content=prompt),
            AIMessage(content=answer)
        ])

        st.session_state.messages.append({"role": "assistant", "content": answer})