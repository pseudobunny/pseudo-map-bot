import discord
from .json_utils import read_from_json, write_to_json

def check_name(name, name_list):

    for n in name_list:
        if name in n:
            return True, n

    return False, ""

async def bank_set(mess):

    role_names = []
    for role in mess.author.roles:
        role_names.append(role.name)

    if "Banker" in role_names:
        params = mess.content.split()[1:]

        balances = read_from_json()

        try:
            check, true_name = check_name(params[0],list(balances.keys()))
            if check:
                
                if params[1] == "add":
                    balances[true_name] += int(params[2])
                if params[1] == "sub":
                    balances[true_name] -= int(params[2])
                if params[1] == "set":
                    balances[true_name] = int(params[2])
                
                write_to_json(balances)
                await mess.channel.send(f"{mess.author.mention}, {true_name}'s new balance is now {balances[true_name]} credits.")

            else:
                await mess.channel.send(f"{mess.author.mention}, sorry... we could not find the user's balance.")

        except:
            await mess.channel.send(f"{mess.author.mention}, please format as bal.bank [name] [add/sub/set] [amount].")

    else:
        await mess.channel.send(f"Wait... {mess.author.mention}... YOU AREN'T A BANKER! WE ARE ALERTING THE AUTHORITIES.")
        
