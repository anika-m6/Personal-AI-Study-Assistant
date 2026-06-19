from utils.gemini_helper import generate_response

def get_classroom_response(prompt: str, system_instruction: str = "") -> str:
    """
    A specific wrapper for core features to send structured academic 
    prompts to our primary backend helper.
    """
    # If a system instruction is passed, we can combine it with the prompt
    if system_instruction:
        full_prompt = f"{system_instruction}\n\nUser Input:\n{prompt}"
    else:
        full_prompt = prompt
        
    return generate_response(full_prompt)