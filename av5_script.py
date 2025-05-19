from langchain_ollama import OllamaEmbeddings
from langchain_ollama.llms import OllamaLLM
from  langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

modelo = OllamaLLM(model="phi3:mini")
prompt = "O que é IA?"

pdf = "C:/Users/maria/OneDrive/Área de Trabalho/IFRN/TASI 1/av5_tasi1/IA_RedesNeurais.pdf"
loader = PyPDFLoader(pdf)
paginas = loader.load_and_split()
paginas = paginas[:1]

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=50,
    length_function=len,
)
texts = text_splitter.split_documents(paginas)

vectordb = FAISS.from_documents(texts, OllamaEmbeddings(model="nomic-embed-text"))

retriever = vectordb.as_retriever(search_kwargs={"k": 5})

qa_chain = RetrievalQA.from_chain_type(llm=modelo, retriever=retriever, chain_type="stuff")

resultado = qa_chain.invoke(prompt)
print(resultado)