from core.ai_utils import get_classroom_response

def explain_concept(concept: str, context: str = "") -> str:
    system_instruction = (
        "You are an elite university professor and academic tutor. "
        "Explain the provided concept in simple, highly clear, and exam-oriented terms. "
        "Structure your response beautifully with clear markdown headings (##), bold keywords, and bullet points. "
        "At the absolute end, always add a section titled: '🎨 Recommended Exam Diagram Idea' describing a simple flowchart."
    )
    full_prompt = f"Explain this concept: {concept}.\n"
    if context:
        full_prompt += f"Additional Exam Context/Level: {context}"
    return get_classroom_response(full_prompt, system_instruction)