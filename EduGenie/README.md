# 🎓 EduGenie: Gemini Powered Learning Assistant

EduGenie is a lightweight AI-powered educational assistant built with **FastAPI** and a simple **HTML + CSS** frontend. It uses **Google Gemini** (cloud) for most tasks and **LaMini-Flan-T5-783M** (local) for concept explanations. It runs well on modest hardware such as a Mac M1.

## Features

| Feature | Endpoint | Powered by |
|---|---|---|
| Ask questions | `POST /qa` | Gemini |
| Explain concepts simply | `POST /explain` | LaMini-Flan-T5-783M (local) |
| Generate a 3-question MCQ quiz | `POST /quiz` | Gemini |
| Summarize long passages | `POST /summarize` | Gemini |
| Personalized learning path | `POST /learn/recommendations` | Gemini |

**Example scenarios**
1. Ask "Which is the largest ocean?"
2. Enter "The Pythagoras Theorem" and click Generate Quiz to test your understanding.
3. Ask for an SQL learning path from beginner to advanced, with timelines and resources.

## Project Structure

```
EduGenie/
├── main.py                 # FastAPI app and endpoints
├── gemini_client.py        # Shared Gemini API helper
├── explanation_module.py   # Concept explanation (LaMini-Flan-T5, local)
├── qna.py                  # Question answering
├── quiz_module.py          # Quiz generation (JSON output)
├── summary_module.py       # Summarization
├── learning_path.py        # Learning recommendations
├── templates/index.html    # HTML frontend
├── static/style.css        # Styling
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variable template
└── README.md
```

## Prerequisites

- **Python 3.10+**. Check with `python --version`. On Windows, tick "Add Python to PATH" during installation.
- **Google Gemini API key**: sign in at [Google AI Studio](https://aistudio.google.com), create an API key and store it securely.
- About **3 GB of free disk space** for the LaMini-Flan-T5 model, downloaded automatically on the first `/explain` request.

## Setup

```bash
# 1. Go into the project folder
cd EduGenie

# 2. (Recommended) create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API key
cp .env.example .env            # Windows: copy .env.example .env
# then edit .env and set GEMINI_API_KEY=your-key
```

## Run

```bash
uvicorn main:app --reload
```

Open **http://127.0.0.1:8000** in your browser. Interactive API docs are at **http://127.0.0.1:8000/docs**.

## Usage

1. Pick a task from the dropdown (Ask a Question, Explain, Generate Quiz, Summarize, Recommend Learning Path).
2. Type a question, topic or passage in the text area.
3. Click **Submit**. The result appears below the input box.
4. For quizzes, click an option to see whether it's right; the correct answer is shown if you're wrong.

### API example

```bash
curl -X POST http://127.0.0.1:8000/qa \
  -H "Content-Type: application/json" \
  -d '{"text": "Which is the largest ocean?"}'
```

## Configuration

| Variable | Required | Description |
|---|---|---|
| `GEMINI_API_KEY` | Yes | Your Google AI Studio API key |
| `GEMINI_MODEL` | No | Gemini model name. Defaults to `gemini-2.5-flash`; set to `gemini-1.5-pro` or any other model available to your key |

## Functional Testing Checklist

- [ ] Ask a question
- [ ] Get an explanation (first call is slow while the model downloads)
- [ ] Generate a quiz (3 questions, 4 options each)
- [ ] Summarize content
- [ ] Get a personalized learning plan

## Troubleshooting

- **"GEMINI_API_KEY is not set"**: make sure `.env` exists in the project root with your key, then restart uvicorn.
- **Quiz parsing error**: retry; the model occasionally returns malformed JSON. Markdown code fences are stripped automatically.
- **`/explain` is slow**: the local model runs on CPU and loads on first use. Later calls are faster.
- **Install errors for `torch`**: see [pytorch.org](https://pytorch.org/get-started/locally/) for a build matching your system.

## Future Enhancements

Voice interaction, multilingual support, a mobile app, progress dashboards, gamification (badges, streaks), adaptive learning paths, group study and LMS integration (Moodle, Google Classroom), and image/PDF input.

---
**Submitted by:** Tella Divya Sree  |  **Mentor:** Siri  |  **Date:** 11/04/2025
