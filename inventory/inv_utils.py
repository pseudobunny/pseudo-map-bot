import json
import discord

def write_to_json(data):
    with open('char_inventories.json', 'w') as f:
        json.dump(data, f, indent=4, separators=(", ", ": "), sort_keys=True)

def read_from_json():
    with open('char_inventories.json', 'r') as f:
        return json.load(f)

def to_embed(name, item_dict):

    item_embed = discord.Embed(title = name + "'s " + item_dict['name'])

    if "qp" in list(item_dict.keys()):
        item_embed.add_field(name = "QP", value = item_dict['qp'], inline = False)
    if "dc" in list(item_dict.keys()):
        item_embed.add_field(name = "DC", value = item_dict['dc'], inline = False)
    if "price" in list(item_dict.keys()):
        item_embed.add_field(name = "Price", value = item_dict['price'], inline = False)

    item_embed.add_field(name = "Description", value = item_dict['desc'], inline = False)

    return item_embed