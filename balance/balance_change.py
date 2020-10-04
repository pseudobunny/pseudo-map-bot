from .json_utils import read_from_json, write_to_json
from .balance_set import bal_set

def op(com):
    op_name = com.split(".")[1]

    if op_name == "add":
        return 1
    if op_name == "sub":
        return -1

async def bal_change(mess):

    params = mess.content.split()
    params[0] = op(params[0])
    params[1] = int(params[1])

    balances = read_from_json()

    try:
        if mess.author.name in list(balances.keys()):
            new_bal = balances[mess.author.name] + (params[0] * params[1])
            bal_set(mess.author.name, new_bal)
            await mess.channel.send(f"{mess.author.mention}, your new balance is {new_bal} credits.")
        else:
            await mess.channel.send(f"{mess.author.mention}, sorry... we couldn't find your balance to add to! We'll set one up for you.")
            new_bal = (params[0] * params[1])
            bal_set(mess.author.name, new_bal)
            await mess.channel.send(f"{mess.author.mention}, your new balance is {new_bal} credits.")
    except:
        await mess.channel.send(f"{mess.author.mention}, please format your balance change as bal.[add/sub] [amount].")