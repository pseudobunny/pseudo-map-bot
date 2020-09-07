import discord
from .char_readv2 import collect_char_embs
from .char_json import char_json

async def char_firstup(chan,g_chans):

    try:
        char_embs, char_chans = collect_char_embs()
        
        uni_chans = []
        char_chans_true = []
        for i in range(len(char_chans)):
            char_chans_true.append(discord.utils.find(lambda c: c.name == char_chans[i], g_chans))
            if not (char_chans_true[i] in uni_chans):
                uni_chans.append(char_chans_true[i])
                await char_chans_true[i].purge(limit = None)

        for i in range(len(char_embs)):
            char_dict = char_embs[i].to_dict()
            char_msg = await char_chans_true[i].send(content = None, embed = char_embs[i])
            char_json(char_dict['title'], char_msg)
    except:
        await chan.send("Failed to collect characters.")