import json

def write_to_json(data):
    with open('char_balances.json', 'w') as f:
        json.dump(data, f, indent=4, separators=(", ", ": "), sort_keys=True)

def read_from_json():
    with open('char_balances.json', 'r') as f:
        return json.load(f)