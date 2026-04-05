# import streamlit as st
# import requests

# # Page configuration
# st.set_page_config(page_title="GitLab Handbook AI", page_icon="🦊")

# st.title("🦊 GitLab Handbook Assistant")
# st.markdown("Ask me anything about GitLab's company culture and handbook.")

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat history
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # User Input
# if prompt := st.chat_input("How does GitLab handle transparency?"):
#     # Add user message to history
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # Call your FastAPI Backend
#     with st.chat_message("assistant"):
#         with st.spinner("Searching the handbook..."):
#             try:
#                 # This matches the /chat endpoint in your main.py
#                 response = requests.post(
#                     "http://127.0.0.1:8000/chat",
#                     json={"question": prompt}
#                 )
                
#                 if response.status_code == 200:
#                     answer = response.json().get("answer", "No answer found.")
#                     st.markdown(answer)
#                     st.session_state.messages.append({"role": "assistant", "content": answer})
#                 else:
#                     st.error(f"Backend Error: {response.status_code}")
            
#             except Exception as e:
#                 st.error(f"Connection Error: {str(e)}")

import streamlit as st
import requests

# 1. Page Configuration (Wide layout for a better chat experience)
st.set_page_config(page_title="GitLab Assistant", page_icon="🦊", layout="wide")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm your GitLab Handbook AI. What would you like to know about our culture?"}
    ]

# 2. Build the Interactive Sidebar
with st.sidebar:
    # Prominent NEW CHAT button at the top
    if st.button("➕ New Chat", type="primary", use_container_width=True):
        # Reset the messages list
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! I'm your GitLab Handbook AI. What would you like to know about our culture?"}
        ]
        # Show a quick pop-up notification
        st.toast("Started a new conversation!", icon="✨")
        st.rerun()
    
    st.divider()
    
    st.title("⚙️ Settings & Info")
    
    # Collapsible Expander for technical details
    with st.expander("🛠️ How does this work?"):
        st.markdown("""
        1. **Search**: Your question is converted into embeddings.
        2. **Retrieve**: We pull the best matches from the GitLab Handbook via **Supabase**.
        3. **Generate**: **Gemini 2.5 Flash** reads the context and writes a custom answer!
        """)

    st.divider()
    
    st.subheader("💡 Quick Questions")
    st.caption("Click to ask instantly:")
    
    # Quick-prompt buttons
    if st.button("What is the CREDIT acronym?", use_container_width=True):
        st.session_state.quick_prompt = "What is the CREDIT acronym?"
    if st.button("How does GitLab handle transparency?", use_container_width=True):
        st.session_state.quick_prompt = "How does GitLab handle transparency?"
    if st.button("What is the mission of GitLab?", use_container_width=True):
        st.session_state.quick_prompt = "What is the mission of GitLab?"

# 3. Main Chat Interface Header
st.title("🦊 GitLab Handbook Assistant")
st.caption("Powered by Gemini 2.5 Flash & Supabase Vector Search ")
st.caption("👨‍💻 **Made by Ashish Kumar**") # <--- Add this line here!
st.divider()

# 4. Handle Input Trigger
prompt = None
if "quick_prompt" in st.session_state:
    prompt = st.session_state.quick_prompt
    del st.session_state.quick_prompt # Clear it so it doesn't loop
else:
    prompt = st.chat_input("Ask a question about GitLab...")

# 5. Display Chat History inside a dedicated container
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        avatar = "🦊" if message["role"] == "assistant" else "👤"
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

# 6. Process new user input
if prompt:
    # Instantly show the user's message
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Show bot's thinking state
    with st.chat_message("assistant", avatar="🦊"):
        with st.spinner("Searching the handbook..."):
            try:
                # Call the FastAPI backend (Make sure your uvicorn server is running!)
                response = requests.post("http://127.0.0.1:8000/chat", json={"question": prompt})
                
                if response.status_code == 200:
                    bot_reply = response.json().get("answer", "No answer found in response.")
                else:
                    bot_reply = f"Sorry, the backend returned an error (Status {response.status_code})."
                    st.error(bot_reply)
            except requests.exceptions.ConnectionError:
                bot_reply = "Could not connect to the backend server. Make sure your FastAPI app is running on port 8000!"
                st.error(bot_reply)
        
        # Output the generated answer
        if "error" not in bot_reply.lower():
            st.markdown(bot_reply)
    
    # Save bot response to history so it stays on screen
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})