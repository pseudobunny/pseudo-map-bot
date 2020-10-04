from .map_tile import map_tiles
from emoji import UNICODE_EMOJI
import re

async def add_map_char(mess):

    try:
        params = mess.content.split()[1:]
        name = params[0]
        emoji = params[1]

        if re.search(r'<:\w*:\d*>', emoji) != None:
            guild_emojis = mess.guild.emojis
            emoji_name = emoji.split(":")[1]
            for e in guild_emojis:
                if e.name == emoji_name:
                    map_tiles.update({name: emoji})
                    await mess.channel.send(f"{mess.author.mention}, {emoji} was added under the name {name}.")
                    break
        elif emoji in UNICODE_EMOJI:
            map_tiles.update({name: emoji})
            await mess.channel.send(f"{mess.author.mention}, {emoji} was added under the name {name}.")
        else:
            await mess.channel.send("Unable to find the specified emoji. Please make sure you are using a valid emoji for this server.\n Please use the command form map.add [name] [emoji].")
    except:
        await mess.channel.send("Please use the command form map.add [name] [emoji].")
    