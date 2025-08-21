from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

# RAG + Summarization prompt template
template = """
You are a research and analytics assistant for UNICEF’s Education Outcomes Fund (EOF).
You answer questions by analyzing official UNICEF/EOF reports.

Instructions:
- Provide a clear, concise answer based on the excerpts.
- Reference the reports directly in your explanation.
- Always finish with a "Sources:" section listing the report names used.
- If the question is to "summarize" a report, provide a concise summary.

Here are relevant excerpts from UNICEF/EOF reports:
{reviews}

Question:
{question}

Answer:
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Function to check if question is likely UNICEF-related
def is_unicef_related(text):
    keywords = ["unicef", "education outcomes fund", "child", "report", "fund", "eof"]
    return any(word.lower() in text.lower() for word in keywords)

def answer_question(question: str):
    if not is_unicef_related(question):
        return "I'm here to help with UNICEF reports only. Please ask a question related to UNICEF. 😊"
    
    retrieved_docs = retriever.invoke(question)
    
    reviews_text = "\n\n".join(
        [f"Excerpt from {doc.metadata.get('source', 'Unknown')}: {doc.page_content}" for doc in retrieved_docs]
    )
    
    sources = list({doc.metadata.get("source", "Unknown") for doc in retrieved_docs})
    sources_text = "\n".join([f"- {src}" for src in sources])
    
    result = chain.invoke({"reviews": reviews_text, "question": question})
    
    final_answer = f"{result}\n\nSources:\n{sources_text}"
    return final_answer
