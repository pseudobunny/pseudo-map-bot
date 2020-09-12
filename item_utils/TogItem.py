import json
from math import ceil

class TogItem:

    def set_base_price(self):
        with open("item_qualities.json", "r") as f:
            item_data = json.load(f)

        for item in list(item_data.keys()):
            if self.name.lower() in item.lower():
                self.base_price = item_data[item]["price"]
                self.name = item
                self.found = True
                return
        
        self.base_price = 0
        self.found = False
        return

    def get_rank_mult(self):

        if self.rank == 5:
            return 1e6
        else:
            return 10**(self.rank)

    def get_grade_mult(self):

        if self.grade == 0:
            return 15
        else:
            return 11 - self.grade

    def set_price(self):
        first = self.get_rank_mult()
        second = self.get_grade_mult()
        self.price = self.base_price * first * second

    def set_QP(self):
        self.qp = (self.rank*4)
        self.qp += ceil((11 - self.grade)/3)

    def __init__(self, params):

        self.name = " ".join(params[:len(params)-1])
        self.rank = 70 - ord(params[len(params)-1][0].upper())
        self.grade = int(params[len(params)-1][1:])
        self.set_base_price()
        self.set_price()
        self.set_QP()

    def fetch_rank_grade(self):
        return chr(70 - self.rank) + str(self.grade)