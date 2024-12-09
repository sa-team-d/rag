# Group 5: RAG & Generative AI (Advanced AI Agent) 

**Project Title**: "Beyond Chatbots: Building a Generative AI Agent for Proactive Decision Support"

**Abstract**:  
This group will create an advanced AI agent based on Retrieval-Augmented Generation (RAG) and generative AI. The AI agent will assist users not only with queries but will also proactively help generate new KPIs, dashboards, and reports based on real-time data and system context.

**Repository Structure**:
```
./
├── 📂 rag_service
│   ├── 📄 config.py
│   ├── 📄 constants.py
│   ├── 📄 rag_lib.py
│   └── 📄 utility.py
├── 📄 data.ipynb
├── 📄 milestone1.ipynb
├── 📄 milestone2.ipynb
├── 📄 milestone3.ipynb
├── 📄 rag_notebook.ipynb
└── 📄 requirements.txt
```
In the folder `rag_service` you can find all the scripts for the final delivery: `rag_lib` is the core file where the model is uploaded, the embeddings are created, and the prompt is chosen based on the query. The available prompts can be found in `constants.py`.

The final notebook is `rag_notebook.ipynb`, where you can see the mocked GUI interaction with our RAG system (i.e. the function `rag_interaction` contained in `rag_lib.py`).

The notebook `data.ipynb` was used for the first development of the system to mock the knowledge base from the available data provided by professors.
