from .TogItem import TogItem

async def item_price(mess):

    parameters = mess.content.split()[1:]
    try:
        item = TogItem(parameters)

        if item.conflict:
            await mess.channel.send(f"Hey, {mess.author.mention} there was an error with your flags: {item.conflict}")
            return

        if item.found:
            out_str = f"Hey, {mess.author.mention}, the price of a {item.fetch_rank_grade()}{item.fetch_ig_com()}{item.name} is {item.price} credits, and the item has {item.qp_mess} QP."
            if item.fetch_dc() != 0:
                out_str += item.fetch_dc()
            await mess.channel.send(out_str)
        else:
            await mess.channel.send(f"Sorry {mess.author.mention}, we could not find the {item.name} item. But if we did, it would be {item.qp} QP.")
    except:
        await mess.channel.send("Please format as \"item.price [flags] [item] [rank/grade]\"")