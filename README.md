# AI Developer Assistant

A command-line AI assistant built with **Python**, the **Groq API**, and **Pydantic** as a Week 3 Python/LLM learning project.

The application answers programming questions, summarizes technical documentation, and extracts structured information from software project descriptions. It also saves conversational history locally in JSON.

## Features

1. **Ask Programming Questions** — Get explanations of programming, APIs, databases, and AI concepts, with context from earlier chat messages.
2. **Summarize Technical Documentation** — Turn technical text into a concise summary.
3. **Extract Software Project Data** — Extract project information as JSON and validate it with Pydantic.
4. **View Chat History** — Display saved conversations.
5. **Clear History** — Reset stored chat messages.
6. **Exit** — Close the application.

## Tech Stack

- Python 3.10+
- Groq Chat Completions API
- `requests` for HTTP requests
- `python-dotenv` for environment variables
- `pydantic` for structured-data validation
- JSON for local conversation storage

## Project Structure

```text
ai-developer-assistant/
├── main.py              # Command-line menu and workflows
├── llm_service.py       # Groq API requests and response handling
├── prompts.py           # System prompts for each AI feature
├── conversation.py      # Load, save, view, and clear chat history
├── config.py            # Environment configuration
├── schemas.py           # Pydantic data model
├── requirements.txt     # Python dependencies
├── .gitignore           # Git exclusions
├── .env                 # Local API credentials (not committed)
└── data/
    └── history.json     # Local conversation history (not committed)
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-developer-assistant.git
cd ai-developer-assistant
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Add your Groq API key

Create a `.env` file in the project root:

```dotenv
GROQ_API_KEY=your_groq_api_key_here
```

Never commit your real API key to GitHub.

### 5. Prepare chat history

Create the `data` directory if it doesn't exist. Inside it, create `history.json` containing:

```json
[]
```

### 6. Run the application

```bash
python main.py
```

## Menu

```text
========== AI DEVELOPER ASSISTANT ==========
1. Ask Programming Questions
2. Summarize Technical Documentation
3. Extract Software Project Data
4. View Chat History
5. Clear History
6. Exit
```

## Example: Software Project Data Extraction

**Input:**

> I built a Student Management System using React for the frontend, Python and Django for the backend, PostgreSQL for the database, and JWT for authentication.

**Example output:**

```json
{
  "project_name": "Student Management System",
  "frontend": "React",
  "backend": ["Python", "Django"],
  "database": "PostgreSQL",
  "authentication": "JWT",
  "deployment": null
}
```

The application parses the model's JSON output and checks its structure using a Pydantic model. Validation checks data types and structure; it does not independently verify factual accuracy.

## What I Practiced

- Python modules, functions, loops, and conditionals
- REST API requests and HTTP error handling
- Environment variables and API-key security
- System prompts and conversation context
- Reading and writing JSON files
- Structured LLM output and Pydantic validation
- Organizing a multi-file Python project

## Notes

- Groq model availability and API rate limits may change. Check the model ID in `llm_service.py` if a request fails.
- Chat history is stored locally and intentionally excluded from Git.
- `.env`, `venv/`, and `data/history.json` should be included in `.gitignore`.

## License

No license has been specified for this learning project.
