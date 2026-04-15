def brevity_score(user_text: str, model_text: str) -> float:
    user_len = len(user_text.split())
    model_len = len(model_text.split())

    if model_len == 0:
        return 0.0

    ratio = user_len / model_len

    # ideal ratio = 1
    score = 1 - abs(ratio - 1)

    # clamp between 0 and 1
    return max(0.0, min(1.0, score))