# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, separator = ','):
    list1 = participants_first_group.split(sep = separator)
    list2 = participants_second_group.split(sep = separator)
    inter_set = set(list1).intersection(set(list2))
    new_list = list(inter_set)
    new_list.sort()
    return(new_list)



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, separator = '|'))

