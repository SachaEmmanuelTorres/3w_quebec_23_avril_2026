import marimo
import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

__generated_with = "0.23.3"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def _(mo):
    mo.md("# 🚀 Hermes RAG - Assistant Documentaire")
    return


@app.cell
def _():
    # Configuration des accès
    OLLAMA_URL = "http://ollama:11434"
    EMBED_MODEL = "mxbai-embed-large"
    LLM_MODEL = "hermes3"
    PERSIST_DIRECTORY = "/app/knowledge"
    return EMBED_MODEL, LLM_MODEL, OLLAMA_URL, PERSIST_DIRECTORY


@app.cell
def _(EMBED_MODEL, OLLAMA_URL, PERSIST_DIRECTORY):
    # Initialisation des embeddings et de la base vectorielle
    embeddings = OllamaEmbeddings(base_url=OLLAMA_URL, model=EMBED_MODEL)
    
    # On vérifie si la DB existe, sinon on l'initialise
    vector_db = Chroma(persist_directory=PERSIST_DIRECTORY, embedding_function=embeddings)
    return embeddings, vector_db


@app.cell
def _(LLM_MODEL, OLLAMA_URL, vector_db):
    # Configuration de la chaîne RAG
    llm = Ollama(base_url=OLLAMA_URL, model=LLM_MODEL)
    
    template = """Utilisez les éléments de contexte suivants pour répondre à la question à la fin. 
    Si vous ne connaissez pas la réponse, dites simplement que vous ne savez pas, n'essayez pas d'inventer une réponse.
    Répondez toujours en français.

    {context}

    Question: {question}
    Réponse utile:"""
    
    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

    rag_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=vector_db.as_retriever(),
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
    )
    return QA_CHAIN_PROMPT, llm, rag_chain


@app.cell
def _(mo, rag_chain):
    # Interface de chat
    query = mo.ui.text(placeholder="Posez une question sur vos documents...", label="Question")
    submit = mo.ui.run_button(label="Interroger")
    
    mo.hstack([query, submit])
    return query, submit


@app.cell
def _(query, rag_chain, submit):
    if submit.value:
        with marimo.status.spinner("Hermes réfléchit..."):
            response = rag_chain.invoke(query.value)
            result = response["result"]
    else:
        result = "En attente d'une question..."
    
    return result,


@app.cell
def _(result):
    import marimo as mo
    mo.md(f"### Réponse :\n{result}")
    return


if __name__ == "__main__":
    app.run()
