class calculator:
    #your code here
    def __init__(self, v=[]) -> None:
        self.v = v
    def __add__(self, obj) -> None:
        return calculator([x + obj for x in self.v])
    def __mul__(self, obj) -> None:
        return calculator([x * obj for x in self.v])
    def __sub__(self, obj) -> None:
        return calculator([x - obj for x in self.v])
    def __truediv__(self, obj):
        return calculator([x / obj for x in self.v])
    def __repr__(self):
        return str(self.v)