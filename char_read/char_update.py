import discord
import json
from .char_collect import TtChar

async def char_update(bot, char):

    with open("char_msgs.json", "r") as f:
        data = json.load(f)

    
    for chan in list(data.keys()):
        for j_char in data[chan]:
            c_name = list(j_char.keys())[0]
            if char in c_name:
                new_char = TtChar(j_char[c_name]["file name"])
                new_char.chan_obj = bot.get_channel(int(chan))
                new_char.msg = await new_char.chan_obj.fetch_message(j_char[c_name]["msg_id"])
                await new_char.msg.edit(embed = new_char.emb)