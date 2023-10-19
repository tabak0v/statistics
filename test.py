import pandas as pd

data = {
  "GPA": 5,
  "cleaner": "Сами убираете комнату",
  "grade": "9 класс",
  "residents": "Живу в комнате с кем-то",
  "room_type": "Достаточно чисто",
  "school": "ГБОУ Школа №57",
  "sex": "Мужской"
}
df0 = pd.read_csv('data.csv', delimiter=',')
df = pd.DataFrame(data, index=[df0.shape[0] + 1])
df.to_csv('data.csv', mode='a', index=False, header=False)
