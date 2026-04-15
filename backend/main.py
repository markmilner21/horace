from fastapi import FastAPI
from pydantic import BaseModel
from backend.engine import HoraceEngine

app = FastAPI()
horace = HoraceEngine()

class Message(BaseModel):
    text: str


@app.get("/question")
def get_question():
    return {"question": horace.get_next_question()}


@app.post("/answer")
def send_answer(msg: Message):
    horace.submit_answer(msg.text)

    next_q = horace.get_next_question()

    return {
        "next_question": next_q,
        "done": next_q is None
    }