from gemini_client import ask_gemini


def summarize_text(text: str) -> str:
    prompt = (
        "Summarize the passage below into a concise, easy-to-understand version "
        "for quick revision. Keep the core information and remove redundancy.\n\n"
        f"Passage:\n{text}"
    )
    return ask_gemini(prompt)
