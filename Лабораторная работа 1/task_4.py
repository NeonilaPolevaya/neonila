users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

statistic_dict = {'Общее количество' : 0, 'Уникальные посещения' : 0}

statistic_dict['Общее количество'] = len(users)

statistic_dict['Уникальные посещения'] = len(set(users))

print(statistic_dict)