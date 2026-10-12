from llm_service import ask_llm
import prompts
from conversation import (
    load_history,
    save_history,
    view_history,
    clear_history
)
import json
from schemas import SoftwareProject
from pydantic import ValidationError

def main():

    while True:
        print("\n========== AI DEVELOPER ASSISTANT ==========\n")
        print("1. Ask Programming Questions")
        print("2. Summarize Technical Documentation")
        print("3. Extract Software Project Data")
        print("4. View Chat History")
        print("5. Clear History")
        print("6. Exit")

        try:
            choice = int(input("\nSelect an option: "))

        except ValueError:
            print("Please enter a number from 1 to 6.")
            continue

        if choice == 1:
            user = input("User: ").strip()
            if not user:
                print("Enter a question")
                continue

            history = load_history()
            answer = ask_llm(user, prompts.DEVELOPER_PROMPT, history)
            if answer:
                print(f"AI: {answer}")
                history.append({"role":"user" , "content":user})
                history.append({"role":"assistant" , "content": answer})
                save_history(history)
            else:
                print("Failure")

        elif choice == 2:
            tech = input("User: ").strip()
            if not tech:
                print("Enter a question")
                continue
            answer = ask_llm(tech, prompts.SUMMARY_PROMPT)
            if answer:
                print(f"\nAI Summary: {answer}")
            else:
                print("Fail")

        elif choice == 3:
            ext = input("Enter Project Description: ").strip()
            if not ext:
                print("Enter a question")
                continue
            answer = ask_llm(ext, prompts.EXTRACTION_PROMPT)
            if answer:
                try:
                    data = json.loads(answer)
                    validated = SoftwareProject.model_validate(data)
                    convert = validated.model_dump()
                    print(json.dumps(convert , indent = 4))
                except json.JSONDecodeError:
                    print("Ai returned invalid JSON")
                except ValidationError as e:
                    print(f"Validation Failed: {e}")
            else:
                print("Fail")   

        elif choice == 4:
            view_history()
            continue

        elif choice == 5:
            clear_history()
            continue

        elif choice == 6:
            print("GoodBye!")
            break

        else:
            print("Invalid choice. Select a number from 1 to 6.")


if __name__ == "__main__":
    main()