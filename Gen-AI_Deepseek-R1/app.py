import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)

# =========================
# 🚀 100% CLOUD READY VERSION (NO OLLAMA)
# =========================

# Load API key from environment / Streamlit secrets
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("❌ GROQ_API_KEY missing. Add it in Streamlit secrets.")
    st.stop()

# =========================
# 🎨 UI STYLING
# =========================
st.markdown("""
<style>
    .main {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    .stChatMessage {
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧠 DeepSeek Code Companion (Cloud Edition)")
st.caption("🚀 Fully Cloud-Deployed AI Pair Programmer")

# =========================
# 🤖 CLOUD LLM (GROQ)
# =========================

llm_engine = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama3-70b-8192",  # fast + strong
    temperature=0.3
)

# =========================
# 🧠 PROMPT SETUP
# =========================
system_prompt = SystemMessagePromptTemplate.from_template(
    "You are an expert AI coding assistant. Provide concise, correct solutions with debugging help when needed."
)

# =========================
# 💾 SESSION STATE
# =========================
if "message_log" not in st.session_state:
    st.session_state.message_log = [
        {"role": "ai", "content": "Hi! I'm DeepSeek Cloud Assistant. How can I help you code today? 💻"}
    ]

# =========================
# 💬 CHAT UI
# =========================
for msg in st.session_state.message_log:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_query = st.chat_input("Type your coding question...")

# =========================
# 🔧 PIPELINE
# =========================

def build_prompt_chain():
    messages = [system_prompt]

    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            messages.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        else:
            messages.append(AIMessagePromptTemplate.from_template(msg["content"]))

    return ChatPromptTemplate.from_messages(messages)


def generate_response(chain):
    try:
        return (chain | llm_engine | StrOutputParser()).invoke({})
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# =========================
# 🚀 CHAT FLOW
# =========================
if user_query:
    st.session_state.message_log.append({"role": "user", "content": user_query})

    with st.spinner("🧠 Thinking..."):
        prompt_chain = build_prompt_chain()
        response = generate_response(prompt_chain)

    st.session_state.message_log.append({"role": "ai", "content": response})

    st.rerun()

# =========================
# 📌 DEPLOYMENT INFO
# =========================
st.info(
"""
✅ FULLY CLOUD READY:
- No Ollama required
- Works on Streamlit Cloud
- Uses Groq API

🔑 Add this in Streamlit Secrets:
GROQ_API_KEY = your_key_here
""")
import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)

# =========================
# 🚀 100% CLOUD READY VERSION (NO OLLAMA)
# =========================

# Load API key from environment / Streamlit secrets
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("❌ GROQ_API_KEY missing. Add it in Streamlit secrets.")
    st.stop()

# =========================
# 🎨 UI STYLING
# =========================
st.markdown("""
<style>
    .main {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    .stChatMessage {
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧠 DeepSeek Code Companion (Cloud Edition)")
st.caption("🚀 Fully Cloud-Deployed AI Pair Programmer")

# =========================
# 🤖 CLOUD LLM (GROQ)
# =========================

llm_engine = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama3-70b-8192",  # fast + strong
    temperature=0.3
)

# =========================
# 🧠 PROMPT SETUP
# =========================
system_prompt = SystemMessagePromptTemplate.from_template(
    "You are an expert AI coding assistant. Provide concise, correct solutions with debugging help when needed."
)

# =========================
# 💾 SESSION STATE
# =========================
if "message_log" not in st.session_state:
    st.session_state.message_log = [
        {"role": "ai", "content": "Hi! I'm DeepSeek Cloud Assistant. How can I help you code today? 💻"}
    ]

# =========================
# 💬 CHAT UI
# =========================
for msg in st.session_state.message_log:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_query = st.chat_input("Type your coding question...")

# =========================
# 🔧 PIPELINE
# =========================

def build_prompt_chain():
    messages = [system_prompt]

    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            messages.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        else:
            messages.append(AIMessagePromptTemplate.from_template(msg["content"]))

    return ChatPromptTemplate.from_messages(messages)


def generate_response(chain):
    try:
        return (chain | llm_engine | StrOutputParser()).invoke({})
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# =========================
# 🚀 CHAT FLOW
# =========================
if user_query:
    st.session_state.message_log.append({"role": "user", "content": user_query})

    with st.spinner("🧠 Thinking..."):
        prompt_chain = build_prompt_chain()
        response = generate_response(prompt_chain)

    st.session_state.message_log.append({"role": "ai", "content": response})

    st.rerun()

# =========================
# 📌 DEPLOYMENT INFO
# =========================
st.info(
"""
✅ FULLY CLOUD READY:
- No Ollama required
- Works on Streamlit Cloud
- Uses Groq API

🔑 Add this in Streamlit Secrets:
GROQ_API_KEY = your_key_here
""")
