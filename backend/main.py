from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from backend.engine import HoraceEngine

app = FastAPI()

# CORS (for safety, mostly needed if frontend not served from same origin)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API first (important for clarity)
horace = HoraceEngine()

class Message(BaseModel):
    text: str


@app.get("/question")
def get_question():
    return {"question": horace.get_next_question()}

@app.post("/answer")
def send_answer(msg: Message):

    score, model_answer = horace.submit_answer(msg.text)
    next_q = horace.get_next_question()
    return {
        "model_answer": model_answer,
        "similarity_score": score,
        "next_question": next_q,
        "done": next_q is None
    }


# Frontend LAST
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")