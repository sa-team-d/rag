import os
from pathlib import Path
from llama_index.llms.ollama import Ollama
from llama_index.core import VectorStoreIndex
from llama_index.core.embeddings import resolve_embed_model
from llama_index.readers.json import JSONReader
from llama_index.core.node_parser import JSONNodeParser
from llama_index.readers.file import FlatReader

DATA_PATH = "./data/"

# setting up reader, parser, and llm
reader = JSONReader()
# parser = JSONNodeParser()     # if we want to split the documents into nodes
llm = Ollama(model="llama3.2", request_timeout=120.0)

# creating the documents out of the json files
documents = []
for filename in os.listdir(DATA_PATH):
    if filename.endswith(".json"):
        file_path = os.path.join(DATA_PATH, filename)
        # documents.extend(FlatReader().load_data(Path(file_path)))     # if we want to load the data to then split it into nodes
        documents.extend(reader.load_data(input_file=file_path))

# nodes = parser.get_nodes_from_documents(documents)            # if we want to split documents into nodes

embed_model = resolve_embed_model("local:BAAI/bge-m3")
vector_index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
query_engine = vector_index.as_query_engine(llm=llm)

result = query_engine.query("is the machine idle or working for the most part?")
print(result)
