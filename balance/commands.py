from balance import balance_show, bal_change, bank_set, balance_buy

async def run_bal_command(message, client):

    if message.content.startswith("bal.show"):
        await balance_show(message)
    
    #elif message.content.startswith("bal.add") or message.content.startswith("bal.sub"):
    #    await bal_change(message)

    elif message.content.startswith("bal.bank"):
        await bank_set(message)

    elif message.content.startswith("bal.buy"):
        await balance_buy(client,message)

    else:
        await message.channel.send(f"The command {message.content.split()[0].split('.')[1]} is not available in the balance package.")