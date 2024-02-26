import Stats
import DeltaCalc

with open("input.txt") as f:
    res = []
    for rows in f:
        res.append(rows.split)
        
table = []

for row in res:
    nrow = []
    for x in row:
        x = int(x)
        nrow.append(x)
    table.append(nrow)
        
buff = DeltaCalc.DeltaCalc(7)

max_value = buff[0]
deltas = buff[1::]