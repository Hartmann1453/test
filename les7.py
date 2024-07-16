import seaborn as sns
import matplotlib.pyplot as plt

x = ['Space Engeenirs', 'Kerbal Space Programm', 'Космические Рейнджеры', 'X4: Foundation', 'Stelaris']
y = [150000, 45000, 450000, 300000, 10000]
sns.barplot(x=x, y=y, color='black')
plt.show()