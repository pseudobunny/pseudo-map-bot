from .TogItem import TogItem

async def item_price(mess):

    parameters = mess.content.split()[1:]
    try:
        item = TogItem(parameters)

        if item.found:
            await mess.channel.send(f"Hey, {mess.author.mention}, the price of a {item.fetch_rank_grade()} {item.name} is {item.price} credits, and the item has {item.qp} QP.")
        else:
            await mess.channel.send(f"Sorry {mess.author.mention}, we could not find the {item.name} item. But if we did, it would be {item.qp} QP.")
    except:
        await mess.channel.send("Please format as \"item.price [item] [rank/grade]\"")