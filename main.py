from llm_simulator import simulate_llm_command
from action_executor import execute_actions

def main_pipeline():
    llm_response = simulate_llm_command()
    execute_actions(llm_response)

if __name__ == "__main__":
    main_pipeline()
