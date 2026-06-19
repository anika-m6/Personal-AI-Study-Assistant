import streamlit as st
from components.sidebar import render_sidebar
from core.pdf_handler import process_core_pdf
from components.chat_ui import (
    initialize_chat_history, 
    append_to_chat_history, 
    render_entire_chat_history,
    display_chat_message
)
from core.explainer import explain_concept
from core.summarize import summarize_academic_text  # FIX: Corrected folder name
from core.quizzer import generate_quiz, solve_questions, evaluate_answers
from utils.logger import log_usage

# 1. Page Configuration
st.set_page_config(page_title="AI Study Assistant", page_icon="📘", layout="wide")
st.title("📘Personal Study Assistant")

# Initialize the message state memory system
initialize_chat_history()

# 2. Render Sidebar
app_mode = render_sidebar()

# Render all past messages in the session first so they don't disappear
render_entire_chat_history()

# --- MODE 1: CONCEPT EXPLAINER ---
if app_mode == "🧠 Concept Explainer":
    st.caption("Active Mode: Concept Explainer & Diagram Planner")
    
    concept = st.text_input("What topic or concept do you want explained?", placeholder="e.g., Database Normalization")
    context = st.text_input("Exam level / Extra Context (Optional):")
    
    if st.button("Explain Concept"):
        if not concept.strip():
            st.warning("Please enter a concept!")
        else:
            # Display user's question instantly in a chat container
            display_chat_message("user", f"Explain: {concept}")
            append_to_chat_history("user", f"Explain: {concept}")
            
            with st.spinner("Analyzing and simplifying..."):
                explanation = explain_concept(concept, context)
                
                # Display AI's response in a chat container and save it
                display_chat_message("assistant", explanation)
                append_to_chat_history("assistant", explanation)
                
                # FIX: Passed all required advanced logging parameters
                log_usage(
                    mode="🧠 Concept Explainer",
                    sub_mode=None,
                    had_pdf=False,
                    prompt_text=concept,
                    response_text=explanation
                )

# --- MODE 2: PDF SUMMARIZER ---
elif app_mode == "📄 PDF Summarizer":
    st.caption("Active Mode: Lecture Notes & PDF Summarizer")
    
    uploaded_file = st.file_uploader("Drop your study material here:", type=["pdf"])
    
    if st.button("Generate Summary"):
        if uploaded_file is None:
            st.warning("Please upload a PDF file first!")
        else:
            display_chat_message("user", f"Summarize uploaded document: {uploaded_file.name}")
            append_to_chat_history("user", f"Summarize uploaded document: {uploaded_file.name}")
            
            with st.spinner("Extracting text and digesting notes..."):
                raw_text = process_core_pdf(uploaded_file)
                
                if "Error reading PDF" in raw_text or len(raw_text.strip()) < 30:
                    st.error("Could not extract readable text. The PDF might be a flat image scan.")
                else:
                    summary_result = summarize_academic_text(raw_text)
                    display_chat_message("assistant", summary_result)
                    append_to_chat_history("assistant", summary_result)
                    
                    # FIX: Passed all required advanced logging parameters
                    log_usage(
                        mode="📄 PDF Summarizer",
                        sub_mode=None,
                        had_pdf=True,
                        prompt_text=f"Summarize document: {uploaded_file.name}",
                        response_text=summary_result
                    )

# --- MODE 3: SMART QUIZZER ---
elif app_mode == "🧩 Smart Quizzer":
    st.caption("Active Mode: Smart Examiner & Evaluator Hub")
    quiz_action = st.radio("What would you like to do?", ["📝 Generate Quiz", "📖 Solve Questions", "✅ Grade My Answer"])
    st.markdown("---")
    
    if quiz_action == "📝 Generate Quiz":
        quiz_source = st.text_area("Paste a chapter passage or type a topic:")
        if st.button("Create Practice Test"):
            if quiz_source.strip():
                display_chat_message("user", "Generate quiz for topic.")
                append_to_chat_history("user", "Generate quiz for topic.")
                with st.spinner("Drafting questions..."):
                    quiz_out = generate_quiz(quiz_source)
                    display_chat_message("assistant", quiz_out)
                    append_to_chat_history("assistant", quiz_out)
                    
                    # FIX: Correct parameters passed to log_usage
                    log_usage(
                        mode="🧩 Smart Quizzer",
                        sub_mode="📝 Generate Quiz",
                        had_pdf=False,
                        prompt_text=quiz_source,
                        response_text=quiz_out
                    )
                    
    elif quiz_action == "📖 Solve Questions":
        questions_input = st.text_area("Paste your exam assignment questions here:")
        word_limits = st.text_input("Word count or mark details (Optional):")
        if st.button("Generate Answers"):
            if questions_input.strip():
                display_chat_message("user", f"Solve these questions:\n{questions_input}")
                append_to_chat_history("user", f"Solve these questions:\n{questions_input}")
                with st.spinner("Solving..."):
                    solutions = solve_questions(questions_input, word_limits)
                    display_chat_message("assistant", solutions)
                    append_to_chat_history("assistant", solutions)
                    
                    # FIX: Correct parameters passed to log_usage
                    log_usage(
                        mode="🧩 Smart Quizzer",
                        sub_mode="📖 Solve Questions",
                        had_pdf=False,
                        prompt_text=questions_input,
                        response_text=solutions
                    )
                    
    elif quiz_action == "✅ Grade My Answer":
        evaluation_input = st.text_area("Paste Question & Answer here (separate with '---'):")
        if st.button("Grade Me"):
            if "---" in evaluation_input:
                display_chat_message("user", "Evaluate my answer submission.")
                append_to_chat_history("user", "Evaluate my answer submission.")
                with st.spinner("Evaluating details..."):
                    grades = evaluate_answers(evaluation_input)
                    display_chat_message("assistant", grades)
                    append_to_chat_history("assistant", grades)
                    
                    # FIX: Correct parameters passed to log_usage
                    log_usage(
                        mode="🧩 Smart Quizzer",
                        sub_mode="✅ Grade Answer",
                        had_pdf=False,
                        prompt_text=evaluation_input,
                        response_text=grades
                    )