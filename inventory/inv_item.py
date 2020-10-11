from item_utils.TogItem import TogItem
import re

class Inv_Item:

    def get_tog_item(self, params):
        
        item = TogItem(params)
        if item.conflict == False:
            self.price = item.price
            self.name = item.fetch_rank_grade() + item.fetch_ig_com() + item.name
            self.QP = item.qp
            self.DC = item.fetch_dc()
        else:
            self.error = item.conflict

    def __init__(self, params):

        self.error = False
        self.name = ""
        self.QP = ""
        self.DC = ""
        self.price = ""

        desc_start = params.index('-d')
        desc_params = params[desc_start+1:]
        self.desc = " ".join(desc_params)
        params = params[:desc_start]

        if params[0] == '-s':
            self.get_tog_item(params[1:])
            return
        #item.add -qp [QP] [name] -d [description]
        elif params[0] == '-qp':
            self.QP = params[1]
            params = params[2:]
        self.name = " ".join(params)

    def to_dict(self):
        item_dict = {'name': self.name, "desc": self.desc}
        if self.QP != "" and self.QP != None:
            item_dict['qp'] = self.QP
        if self.DC != "" and self.DC != None:
            item_dict['dc'] = self.DC
        if self.price != "" and self.price != None:
            item_dict['price'] = self.price
        return item_dict