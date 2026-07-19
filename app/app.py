import streamlit as st
import sys
import os

# Add src to the Python path
sys.path.append(os.path.abspath("src"))

from run_agent import initialize_agent

st.set_page_config(
    page_title="SciAgent",
    page_icon="🤖",
    layout="wide"
)

#@st.cache_resource
def load_agent():
    return initialize_agent()

agent = load_agent()

# ----------------------------
# Sidebar
# ----------------------------

with st.sidebar:

    st.title("Scientific Literature Assistant")

    st.caption("Powered by FAISS + Ollama + Multi-Agent RAG")

    st.divider()

    st.markdown(
        """
        **Trustworthy Multi-Agent AI**
        
        Scientific Literature Exploration
        """
    )

    st.divider()

    st.subheader("Loaded Papers")

    st.success("1. Attention is All You Need (Vaswani et al., 2017)")

    st.divider()

    st.info(
        "Ask questions grounded in the uploaded scientific papers."
    )

st.title("🤖 SciAgent")

st.subheader(
    "Trustworthy Multi-Agent AI for Scientific Literature Exploration"
)

st.divider()

question = st.text_area(
    "Research Question",
    placeholder="Example: What is positional encoding?",
    height=100
)

if st.button("Ask SciAgent", use_container_width=True):

    if question.strip() == "":
        st.warning("Please enter a research question.")
        st.stop()

    with st.spinner("SciAgent is working on your question..."):
        result = agent.answer(question)

    verification = result["verification"]

    answer_tab, verify_tab, citation_tab = st.tabs(["Answer", "Verification", "Citations"])

    with answer_tab:
        st.markdown("### Draft Answer")
        st.markdown(result["draft"])

    with verify_tab:
        st.metric("Confidence", f"{verification['confidence']*100:.0f}%")
        if verification["verified"]:
            st.success("The answer is verified based on the retrieved evidence.")
        else:
            st.error("The answer is NOT verified based on the retrieved evidence.")
        st.markdown("### Verification Report")
        st.write(verification["report"])

    with citation_tab:
        for citation in result["citations"]:
            st.info(f""" Paper : {citation['paper']}
                Page  : {citation['page']}
                Distance Score: {citation['distance']:.4f}
            """)