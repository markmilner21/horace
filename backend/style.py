import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"


def style_score(user_answer: str, model_answer: str) -> float:
    prompt = f"""
You are an evaluator.

Compare the USER ANSWER to the MODEL ANSWER.

MODEL ANSWER:
{model_answer}

USER ANSWER:
{user_answer}

Score the USER ANSWER from 0 to 1 based on:
- clarity (clear and understandable)
- confidence (not hesitant or uncertain)
- directness (not rambling)
- professionalism (appropriate tone)

Return ONLY a number between 0 and 1.
No explanation. No text.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    text = response.json()["response"].strip()

    try:
        return float(text)
    except:
        return 0.5  # fallback if model misbehaves