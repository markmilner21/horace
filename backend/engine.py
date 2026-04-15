from backend.prompts import QUESTIONS
from backend.model_answers import MODEL_ANSWERS
from backend.similarity import compute_similarity
from backend.brevity import brevity_score
from backend.style import style_score

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

        content = compute_similarity(user_answer, model_answer)
        brevity = brevity_score(user_answer, model_answer)
        style = style_score(user_answer, model_answer)

        final_score = (
            0.5 * content +
            0.2 * brevity +
            0.3 * style
        )

        self.history.append({
            "question": QUESTIONS[self.index],
            "user_answer": user_answer,
            "model_answer": model_answer,
            "content_score": content,
            "brevity_score": brevity,
            "style_score": style,
            "final_score": final_score
        })

        self.index += 1

        return final_score, model_answer, content, brevity, style
    