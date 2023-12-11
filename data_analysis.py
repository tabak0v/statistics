import numpy as np
import pandas as pd
import scipy
import graphs


def cramers_v(crosstab):
    chi2 = scipy.stats.chi2_contingency(crosstab)[0]
    return np.sqrt(chi2 / (crosstab.sum().sum() * (min(crosstab.shape) - 1)))


def check_school(school):
    if school == "ГБОУ Школа №57":
        return 1
    elif school == "ГБОУ Школа №179":
        return 2
    elif school == "ГБОУ Лицей Вторая школа":
        return 3
    elif school == "Школа ЦПМ":
        return 4
    elif school == 'Школа "Летово"':
        return 5
    elif school == 'ГБОУ Школа №2007':
        return 6
    else:
        return 7


def check_room(room):
    if room == "Идеально чисто":
        return 1
    elif room == "Достаточно чисто":
        return 2
    elif room == "Не очень чисто":
        return 3
    else:
        return 4


# аггрегация данных
data = pd.read_csv('data.csv', delimiter=',')
data["school"] = data["school"].apply(lambda x: check_school(x))
data["sex"] = data["sex"].apply(lambda x: 'male' if x == "Мужской" else "female")
data["room_type"] = data["room_type"].apply(lambda x: check_room(x))
data["cleaner"] = data["cleaner"].apply(lambda x: "me" if x == "Сами убираете комнату" else "other")
data["residents"] = data["residents"].apply(lambda x: "1" if x == "Живу в комнате один/одна" else "1+")
data["grade"] = data["grade"].apply(lambda x: int(x[:-5]))

print(data.head(10))
