📄 RAG Resume Chatbot (Streamlit + LangChain + Gemini)

An AI-powered chatbot that allows users to upload a PDF document (like a resume) and ask questions about its content using a Retrieval-Augmented Generation (RAG) pipeline.

🚀 Features
📂 Upload PDF documents
✂️ Automatic text chunking
🔎 Semantic search using FAISS vector database
🤖 Context-aware responses using Gemini LLM
💬 Chat interface with memory (conversation history)
⚡ Fast and interactive UI with Streamlit
🧠 Tech Stack
Python
Streamlit
LangChain
Google Gemini (Generative AI)
FAISS (Vector Database)
PyPDFLoader
🏗️ Project Structure
AI-Projects/
│
└── RAG_chatbot/
    ├── app.py               # Streamlit UI
    ├── ingest.py            # PDF loading & chunking
    ├── rag_chain.py         # RAG pipeline (LangChain)
    ├── requirements.txt
    ├── .gitignore
    └── README.md
⚙️ How It Works
User uploads a PDF
Document is split into smaller chunks
Chunks are converted into embeddings
Stored in FAISS vector database
User asks a question
Relevant chunks are retrieved
Gemini LLM generates answer using context
🔧 Installation & Setup
1. Clone the repository
git clone https://github.com/CGKishore/AI-Projects.git
cd AI-Projects/RAG_chatbot
2. Install dependencies
pip install -r requirements.txt
3. Setup environment variables

Create a .env file:

GOOGLE_API_KEY=your_api_key_here

⚠️ Do NOT upload this file to GitHub

4. Run the application
streamlit run app.py
💡 Example Use Cases
Chat with resumes
Analyze research papers
Query PDFs like reports or notes
Build document-based Q&A systems
🔒 Security Note
API keys are stored in .env file
.env is excluded using .gitignore
Never expose API keys publicly
📈 Future Improvements
Support multiple documents
Add document upload history
Improve UI/UX
Deploy on cloud (Streamlit Cloud / Render)
Add source citation in answers
👨‍💻 Author

Kishore
MCA Student | AI & Data Science Enthusiast

⭐ If you like this project

Give it a ⭐ on GitHub!
