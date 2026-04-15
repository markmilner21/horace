from backend.prompts import QUESTIONS

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

    def submit_answer(self, answer: str):
        self.answers.append(answer)
        self.index += 1