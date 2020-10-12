from char_read import char_firstup, char_update, char_add

async def run_chars_command(message, client):

    if message.content.startswith("chars.firstup"):
        
        await char_firstup(message.channel, message.guild.channels)

    elif message.content.startswith("chars.update"):
        
        await char_update(client, " ".join(message.content.split()[1:]))
        await message.delete()

    elif message.content.startswith("chars.add"):
        await char_add(message)

    else:
        await message.channel.send(f"The command {message.content.split()[0].split('.')[1]} is not available in the character package.")