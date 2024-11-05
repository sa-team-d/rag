from llama_index.llms.ollama import Ollama
from llama_index.core import VectorStoreIndex
from llama_index.core.embeddings import resolve_embed_model
from llama_index.readers.json import JSONReader


reader = JSONReader()
llm = Ollama(model="llama3.2", request_timeout=120.0)

documents = reader.load_data(input_file="./data/machine_data.json")
embed_model = resolve_embed_model("local:BAAI/bge-m3")
vector_index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
query_engine = vector_index.as_query_engine(llm=llm)

result = query_engine.query("is the machine idle or working for the most part?")
print(result)
