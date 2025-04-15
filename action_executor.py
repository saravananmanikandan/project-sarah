import json
import time
import subprocess
import pyautogui
from open_notepad import open_notepad

def execute_actions(llm_response):
    try:
        actions = json.loads(llm_response).get("actions", [])
    except Exception as e:
        print("JSON Parsing Error:", e)
        return

    for act in actions:
        if act["type"] == "open_app":
            open_notepad()
            time.sleep(2)  
        elif act["type"] == "input_text":
            pyautogui.write(act["text"], interval=0.1)
