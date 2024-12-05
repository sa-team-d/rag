import json 
from pathlib import Path
from tempfile import NamedTemporaryFile

from llama_index.core.node_parser import TokenTextSplitter
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.llms.ollama import Ollama
from llama_index.readers.file import FlatReader

from rag_service.constants import CHAT_PROMPT
from rag_service.config import vector_store, embed_model
from rag_service.utility import VectorDBRetriever


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

    text_splitter = TokenTextSplitter(
        # separator=" ", 
        chunk_size=512, 
        chunk_overlap=128
    )

    transformations = [
    text_splitter,
    ]

    pipeline = IngestionPipeline(
        transformations=transformations
    )

    nodes = pipeline.run(
        documents=documents,
        in_place=True,
        show_progress=True,
    )

    for node in nodes:
        node_embedding = embed_model.get_text_embedding(
            node.get_content(metadata_mode="all")
        )
        node.embedding = node_embedding

    vector_store.add(nodes)

    retriever = VectorDBRetriever(
        query_mode="default", similarity_top_k=2
    )

    query_engine = RetrieverQueryEngine.from_args(retriever, llm=llm)
    response = query_engine.query(CHAT_PROMPT + "\n" + query)
    
    return response