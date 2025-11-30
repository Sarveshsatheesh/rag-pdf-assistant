from langchain_community.document_loaders import PyPDFLoader
import tempfile
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
import os



load_dotenv()
pinecone_api_key = os.getenv('pinecone_api_key')


##function
def get_text_frm_pdf(clubbed_file_path):
    all_doc = []

    for single_path in clubbed_file_path:
        with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf") as tmp:
            tmp.write(single_path.getvalue())
            tmp_file_path = tmp.name

        loader = PyPDFLoader(tmp_file_path)
        doc = loader.load()
        all_doc.extend(doc)
    
    return all_doc

def embeding_vector_store(file,id):
    clubed_document = get_text_frm_pdf(file)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000,chunk_overlap= 200,separators=["\n\n", "\n", ".", " "])
    chunks = text_splitter.split_documents(clubed_document)

    embeddings = HuggingFaceEmbeddings(
        model_name = 'sentence-transformers/all-MiniLM-L6-v2',
        model_kwargs = {'device': 'cpu'}
    )
    db = PineconeVectorStore.from_documents(
        documents = chunks,
        index_name = 'ragminiproj',
        embedding = embeddings,
        namespace = id

    )

    return db


