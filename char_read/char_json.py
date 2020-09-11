import discord
import json

def write_to_json(data):
    with open('char_msgs.json', 'w') as f:
        json.dump(data, f, indent=4, separators=(", ", ": "), sort_keys=True)

def char_append(c_data, ch_id):
    with open('char_msgs.json', 'r') as f:
        total_data = json.load(f)

    try:
        total_data[str(ch_id)].append(c_data)
        print(total_data[str(ch_id)])
    except:
        new_data = {ch_id: [c_data]}
        total_data.update(new_data)

    write_to_json(total_data)

def char_json(char):

    c_data = char.to_dict()

    try:
        char_append(c_data, char.chan_obj.id)
    except:
        new_data = {char.chan_obj.id: [c_data]}
        write_to_json(new_data)

def json_reset():
    with open('char_msgs.json', 'w') as f:
        json.dump({}, f, indent=4, separators=(", ", ": "), sort_keys=True)