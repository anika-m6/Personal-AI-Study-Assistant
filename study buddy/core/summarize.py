from core.ai_utils import get_classroom_response

def summarize_academic_text(text: str) -> str:
    """Sends raw text to Gemini with strict rules to build a study summary."""
    system_instruction = (
        "You are an expert academic summarizer. Condense the provided lecture notes into an "
        "exam-ready study summary. Use clear markdown headings, bold key terms, structured bullet points, "
        "and conclude with 3 quick self-test practice questions."
    )
    return get_classroom_response(text, system_instruction)