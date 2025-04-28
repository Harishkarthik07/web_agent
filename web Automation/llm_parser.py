def parse_steps(steps):
    return [
        {"action": "click", "target": "text='Sign in'"},
        {"action": "type", "target": "input[type='email']", "value": "test@example.com"},
        {"action": "type", "target": "input[type='password']", "value": "test123"},
        {"action": "click", "target": "text='Sign in'"}
    ]
