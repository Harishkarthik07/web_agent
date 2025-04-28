import json
from llm_parser import parse_steps
from browser_use_helper import execute_steps
from validator import validate_result

def run_test(test_input):
    steps = parse_steps(test_input["test_case"]["steps"])
    actual_output = execute_steps(test_input["url"], steps)
    result = validate_result(actual_output, test_input["test_case"]["expected_output"])
    return result

if __name__ == "__main__":
    with open("example_input.json") as f:
        test_input = json.load(f)
    result = run_test(test_input)
    print(json.dumps(result, indent=2))
