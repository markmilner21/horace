from backend.prompts import QUESTIONS
from backend.model_answers import MODEL_ANSWERS

class HoraceEngine:
    def __init__(self):
        self.answers = []
        self.index = 0

    def has_next_question(self):
        return self.index < len(QUESTIONS)

    def get_next_question(self):
        if self.has_next_question():
            return QUESTIONS[self.index]
        return None
    
    def get_model_answer(self):
        i = self.index - 1
        if 0 <= i < len(MODEL_ANSWERS):
            return f"Model answer: {MODEL_ANSWERS[i]}"
        return None

    def submit_answer(self, user_answer: str):
        # store user answer (optional but useful later)
        self.answers.append({
            "question_index": self.index,
            "user_answer": user_answer,
            "model_answer": MODEL_ANSWERS[self.index] if self.index < len(MODEL_ANSWERS) else None
        })

        self.index += 1