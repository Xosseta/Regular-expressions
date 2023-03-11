from pprint import pprint
import csv
import re
# Читаем адресную книгу в формате CSV в список contacts_list:


with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

# 1. Выполните пункты 1-3 задания.
# Ваш код
PHONE_SEARCH_PATTERN = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
PHONE_SUB_PATTERN = r'+7(\2)-\3-\4-\5 \6\7'


def process_raw_data(data):
    result = list()
    for row in data:
        record = list()
        full_name = re.findall(r'(\w+)', ' '.join(row[:3]))
        full_name.append('') if len(full_name) < 3 else ...
        record += full_name
        record.append(row[3])
        record.append(row[4])
        record.append(re.sub(PHONE_SEARCH_PATTERN, PHONE_SUB_PATTERN, row[5]).strip())
        record.append(row[6])
        result.append(record)
    return result


def make_pure_contact_list(data):
    result = dict()
    for item in data:
        result[item[0]] = merge_doubles(item, result[item[0]]) if item[0] in result else item
    return result.values()


def merge_doubles(record_one, record_two):
    result = list()
    for index in range(len(record_one)):
        result.append(record_one[index]) if record_one[index] else result.append(record_two[index])
    return result


contact_list_with_doubles = process_raw_data(contacts_list)
pure_contact_list = make_pure_contact_list(contact_list_with_doubles)
# 2. Сохраните получившиеся данные в другой файл.
# Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(pure_contact_list)