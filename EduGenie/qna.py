from gemini_client import ask_gemini


def answer_question(question: str) -> str:
    prompt = (
        "You are EduGenie, a friendly educational assistant. "
        "Answer the student's question accurately and concisely.\n\n"
        f"Question: {question}"
    )
    return ask_gemini(prompt)
