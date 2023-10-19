import pandas as pd

data = {
        "ID": "2",
        "GPA": "4.35",
        "cleaner": "Уборкой занимается кто-то другой",
        "grade": "10 класс",
        "residents": "Живу в комнате с кем-то",
        "room_type": "Идеально чисто",
        "school": "ГБОУ Лицей Вторая школа",
        "sex": "Мужской"
        }
df = pd.DataFrame(data, index=[int(data["ID"])])
df.to_csv('data.csv', mode='a', index=False)
