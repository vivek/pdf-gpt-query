# PDF GPT query interface
Tool to search PDF documents using OpenAI and FAISS (Facebook AI Similarity Search).

- Recursively extract text from PDF documents from the given directory
- Load and split PDF document in to text chunks using [PyPDFLoader](https://python.langchain.com/docs/modules/data_connection/document_loaders/how_to/pdf#using-pypdf) langchain document loader
- Embed text chunks using OpenAI API embedding 
- Store embeddings in FAISS index
- Use retrieval to find relevant text chunks for a given query using OpenAI API LLM

## Install dependencies

```bash
## Create conda environment using environment.yml
conda env create -f ./environment.yml
conda activate pdf-gpt-query
```

## Run
Use default PDF in `data` directory:

```bash
OPENAI_API_KEY="..." python main.py 
```

Use a directory with PDFs (it will recursively find all PDFs in the directory, can be slow):

```bash
OPENAI_API_KEY="..." python main.py ~/Documents
```
