import json 
from pathlib import Path
from tempfile import NamedTemporaryFile

from llama_index.core import VectorStoreIndex
from llama_index.llms.ollama import Ollama
from llama_index.readers.file import FlatReader

from rag_service.constants import CHAT_PROMPT
from rag_service.config import embed_model


def rag_chat(response_data_list, query):
    """
    @param vector_store vector store to be used for the RAG system
    @param documents list of documents to be ingested (each in json format)
    @param query query to be answered

    @return response to the query
    """

    llm = Ollama(model="llama3.2", request_timeout=180.0) 

    documents = []
    for response_data in response_data_list:
        # Create a temporary file for each JSON data
        with NamedTemporaryFile(mode='w+', suffix=".json", delete=True) as temp_file:
            json.dump(response_data, temp_file)  # Write JSON data to the temp file
            temp_file.flush()  # Ensure data is written to disk
            temp_path = Path(temp_file.name)  # Get the path of the temp file

            # Load data using the temporary file's path
            documents.extend(FlatReader().load_data(temp_path))


    vector_index = VectorStoreIndex.from_documents(documents, embed_model=embed_model, show_progress=True)

    query_engine = vector_index.as_query_engine(llm=llm, verbose=True, similarity_top_k=2)

    response = query_engine.query(CHAT_PROMPT + "\n" + query)
    
    return response