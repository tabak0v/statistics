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
data = data[["Ваш пол",
             "Способ уборки",
             "Проживание в комнате",
             "Класс обучения",
             "На какую картинку больше похожа ваша комната? (Примеры сверху)",
             "Школа",
             "Общий средний балл за прошлый учебный год"]]
data.columns = data.columns.str.replace(' ', '_')
data.columns = ["sex",
                "type_clean",
                "roommate",
                "class",
                "room_type",
                "school",
                "grade"]

data["grade"] = data["grade"].apply(lambda x: float(x.replace(',', '.')))
data["school"] = data["school"].apply(lambda x: check_school(x))
data["sex"] = data["sex"].apply(lambda x: 'male' if x == "Мужской" else "female")
data["room_type"] = data["room_type"].apply(lambda x: check_room(x))
data["type_clean"] = data["type_clean"].apply(lambda x: "me" if x == "Сами убираете комнату" else "other")
data["roommate"] = data["roommate"].apply(lambda x: "1" if x == "Живу в комнате один/одна" else "1+")
data["class"] = data["class"].apply(lambda x: int(x[:-5]))

cross_table = pd.crosstab(data["room_type"], data["grade"])
print(round(cramers_v(cross_table), 4))

'''
graphs.box_plot(data)
'''

problems = ["sex",
            "type_clean",
            "roommate",
            "class",
            "room_type",
            "school"]
results = []
for problem in problems:
    problem_type = data[problem]
    col = data['grade']
    contingency_table = pd.crosstab(col, problem_type)
    chi2, p, _, _ = scipy.stats.chi2_contingency(contingency_table)
    results.append([problem, round(p, 4)])
results.sort(key=lambda x: x[1])
ans = [['показатель', 'р-уровень']]
for elem in results:
    ans.append(elem)
print(ans)

print(data.head(10))
