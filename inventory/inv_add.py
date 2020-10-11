from .inv_utils import read_from_json, write_to_json
from .inv_item import Inv_Item

async def add_item(mess):

    try:
        data = read_from_json()
    except:
        data = {}

    item = Inv_Item(mess.content.split()[1:])

    if item.error:
        await mess.channel.send(f"{mess.author.mention}, there was an error processing your item due to: {item.error}. Sorry!")
        return

    if mess.author.name in list(data.keys()):
        data[mess.author.name].append(item.to_dict())
    else:
        data.update({mess.author.name: [item.to_dict()]})

    write_to_json(data)

    await mess.channel.send(f"{mess.author.mention}, your {item.name} has been added to your inventory!")