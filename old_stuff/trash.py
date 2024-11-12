def retrieve_data(query):
    # right now this function doesn't use the query, but it could be used to filter the data later...
    with open(DATA_PATH, 'r') as file:
        file_content = file.read()
    return file_content
    
# Step 3: Define the RAG pipeline with retrieval and generation
def rag_pipeline(query):
    # Retrieve relevant documents
    # retrieved_docs = [retrieve_data(query)]
    data = ""
    data = retrieve_data(query)
    # Build the prompt with the retrieved documents
    prompt = PROMPT + data + query
    # print(prompt)
    # Generate the response with Ollama  
    response = llm.complete(prompt)


    def retrieve_data(query):
    # Aggregate data from all JSON files in the specified directory
    data_content = ""
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".json"):
            file_path = os.path.join(DATA_DIR, filename)
            with open(file_path, 'r') as file:
                file_content = file.read()
                data_content += file_content + "\n"  # Append content from each file
    return data_content

# Define the RAG pipeline with retrieval and generation
def rag_pipeline(query):
    # Retrieve relevant documents from all JSON files
    data = retrieve_data(query)
    
    # Build the prompt with the retrieved documents
    prompt = PROMPT + data + query
    # Generate the response with Ollama
    response = llm.complete(prompt)
    return response  # Extracting the generated answer text


PROMPT = """
Data Structure Overview

Machines
The dataset includes data from 16 distinct machines used in various manufacturing processes. Machines are categorized as follows:

Metal Cutting Machines
Large Capacity Cutting Machine 1
Large Capacity Cutting Machine 2
Medium Capacity Cutting Machine 1
Medium Capacity Cutting Machine 2
Medium Capacity Cutting Machine 3
Low Capacity Cutting Machine 1

Laser Welding Machines
Laser Welding Machine 1
Laser Welding Machine 2

Assembly Machines
Assembly Machine 1
Assembly Machine 2
Assembly Machine 3

Testing Machines
Testing Machine 1
Testing Machine 2
Testing Machine 3

Other Machines
Riveting Machine
Laser Cutter

Key Performance Indicators (KPIs)
The data captures 12 KPIs, classified by their focus area:

Time-Related KPIs
working_time: seconds of active machine operation
idle_time: seconds when machine is idle
offline_time: seconds when machine is offline

Energy and Cost-Related KPIs
consumption: total energy consumption (kWh)
power: energy power rating (kW)
cost: energy cost (euro per kWh)
consumption_working: energy consumed during active operation (kWh)
consumption_idle: energy consumed while idle (kWh)

Production-Related KPIs
cycles: total production cycles
good_cycles: number of successful cycles
bad_cycles: number of defective cycles
average_cycle_time: average time per cycle (seconds)
"""

#embed_model = resolve_embed_model('local:sentence-transformers/all-MiniLM-L6-v2')

# embed_model = resolve_embed_model('local:sentence-transformers/all-mpnet-base-v2')