import json
from gemini_client import ask_gemini


def clean_json_block(text: str) -> str:
    """Strip Markdown code fences such as ```json ... ```."""
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1] if "\n" in text else text
        text = text.rsplit("```", 1)[0]
    return text.strip()


def generate_quiz(passage: str):
    prompt = (
        "Create exactly 3 multiple-choice questions from the topic or passage below. "
        "Each question needs exactly 4 options and one correct answer. "
        "Respond ONLY with a JSON list, no extra text, in this format:\n"
        '[{"question": "...", "options": ["A", "B", "C", "D"], '
        '"answer": "<the exact text of the correct option>"}]\n\n'
        f"Passage or topic:\n{passage}"
    )
    try:
        raw = ask_gemini(prompt)
        data = json.loads(clean_json_block(raw))
        if not isinstance(data, list) or not data:
            raise ValueError("Quiz is not a non-empty list")
        return data
    except Exception as e:
        raise RuntimeError(f"Quiz generation/parsing failed: {e}")
