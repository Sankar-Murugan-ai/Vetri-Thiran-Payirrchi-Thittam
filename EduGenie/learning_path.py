from gemini_client import ask_gemini


def get_learning_recommendations(topic: str) -> str:
    prompt = (
        f"Create a personalized, structured learning path for: {topic}.\n"
        "Organise it from beginner to advanced. For each stage give the key concepts, "
        "a suggested timeline, and useful resources (videos, articles, books). "
        "Use clear headings and short bullet points."
    )
    return ask_gemini(prompt)
