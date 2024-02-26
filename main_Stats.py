from pstats import Stats
from re import match
import OneSol

class main_Stats(object):
    def __init__(self, deltas, max_value):
        self.deltas = deltas
        self.max_value = max_value
        self.stats = [0,0,0,0]
    def Calc(self,solution: OneSol):
        for i in range(4):
            x = 0
            match solution[i]:
                case 0: x -= self.deltas[0]
                case 1: x -= self.deltas[1]
                case 2: x -= self.deltas[2]
                case 4: x += self.deltas[2]
                case 5: x += self.deltas[1]
                case 6: x += self.deltas[0]                    
            self.stats[i] += x
        pass
    pass