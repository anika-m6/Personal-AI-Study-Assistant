import streamlit as st

def render_sidebar() -> str:
    """
    Renders the sidebar navigation panel and returns the user's selected operational mode.
    """
    st.sidebar.title("Workspace")
    st.sidebar.write("Configure your study dashboard options here.")
    
    st.sidebar.markdown("---")
    
    # 1. Provide the dropdown menu option selection
    selected_mode = st.sidebar.selectbox(
        "Choose App Mode",
        ["🧠 Concept Explainer", "📄 PDF Summarizer", "🧩 Smart Quizzer"]
    )
    
    st.sidebar.markdown("---")
    
    # 2. Provide a clean system reset button control routine
    st.sidebar.subheader("App Controls")
    if st.sidebar.button("🔄 Clear App Cache / Reset"):
        st.session_state.clear()
        st.rerun()
        
    return selected_mode