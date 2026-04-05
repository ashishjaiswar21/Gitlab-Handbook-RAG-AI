import os
from dotenv import load_dotenv
from supabase import create_client
from sentence_transformers import SentenceTransformer
from scraper import scrape_gitlab_page

# Load environment variables
# This tells Python to look inside the Gitlab-chatbot folder for the .env file
load_dotenv("Gitlab-chatbot/.env")

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    return model.encode(text).tolist()

def chunk_text(text, chunk_size=500):
    chunks = []
    paragraphs = text.split('\n')
    current_chunk = ""
    for para in paragraphs:
        if len(current_chunk) + len(para) < chunk_size:
            current_chunk += para + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = para + " "
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

def save_to_supabase(content, page_url, embedding):
    data = {
        "content": content,
        "url": page_url,
        "embedding": embedding
    }
    supabase.table("gitlab_documents").insert(data).execute()

if __name__ == "__main__":
    target_url = "https://handbook.gitlab.com/handbook/company/culture/"
    print(f"Processing {target_url}...")
    
    text = scrape_gitlab_page(target_url)
    chunks = chunk_text(text)
    
    for i, chunk in enumerate(chunks):
        print(f"Uploading chunk {i+1}/{len(chunks)}...")
        embedding = get_embedding(chunk)
        save_to_supabase(chunk, target_url, embedding)
        
    print("Done! All chunks uploaded to Supabase.")