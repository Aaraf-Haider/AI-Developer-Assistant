from conversation import save_history, load_history

history = [
    {"role": "user", "content": "Explain REST API"},
    {"role": "assistant", "content": "REST API allows applications to communicate."}
]

save_history(history)

loaded = load_history()

print(loaded)