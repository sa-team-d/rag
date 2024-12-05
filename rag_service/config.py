from llama_index.vector_stores.postgres import PGVectorStore
from llama_index.core.embeddings import resolve_embed_model

db_name = "vector_db"
host = "localhost"
password = "password"
port = "5432"
user = "superuser" 

vector_store = PGVectorStore.from_params(
    database=db_name,
    host=host,
    password=password,
    port=port,
    user=user,
    table_name="json_data",
    embed_dim=1024,  # openai embedding dimension
)

embed_model = resolve_embed_model("local:BAAI/bge-m3")
