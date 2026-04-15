from backend.prompts import QUESTIONS
from backend.model_answers import MODEL_ANSWERS
from backend.similarity import compute_similarity

class HoraceEngine:
    def __init__(self):
        self.history = []
        self.index = 0

    def has_next_question(self):
        return self.index < len(QUESTIONS)

    def get_next_question(self):
        if self.has_next_question():
            return QUESTIONS[self.index]
        return None

    def submit_answer(self, user_answer: str):
        model_answer = MODEL_ANSWERS[self.index]

        score = compute_similarity(user_answer, model_answer)

        self.history.append({
            "question": QUESTIONS[self.index],
            "user_answer": user_answer,
            "model_answer": model_answer,
            "similarity": score
        })

        self.index += 1

        return score, model_answer
    