import math
from re import M

def DeltaCalc(n):
    x = 1.65*((3*n/2)**0.5)
    x = round(x)
    a = math.ceil(x/2)
    b = round(x/3)
    c = x // 4
    res = x,a,b,c
    return res