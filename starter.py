# from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
# from llama_index.core import VectorStoreIndex,SimpleDirectoryReader,ServiceContext,PromptTemplate

# from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex,SimpleDirectoryReader,ServiceContext,PromptTemplate

# 加载文档
reader = SimpleDirectoryReader('data')
documents = reader.load_data()
print("start")

# 构建索引
# index = GPTVectorStoreIndex(documents)

# # 保存索引到磁盘
# index.save_to_disk('index.json')

# # 从磁盘加载索引
# index = GPTVectorStoreIndex.load_from_disk('index.json')

# # 查询索引
# response = index.query("Find me all software engineers in the bay area that have 5+ years of experience and have worked on a marketplace type product in the past")
# print(response)


# documents = SimpleDirectoryReader("data").load_data()
# index = VectorStoreIndex.from_documents(documents)
# query_engine = index.as_query_engine()
# response = query_engine.query("What did the author do growing up?")
# print(response)