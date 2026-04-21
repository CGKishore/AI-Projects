from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def build_rag_chain_from_docs(docs):

    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
        google_api_key=api_key
    )

    # Create vectorstore dynamically
    vectorstore = FAISS.from_documents(docs, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key,
        temperature=0
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a helpful assistant.
Use ONLY the context below.

Context:
{context}"""),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ])

    condense_prompt = ChatPromptTemplate.from_messages([
        ("system", "Rewrite follow-up question as standalone."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ])

    condense_chain = condense_prompt | llm | StrOutputParser()

    def get_standalone_question(input):
        if input.get("chat_history"):
            return condense_chain.invoke(input)
        return input["question"]

    rag_chain = (
        RunnablePassthrough.assign(
            standalone_question=RunnableLambda(get_standalone_question)
        )
        | RunnablePassthrough.assign(
            context=lambda x: format_docs(
                retriever.invoke(x["standalone_question"])
            )
        )
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain