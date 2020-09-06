import discord
from .char_readv2 import collect_char_embs

async def char_update(chan,g_chans):

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
            await char_chans_true[i].send(content = None, embed = char_embs[i])
    except:
        await chan.send("Failed to collect characters.")