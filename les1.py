import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
f = open('dz.csv')
lines = 0

massive_click = []
massive_pokaz = []

for i in f:
    lines += 1
    if lines == 1:
        continue
    row = i.split(';')

    count_click = int(row[0])
    count_pokaz = int(row[1])

    massive_click.append(count_click)
    massive_pokaz.append(count_pokaz)

plt.plot(massive_click)
plt.plot(massive_pokaz)
plt.show()
