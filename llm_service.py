import requests
from config import groq_api

def ask_llm(user_text, system_prompt, history=None):

    messages = [
        {"role": "system", "content": system_prompt}
    ]

    if history:
        messages.extend(history)

    messages.append({
        "role": "user",
        "content": user_text
    })
    
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
    "Authorization": f"Bearer {groq_api}",
    "Content-Type": "application/json"
}

    payload = {
    "model": "openai/gpt-oss-20b",
    "messages": messages ,
    "temperature": 0.3
}

    try:
        response = requests.post(
            url, 
            headers=headers, 
            json=payload, 
            timeout=30
            )
        response.raise_for_status()

        result = response.json()
        answer = result["choices"][0]["message"]["content"]
        return answer
    
    except (KeyError, IndexError, TypeError, ValueError):
        print("Error: Invalid API response.")
        return None

    except requests.exceptions.Timeout:
        print("Error: API request timed out.")
        return None

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to Groq.")
        return None

    except requests.exceptions.HTTPError as e:
        print(f"Error: Groq returned HTTP {e.response.status_code}.")
        return None

    except requests.exceptions.RequestException:
        print("Error: API request failed.")
        return None