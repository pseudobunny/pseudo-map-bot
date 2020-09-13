import json
from math import ceil

class TogItem:
    
    def set_base_price(self):
        with open("item_qualities.json", "r") as f:
            item_data = json.load(f)

        if self.name in self.flags:
            raise Exception("Flag for name")

        no_type_check = True
        type_flag = None
        for flag in self.flags:
            if flag in ["-t", "-r", "-m", "-it"]:
                no_type_check = False
                type_flag = self.flag_to_type[flag]
                break

        for item in list(item_data.keys()):
            if (self.name.lower() in item.lower()) and ((item_data[item]["type"] == type_flag) or no_type_check):
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

        if "-c" in self.flags:
            self.price *= 3

        if "-i" in self.flags:
            self.price *= 5

    def set_QP(self):
        self.qp = (self.rank*4)
        self.qp += ceil((11 - self.grade)/3)
        
        self.qp_mess = self.qp
        
        qp_increase = {"-i": {0: 10, 1: 5, 3: 3, 5: 1, 7: 0}, "-c": {3: 5, 5: 3, 7: 1}}
        if "-i" in self.flags:
            inc = self.qp + qp_increase["-i"][self.grade]
            self.qp_mess = f"{self.qp} QP, but when ignited it has {inc}"
        elif "-c" in self.flags:
            inc = self.qp + qp_increase["-c"][self.grade]
            self.qp_mess = f"{self.qp} QP, but when decompressed {inc}"

    def flag_conflicts(self):
        i = 0
        for flag in self.flags:
            if flag in ["-t", "-r", "-m", "-it"]:
                i += 1
        if i > 1:
            self.conflict = "two different item type flags"

        if ("-i" in self.flags) and ("-c" in self.flags):
            self.conflict = "both ignition and compression on the same item"

        if (("-i" in self.flags) and (not self.grade in [0,1,3,5,7])) or (("-c" in self.flags) and (not self.grade in [3,5,7])):
           self.conflict = "not the right grade for ignition or compression"

    def check_for_flags(self, params):
        n = 0
        for string in params[:len(params)-1]:
            if string[0] == "-":
                if string in self.accepted_flags:
                    self.flags.append(string)
                n += 1

        return params[n:]

    def __init__(self, params):
        self.accepted_flags = ["-t", "-r", "-m", "-i", "-c", "-it"]
        self.flag_to_type = {"-it": "item", "-r": "ranged", "-m": "melee", "-t": "thrown"}
        self.flags = []
        self.conflict = False
        params = self.check_for_flags(params)
        self.name = " ".join(params[:len(params)-1])
        self.rank = 70 - ord(params[len(params)-1][0].upper())
        self.grade = int(params[len(params)-1][1:])
        self.flag_conflicts()

        if self.conflict == False:
            self.set_base_price()
            self.set_price()
            self.set_QP()

    def fetch_rank_grade(self):
        return chr(70 - self.rank) + str(self.grade)

    def fetch_ig_com(self):
        if "-i" in self.flags:
            return " Ignition "
        elif "-c" in self.flags:
            return " Compressed "
        else:
            return " "

    def fetch_dc(self):
        if "-i" in self.flags:
            if self.grade == 0:
                DC = int(30 + self.qp)
            else:
                DC = int(10 + ((7 - self.grade)*2.5) + self.qp)
            return f" The DC for igniting is {DC}."

        elif "-c" in self.flags:
            DC = int(10 + ((7 - self.grade) + 1) + self.qp)
            return f" The DC for decompressing is {DC}."
        
        else:
            return 0