import discord

async def item_help(chan):
    help_emb = discord.Embed(title = "Item Price Commands")
    help_emb.add_field(name = "Check the price of an item:", value = "item.price [optional flags] [item name] [rank/grade]", inline = False)
    help_emb.add_field(name = "Rank/Grade", value = "Format the style in [Rank][Grade]\n Examples: F10, E3, B0", inline = False)
    help_emb.add_field(name = "Optional Flags", value = "-it: Searches for name in the item category\n-m: Searches for name in the melee category\n-r: Searches for name in the ranged category\n-t: Searches for name in the thrown category\nOnly one category flag can be used at one time.\n\n-i: Specifies that the item is an ignition item.\n-c: Specifies that the item is a compressed item.\nOnly one special property can be specified at one time.", inline = False)
    await chan.send(content = None, embed = help_emb)