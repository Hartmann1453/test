import pandas as pd

sp_offise = [
    [200, 1300, 'Бабушкин', 'Валера'],
    [300, 1200, 'Евро', 'Петя'],
    [400, 1100, 'Евро', 'Саша'],
    [500, 1000, 'Бабушкин', 'Маша'],
    [600, 900, 'Евро', 'Валя'],
    [700, 800, 'Евро', 'Ваня'],
    [800, 700, 'Бабушкин', 'Леша'],
    [900, 600, 'Евро', 'Лида'],
    [1000, 500, 'Евро', 'Никита'],
    [1100, 400, 'Бабушкин', 'Настя'],
    [1200, 300, 'Евро', 'Булкин'],
    [348, 702, 'Бабушкин', 'Валера'],
    [348, 695, 'Евро', 'Петя'],
    [352, 702, 'Евро', 'Саша'],
    [352, 695, 'Бабушкин', 'Маша']
]

new_sp = []
for office in sp_offise:
    if office[0] > 350:
        continue
    if office[1] < 700:
        continue
    new_sp.append(office)

df_1 = pd.DataFrame(new_sp,
    columns = ['Номер офиса', 'Количество сотрудников', 'Ремонт', 'Начальник']
)

df = pd.concat([df_1])
df.reset_index(drop = True, inplace = True)
print(df)