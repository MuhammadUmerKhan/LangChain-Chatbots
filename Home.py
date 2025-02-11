# Import Streamlit for creating an interactive web application
import streamlit as st

# Set the Streamlit page configuration
st.set_page_config(
    page_title="Langchain Chatbot",  # Title displayed on the browser tab
    page_icon='💬',  # Emoji icon for the tab
    layout='wide'  # Use a wide layout for better UI display
)

# Display the main header of the chatbot application
st.header("Chatbot Implementations with Langchain")

# Display GitHub and LinkedIn profile links using badges
st.write("""
[![view source code](https://img.shields.io/badge/GitHub%20Repository-gray?logo=github)](https://github.com/MuhammadUmerKhan)
[![linkedin](https://img.shields.io/badge/Muhammad%20Umer-blue?logo=linkedin&color=gray)](https://www.linkedin.com/in/muhammad-umer-khan-61729b260/)
""")

# Introduction to Langchain and chatbot implementations
st.write("""
Langchain is a powerful framework designed to streamline the development of applications using Language Models (LLMs). It provides a comprehensive integration of various components, simplifying the process of assembling them to create robust applications.

Leveraging the power of Langchain, the creation of chatbots becomes effortless. Here are a few examples of chatbot implementations catering to different use cases:

### 🔹 Select a Chatbot to Try:
""")

# ✅ Sidebar Navigation to Different Chatbots
st.sidebar.title("🔗 Chatbot Navigation")  # Sidebar title for chatbot navigation

# Add links to different chatbot implementations in the sidebar for easy navigation
st.sidebar.page_link("./pages/💬_BasicChatbot.py", label="🗨️ Basic Chatbot")  # Link to Basic Chatbot
st.sidebar.page_link("./pages/📄_chat_with_your_documents.py", label="📄 Chat With Your Document")  # Link to Document-Based Chatbot
st.sidebar.page_link("./pages/⭐_context_aware_chatbot.py", label="⭐️ Context-Aware Chatbot")  # Link to Context-Aware Chatbot
# st.sidebar.page_link("pages/3_Food_Order_Bot.py", label="🍕 Food Order Bot")  # Commented out: Link to Food Order Bot

# Additional description of chatbot functionalities
st.write("""
Langchain is a powerful framework designed to streamline the development of applications using Language Models (LLMs). It provides a comprehensive integration of various components, simplifying the process of assembling them to create robust applications.

Leveraging the power of Langchain, the creation of chatbots becomes effortless. Here are a few examples of chatbot implementations catering to different use cases:

- **Basic Chatbot**: Engage in interactive conversations with the LLM.
- **Chat with your documents**: Empower the chatbot with the ability to access custom documents, enabling it to provide answers to user queries based on the referenced information.

To explore sample usage of each chatbot, please navigate to the corresponding chatbot section.
""")
