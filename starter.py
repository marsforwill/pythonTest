# from llama_index.core import VectorStoreIndex,SimpleDirectoryReader,ServiceContext,PromptTemplate
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

print("start")
documents = SimpleDirectoryReader("data").load_data()

# bge-base embedding model
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# ollama
Settings.llm = Ollama(model="llama3", request_timeout=360.0)

index = VectorStoreIndex.from_documents(
    documents,
)
query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)

# Error :openai.RateLimitError: Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}
# 加载文档
# print("start")
# documents = SimpleDirectoryReader("data").load_data()
# index = VectorStoreIndex.from_documents(documents)
# query_engine = index.as_query_engine()
# response = query_engine.query("What did the author do growing up?")
# print(response)
# print("end")