from transformers import DPRQuestionEncoder, DPRContextEncoder, DPRQuestionEncoderTokenizer, DPRContextEncoderTokenizer
from transformers import BartTokenizer, BartForConditionalGeneration
import faiss
import numpy as np
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

print("start")
# Sample profile data
profiles = [
    {"name": "John Doe", "location": "Bay Area", "years_experience": 6, "work_experience": "marketplace type product"},
    {"name": "Jane Smith", "location": "Bay Area", "years_experience": 5, "work_experience": "e-commerce platform"},
    {"name": "Alice Johnson", "location": "Bay Area", "years_experience": 7, "work_experience": "marketplace type product"},
    # Add more profiles as needed
]

# Initialize DPR models and tokenizers
question_encoder = DPRQuestionEncoder.from_pretrained('facebook/dpr-question_encoder-single-nq-base')
context_encoder = DPRContextEncoder.from_pretrained('facebook/dpr-ctx_encoder-single-nq-base')
question_tokenizer = DPRQuestionEncoderTokenizer.from_pretrained('facebook/dpr-question_encoder-single-nq-base')
context_tokenizer = DPRContextEncoderTokenizer.from_pretrained('facebook/dpr-ctx_encoder-single-nq-base')

# Initialize BART model and tokenizer
generator_tokenizer = BartTokenizer.from_pretrained('facebook/bart-large')
generator = BartForConditionalGeneration.from_pretrained('facebook/bart-large')

# Encode profiles into vectors
context_embeddings = []
for profile in profiles:
    context = f"{profile['name']} from {profile['location']} with {profile['years_experience']} years of experience in {profile['work_experience']}."
    context_inputs = context_tokenizer(context, return_tensors='pt')
    context_embedding = context_encoder(**context_inputs).pooler_output
    context_embeddings.append(context_embedding.detach().numpy())

context_embeddings_matrix = np.vstack(context_embeddings)

# Create FAISS index
dimension = context_embeddings_matrix.shape[1]
index = faiss.IndexFlatIP(dimension)
index.add(context_embeddings_matrix)

def encode_query(query):
    question_inputs = question_tokenizer(query, return_tensors='pt')
    question_embedding = question_encoder(**question_inputs).pooler_output
    return question_embedding

def search_profiles(query_embedding, top_k=5):
    query_vector = query_embedding.detach().numpy()
    _, indices = index.search(query_vector, top_k)
    retrieved_profiles = [profiles[idx] for idx in indices[0]]
    return retrieved_profiles

def generate_response(query, profiles):
    context = " ".join([f"{p['name']} from {p['location']} with {p['years_experience']} years of experience in {p['work_experience']}." for p in profiles])
    inputs = generator_tokenizer(query + " " + context, return_tensors='pt', max_length=1024, truncation=True)
    outputs = generator.generate(**inputs)
    response = generator_tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def main(query):
    query_embedding = encode_query(query)
    profiles = search_profiles(query_embedding)
    response = generate_response(query, profiles)
    return response

# Example query
query = "Find me all software engineers in the bay area that have 5+ years of experience"
response = main(query)
print("end")
print(response) #Find me all software engineers in the bay area that have 5+ years of experience John
