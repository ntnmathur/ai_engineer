############################## Data Ingestion ##############################


############### From Directory

from llama_index.core import SimpleDirectoryReader

documents = SimpleDirectoryReader("/Users/ntnmathur/github/ai_engineer/llamaindex_tutorials/data/").load_data()
print(documents)


############### From Input text

from llama_index.core import Document
doc = Document(text="text")
print(doc)


############### From Database
# from llama_index.core import download_loader
# from llama_index.readers.database import DatabaseReader

# reader = DatabaseReader(
#     scheme=os.getenv("DB_SCHEME"),
#     host=os.getenv("DB_HOST"),
#     port=os.getenv("DB_PORT"),
#     user=os.getenv("DB_USER"),
#     password=os.getenv("DB_PASS"),
#     dbname=os.getenv("DB_NAME"),
# )

# query = "SELECT * FROM users"
# documents = reader.load_data(query=query)

############################## Data Transformation ##############################
# High level API
from llama_index.core import VectorStoreIndex
vector_index = VectorStoreIndex.from_documents(documents)
vector_index.as_query_engine()

from llama_index.core.node_parser import SentenceSplitter
text_splitter = SentenceSplitter(chunk_size=512, chunk_overlap=10)

# global
from llama_index.core import Settings
Settings.text_splitter = text_splitter
# per-index
index = VectorStoreIndex.from_documents(
    documents, transformations=[text_splitter]
)

# Low level API