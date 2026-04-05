import os
import time
from dotenv import load_dotenv
from supabase import create_client
from sentence_transformers import SentenceTransformer
from google import genai
from google.genai import errors

# Load environment variables from your specific folder path
load_dotenv("Gitlab-chatbot/.env")

# Initialize clients
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
gemini_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
embed_model = SentenceTransformer('all-MiniLM-L6-v2')

def get_answer(user_query):
    # 1. Turn the user's question into a vector
    query_vector = embed_model.encode(user_query).tolist()

    # 2. Search Supabase for the 3 most relevant chunks
    response = supabase.rpc("match_documents", {
        "query_embedding": query_vector,
        "match_threshold": 0.5, 
        "match_count": 3
    }).execute()

    # 3. Combine the found text into one "Context" block
    context = "\n\n".join([item['content'] for item in response.data])
    
    if not context:
        return "I'm sorry, I couldn't find any information about that in the GitLab handbook."

    # 4. Ask Gemini to answer based ONLY on that context
    prompt = f"""
    You are a GitLab Handbook Assistant. Answer the user question based ONLY on the context provided below.
    If the answer isn't in the context, say you don't know.

    CONTEXT:
    {context}

    USER QUESTION:
    {user_query}
    """

    # 5. Add Retry Logic for the Gemini API call to handle Rate Limits (429 errors)
    max_retries = 3
    for attempt in range(max_retries):
        try:
            answer = gemini_client.models.generate_content(
                # model="gemini-2.0-flash",
                model="gemini-2.5-flash",
                contents=prompt
            )
            return answer.text
            
        except errors.ClientError as e:
            if e.code == 429:
                print(f"Rate limit hit. Waiting 45 seconds before retrying (Attempt {attempt + 1}/{max_retries})...")
                time.sleep(45) # Wait for the quota bucket to reset
            else:
                # If it's a different error, raise it so you can see what went wrong
                raise e
                
    return "Sorry, the AI service is currently busy. Please try again later."

if __name__ == "__main__":
    # Test call
    print("Asking Gemini about GitLab's mission...")
    print(get_answer("What is the mission of GitLab?"))