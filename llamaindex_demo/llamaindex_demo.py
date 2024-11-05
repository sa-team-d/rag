import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, ServiceContext
from llama_index.llms.ollama import Ollama
from llama_index.core import Settings
from llama_index.embeddings.ollama import OllamaEmbedding

# Set up Ollama
llm = Ollama(model="phi3")
Settings.llm = llm
embed_model = OllamaEmbedding(model_name="snowflake-arctic-embed")
Settings.embed_model = embed_model

# Define the path to your document directory
directory_path = '../kb'

# Load documents
documents = SimpleDirectoryReader(directory_path).load_data()

# Create index
index = VectorStoreIndex.from_documents(documents, show_progress=True)

# Create query engine
query_engine = index.as_query_engine(llm=llm)

# Perform a query
response = query_engine.query("What's the idle time of Large Capacity Cutting Machine 1?")
print(response)