from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from qna import answer_question
from explanation_module import explain_concept
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

app = FastAPI(title="EduGenie")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class TextIn(BaseModel):
    text: str


def run(fn, text: str):
    text = text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Input cannot be empty.")
    try:
        return fn(text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.post("/qa")
def qa(body: TextIn):
    return {"result": run(answer_question, body.text)}


@app.post("/explain")
def explain(body: TextIn):
    return {"result": run(explain_concept, body.text)}


@app.post("/quiz")
def quiz(body: TextIn):
    return {"result": run(generate_quiz, body.text)}


@app.post("/summarize")
def summarize(body: TextIn):
    return {"result": run(summarize_text, body.text)}


@app.post("/learn/recommendations")
def recommendations(body: TextIn):
    return {"result": run(get_learning_recommendations, body.text)}
