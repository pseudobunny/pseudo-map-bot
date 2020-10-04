import discord
from item_utils.TogItem import TogItem
from .balance_set import bal_set
from .json_utils import read_from_json
from .balance_banker_set import check_name

async def balance_buy(client, mess):

    params = mess.content.split()[1:]
    try:
        item = TogItem(params)
        
        if item.conflict:
            await mess.channel.send("Please format as \"bal.buy [flags] [item] [rank/grade]\"")
            return
        else:
            
            balances = read_from_json()

            if check_name(mess.author.name,list(balances.keys())):
                new_bal = balances[mess.author.name] - item.price
                if new_bal > 0:
                    buy_msg = await mess.channel.send(f"So, {mess.author.mention}, you want to buy a {item.fetch_rank_grade()}{item.fetch_ig_com()}{item.name} for {item.price} credits?")
                    await buy_msg.add_reaction('👍') 
                    await buy_msg.add_reaction('👎')
                    confirm, _ = await client.wait_for('reaction_add', check = lambda react, user: user == mess.author)
                    if str(confirm.emoji) == '👍':
                        bal_set(mess.author.name, new_bal)
                        await mess.channel.send(f"{mess.author.mention}, you have bought the item!. Your new balance is {new_bal}.")
                    elif str(confirm.emoji) == '👎':
                        await mess.channel.send("No item bought. Cheapskate.")
                    else:
                        await mess.channel.send("Wrong reaction. Try buying again, please.")
                else:
                    await mess.channel.send(f"{mess.author.mention}, you don't have enough credits! You need {abs(new_bal)} more credits!")
            else:
                await mess.channel.send(f"{mess.author.mention}, looks like you don't have a balance... let me set that up for you.")
                bal_set(mess.author.name, 0)
                await mess.channel.send(f"Which also means you can't buy that item. Sorry!")
    except:
        await mess.channel.send("Please format as \"bal.buy [flags] [item] [rank/grade]\"")