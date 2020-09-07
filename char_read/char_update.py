import discord
import json
from .char_readv2 import *

async def char_update(bot, char):

    with open("char_msgs.json", "r") as f:
        data = json.load(f)

    for data_c in data:
        if char in data_c:
            c_file_name = data[data_c]["file name"]
            char_file = open(os.path.join(".\\tog_chars", c_file_name), "r")
            traits = collect_traits(char_file)
            
            chan = bot.get_channel(data[data_c]['chan_id'])
            msg = await chan.fetch_message(data[data_c]['msg_id'])
            await msg.edit(embed = build_emb(traits))