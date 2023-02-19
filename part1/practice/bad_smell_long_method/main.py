# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;19"""


def read_data(csv_string):
    # Чтение данных из строки
    data = []
    for line in csv_string.split('\n'):
        name, age = line.split(';')
        data.append({'name': name, 'age': int(age)})
    return data


def sort_by_age(data):
    # Сортировка по возрасту по возрастанию
    new_data = []
    used_person = set()

    while len(used_person) != len(data):
        minimum_age_person = None
        for person in data:
            if person['name'] not in used_person and (
                    minimum_age_person is None or person['age'] < minimum_age_person['age']):
                minimum_age_person = person

        new_data.append(minimum_age_person)
        used_person.add(minimum_age_person['name'])

    return new_data


def filtration(data):
    # Фильтрация
    return [person for person in data if person['age'] >= 10]


def get_users_list(csv_string):
    data = read_data(csv_string)
    sorted_data = sort_by_age(data)
    filtered_data = filtration(sorted_data)
    return filtered_data


if __name__ == '__main__':
    print(get_users_list(csv))
