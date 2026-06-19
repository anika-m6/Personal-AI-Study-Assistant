from core.ai_utils import get_classroom_response

def generate_quiz(topic_or_text: str) -> str:
    prompt = f"Generate a balanced academic quiz containing 2 MCQs, 2 Fill-in-the-blanks, and 1 descriptive question based on this:\n\n{topic_or_text}\n\nProvide a clearly marked '🔑 Answer Key' at the bottom."
    return get_classroom_response(prompt)

def solve_questions(questions: str, constraints: str = "") -> str:
    prompt = f"Provide structured, exam-ready answers for these questions:\n\n{questions}\n\nConstraints: {constraints}"
    return get_classroom_response(prompt)

def evaluate_answers(question_and_answer: str) -> str:
    prompt = f"Review this student submission. Provide a score out of 10, what went well, and what is missing:\n\n{question_and_answer}"
    return get_classroom_response(prompt)