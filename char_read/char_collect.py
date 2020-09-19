import discord
import os
import json

class TtChar:

    def emb_filling(self, c_dict):

        traits = c_dict[self.name]

        for trait in traits:
            if trait == "Channel":
                self.chan_name = traits[trait]
            else:
                self.emb.add_field(name = trait, value = traits[trait], inline = False)

    def load_json(self):
        with open(os.path.join(".\\tog_jsons", self.c_file), "r") as f:
            c_dict = json.load(f)
        
        self.emb.title = self.name = list(c_dict.keys())[0]
        self.emb_filling(c_dict)

    def __init__(self, c_file):
        self.emb = discord.Embed()
        self.chan_name = ""
        self.chan_id = 0
        self.chan_obj = None
        self.msg = None
        self.c_file = c_file
        self.name = ""
        self.load_json()

    def to_dict(self):
        return {self.name : {"msg_id": self.msg.id, "file name": self.c_file}}

    def find_chan_obj(self, g_chans):
        self.chan_obj = discord.utils.find(lambda c: c.name == self.chan_name, g_chans)

    async def send_msg(self):
        self.msg = await self.chan_obj.send(content = None, embed = self.emb)
    
    async def find_msg(self, m_id):
        self.msg = await self.chan_obj.fetch_message(m_id)

def collect_chars():

    char_list = []

    for c_file in os.listdir(".\\tog_jsons"):
        if c_file.endswith(".json"):
            char_list.append(TtChar(c_file))

    return char_list