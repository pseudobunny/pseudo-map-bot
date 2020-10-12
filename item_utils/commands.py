from item_utils import item_price, item_help

async def run_item_command(message, client):

    if message.content.startswith("item.price"):
        await item_price(message)

    elif message.content.startswith("item.help"):
        await item_help(message.channel)

    else:
        await message.channel.send(f"The command {message.content.split()[0].split('.')[1]} is not available in the item package.")