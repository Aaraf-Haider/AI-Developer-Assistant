import os
import json

filename = os.path.join(
    os.path.dirname(__file__),
    "data",
    "history.json"
)

def load_history():

    if os.path.exists(filename):

        with open(filename, "r", encoding="utf-8") as f:
            history = json.load(f)

        return history

    else:
        return []

def save_history(history):
    with open(filename , "w" , encoding = "utf-8") as f:
        json.dump(history , f , indent = 4)

def view_history():
    history = load_history()
    if not history:
        print("No chat history found.")
    else:
        for i,message in enumerate(history , start = 1):
            print(f"{i}. {message['role']}: {message['content']}")

def clear_history():
    save_history([])
    print("Conversation History cleared successfully")
