import streamlit as st
import uuid
import pdf_processor
from dotenv import load_dotenv
import os

from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser




load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv('groqkey')


st.set_page_config(
    'PDF Insighter',page_icon = '📃'
)
if 'id' not in st.session_state:
    st.session_state.id = str(uuid.uuid4())

if 'db' not in st.session_state:
    st.session_state.db = ''

if 'file_uploaded' not in st.session_state:
    st.subheader('RAG Assistant for your uploaded pdf')
    st.info("💡 Pls upload your PDF to get start!")
    container = st.container(vertical_alignment = 'bottom',horizontal_alignment = 'right' ,height =200,border = False)
    file_upload = container.file_uploader(label = 'pdf_retriever',type = 'pdf',accept_multiple_files = True,label_visibility = 'collapsed')
    button = container.button('Process',type = 'primary')


    if button:
        with st.spinner('Pls wait creating a vector DB for you!',show_time = True):
            st.session_state.db = pdf_processor.embeding_vector_store(file_upload,st.session_state.id)
            st.session_state.file_uploaded = True
            st.rerun()

else:
    st.subheader('Chat with your uploaded pdf')

    if 'retriever' not in st.session_state and st.session_state.db is not None:
        st.session_state.retriever = st.session_state.db.as_retriever(
            search_type="mmr",
            search_kwargs={"k": 5, "fetch_k": 20}
        )
    
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",  
        temperature=0.5,
        max_tokens=512
    )

    qa_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
        Answer the following question using ONLY the information in the provided context. 
        If the answer cannot be found in the context, respond exactly: "I could not find this information in the provided document."

        Provide:
        1) A one-paragraph concise answer (directly answer the question).
        2) A short structured rationale (up to 4 bullet points) summarizing the key steps or evidence you used from the context — do NOT reveal internal chain-of-thought.
        3) Source references: list the chunk ids or page numbers (if present) you used.

        <context>
        {context}
        </context>

        Question:
        {question}

        Format your response exactly as:
        Answer:
        <your concise answer>

        Rationale:
        - step 1...
        - step 2...
    """
    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    rag_chain = (
        {
            "context": st.session_state.retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | qa_prompt
        | llm
        | StrOutputParser()
    )

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg['role']):
            st.write(msg['content']) 
    
    user_input = st.chat_input('Ask anything abt the file.....')

    if user_input:
        st.session_state.messages.append({'role':'user','content':user_input})

        with st.chat_message('user'):
            st.write(user_input) 
 
        answer = rag_chain.invoke(user_input)
        st.session_state.messages.append({'role':'assistant','content':answer})

        with st.chat_message('assistant'):
            st.write(answer)
