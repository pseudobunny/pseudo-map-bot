import discord
from .json_utils import read_from_json
from .balance_set import bal_set

async def balance_show(mess):

    try:
        balances = read_from_json()

        if mess.author.name in list(balances.keys()):
            await mess.channel.send(f"{mess.author.mention}, your balance is {balances[mess.author.name]} credits.")
        else:
            await mess.channel.send(f"{mess.author.mention}, you do not have a balance. Don't worry though, one is being set for you.")
            bal_set(mess.author.name, 0)
    except:
        await mess.channel.send(f"{mess.author.mention}, there are no balances yet! Let us set one for you.")
        bal_set(mess.author.name, 0)