import discord
import json
import os
from .char_collect import TtChar
from .char_json import char_json, write_to_json

def open_json(string):

    with open(string, "r") as f:
        data = json.load(f)

    return data

async def char_add(mess):

    char_name = mess.content.split()[1]

    char_file = ""
    for c_file in os.listdir(".\\tog_jsons"):
        if c_file.endswith(".json") and (char_name in c_file):
            char_file = c_file

    try:
        char = TtChar(char_file)
        char.find_chan_obj(mess.guild.channels)

        msgs = open_json("char_msgs.json")
        
        if not (str(char.chan_obj.id) in list(msgs.keys())):
            await char.send_msg()
            char_json(char)
            await mess.delete()
            return

        current_chars = msgs[str(char.chan_obj.id)]
        current_chars_names = []
        for i in range(len(current_chars)):
            current_chars_names.append(list(current_chars[i].keys())[0])
        
        if char.name in current_chars_names:
            await mess.channel.send("Character already here! Use chars.update instead.")
            return

        current_chars_names.append(char.name)
        current_chars_names.sort()
        start_ind = current_chars_names.index(char.name)
        
        embeds = [char.emb]
        file_names = [char.c_file]
        await char.send_msg()
        c_msgs = [char.msg]
        c_names = [char.name]
        
        for c_char in current_chars[start_ind:]:
            name = list(c_char.keys())[0]
            c_names.append(name)
            
            file_names.append(c_char[name]["file name"])
            
            c_char_msg = await char.chan_obj.fetch_message(c_char[name]["msg_id"])
            embeds.append(c_char_msg.embeds[0])
            c_msgs.append(c_char_msg)

        c_msgs.append(c_msgs.pop(0))

        new_chars = []
        for i in range(len(embeds)):
            await c_msgs[i].edit(embed = embeds[i])
            new_chars.append({c_names[i] : {"msg_id": c_msgs[i].id, "file name": file_names[i]}})

        msgs[str(char.chan_obj.id)] = current_chars[:start_ind] + new_chars

        write_to_json(msgs)

        await mess.delete()

    except:
        await mess.channel.send("Could not find character file specified.")