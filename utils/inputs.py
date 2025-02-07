class TakeInput:
    def __init__(self, no, div):
        self.no = no # number
        self.div = div #division
        self.depriming = self.no -1
        self.new_div = self.depriming / self.div
    def calculate(self):
        return "L+{}G{}".format(self.div,self.new_div)