from horace.engine import HoraceEngine

def run():
    horace = HoraceEngine()

    print("=== Horace Interview Started ===\n")

    while horace.has_next_question():
        question = horace.get_next_question()
        print(f"Horace: {question}")

        answer = input("You: ")
        horace.submit_answer(answer)

        print("")  # spacing

    print("=== Interview Complete ===")
    print("Your answers:")
    for i, a in enumerate(horace.answers, 1):
        print(f"{i}. {a}")

if __name__ == "__main__":
    run()