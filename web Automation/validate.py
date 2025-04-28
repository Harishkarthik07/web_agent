def validate_result(actual, expected):
    if expected.lower() in actual["final_dom_text"].lower():
        return {"status": "Pass", "notes": "Expected text found in final DOM"}
    else:
        return {"status": "Fail", "notes": "Expected text not found"}
