import pandas as pd
import matplotlib.pyplot as plt
import random

sp, sp2 = [], []
for i in range(10):
    sp.append(random.randint(10, 100))
    sp2.append(random.randint(10, 100))

fig, axes = plt.subplots(2, 1)
s, s2 = pd.Series(sp), pd.Series(sp2)    # Создаем две отдельные Оси
s.plot(ax = axes[0], color = 'red', alpha = 0.9)
s2.plot(ax = axes[1], color = 'blue', alpha = 0.8)
plt.show()
