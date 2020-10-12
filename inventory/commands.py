from inventory import add_item, show_inv

async def run_inv_command(message, client):

    if message.content.startswith("inv.add"):
        await add_item(message)

    elif message.content.startswith("inv.show"):
        await show_inv(message)

    else:
        await message.channel.send(f"The command {message.content.split()[0].split('.')[1]} is not available in the inventory package.")