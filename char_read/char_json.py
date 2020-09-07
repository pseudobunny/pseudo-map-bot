import discord
import json

def write_to_json(data):
    with open('char_msgs.json', 'w') as f:
        json.dump(data, f, indent=4, separators=(", ", ": "), sort_keys=True)

def char_append(c_data):
    with open('char_msgs.json', 'r') as f:
        total_data = json.load(f)
        
    total_data.update(c_data)

    write_to_json(total_data)

def char_json(name, msg):

    c_data = { name: {"msg_id" : msg.id, "chan_id" : msg.channel.id}}

    try:
        char_append(c_data)
    except:
        write_to_json(c_data)