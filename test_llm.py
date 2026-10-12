from llm_service import ask_llm
from prompts import DEVELOPER_PROMPT

answer = ask_llm(
    "Explain Python lists in simple English.",
    DEVELOPER_PROMPT
)

print("AI:", answer)