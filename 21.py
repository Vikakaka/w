import re
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

new_list = []

for contact in contacts_list:
    contact_1 = list()
    pattern_1 = re.compile(r'([a-z]+)?(\+7\s*|8\s*)\(?(\d\d\d)\)?[- ]?(\d\d\d)?[- ]?(\d\d)[- ]?(\d\d)\s*\(?(['
                         r'а-я]+)?(\.\s*\d+)?\)?')
    phones = pattern_1.sub(r'\1 +7(\3)\4-\5-\6 \7\8', contact[5])
    contact[5] = phones
    name_str = ",".join(contact[:3])
    result = re.findall(r'(\w+)', name_str)
    while len(result) < 3:
        result.append('')
    contact_1 += result
    contact_1.append(contact[3])
    contact_1.append(contact[4])
    contact_1.append(contact[5])
    contact_1.append(contact[6])
    new_list.append(contact_1)

phone = dict()

for contact in new_list:
    if contact[0] in phone:
        contact_value = phone[contact[0]]
        for i in range(len(contact_value)):
            if contact[i]:
                contact_value[i] = contact[i]
    else:
        phone[contact[0]] = contact

with open("phonebook.csv", "w") as f:
    data_writer = csv.writer(f, delimiter=',')
    data_writer.writerows(list(phone.values()))

