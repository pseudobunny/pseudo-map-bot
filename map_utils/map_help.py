import discord

async def map_help(chan):
    help_emb = discord.Embed(title = "Commands")
    help_emb.add_field(name = "Create a map:", value = "map.create \{rows\} \{columns\}", inline = False)
    help_emb.add_field(name = "Add a token to the map:", value = "map.update \{row\} \{columns\} \{token\}\n\nRows and columns start at zero in the top right corner.\nTokens are the numbers 1 - 9.", inline = False)
    help_emb.add_field(name = "Move a token around the map:", value = "map.cmove \{token\} \{direction\} \{move amount\}\n\nA token cannot move out of map area or onto another token.\nValid directions are up, down, left, right.", inline = False)
    help_emb.add_field(name = "Remove a token from the map:", value = "map.cremove \{token\}", inline = False)
    help_emb.add_field(name = "Send the map again in a channel:",value = "map.redraw", inline = False)
    help_emb.add_field(name = "Close the map:", value = "map.close", inline = False)
    help_emb.add_field(name = "View the commands:", value = "map.help", inline = False)

    await chan.send(content = None, embed = help_emb)