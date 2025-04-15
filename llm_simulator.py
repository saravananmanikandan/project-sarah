import json

def simulate_llm_command():
    command = {
        "command": "open_notepad",
        "actions": [
            {"type": "open_app", "app": "notepad.exe"},
            {"type": "input_text", "text": "Hello, this is an automated message for Project Sarah."}
        ]
    }
    return json.dumps(command)
