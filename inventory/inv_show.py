from .inv_utils import read_from_json, to_embed
import discord

async def show_inv(mess):

    try:
        data = read_from_json()
    except:
        await mess.channel.send(f"{mess.author.mention}, there are no inventories yet... Add an item to start!")
        return

    if len(mess.content.split()) > 1:

        if mess.author.name in list(data.keys()):

            items = data[mess.author.name]
            to_search = " ".join(mess.content.split()[1:])

            for item in items:

                if to_search.lower() in item['name'].lower():
                    await mess.channel.send(content = None, embed = to_embed(mess.author.name,item))
                    return

            await mess.channel.send(f"{mess.author.mention} - sorry, we couldn't find your {to_search} in your inventory.")

        else:

            await mess.channel.send(f"{mess.author.mention}, sorry - you don't have an inventory. Why don't you add some items?")

    elif mess.author.name in list(data.keys()):

        item_list_embed = discord.Embed()
        item_string = ""

        for item in data[mess.author.name]:

            item_string += item['name']

            if 'price' in list(item.keys()):
                item_string += f" ({item['price']} credits)"

            item_string += "\n"

        item_list_embed.add_field(name = mess.author.name + "'s Items", value = item_string)

        await mess.channel.send(content = None, embed = item_list_embed)

    else:
        
        await mess.channel.send(f"{mess.author.mention}, sorry - you don't have an inventory. Why don't you add some items?")