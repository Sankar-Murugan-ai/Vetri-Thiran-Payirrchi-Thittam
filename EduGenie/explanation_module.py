"""Concept explanation using the local LaMini-Flan-T5-783M model (CPU-friendly)."""
from transformers import pipeline

MODEL_NAME = "MBZUAI/LaMini-Flan-T5-783M"
_pipe = None


def _get_pipe():
    global _pipe
    if _pipe is None:  # lazy load: first call downloads the model (~3 GB)
        _pipe = pipeline("text2text-generation", model=MODEL_NAME)
    return _pipe


def explain_concept(topic: str) -> str:
    prompt = f"Explain the following concept in simple words for a beginner: {topic}"
    out = _get_pipe()(prompt, max_length=256, do_sample=True, temperature=0.4)
    return out[0]["generated_text"].strip()
