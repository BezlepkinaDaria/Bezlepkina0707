# Из исходного текстового файла (hotline.txt) перенести в первый файл строки с
# корректными номерами телефонов (т.е. в номере должно быть 11 цифр, например,
# 86532547891), а во второй с некорректными номерами телефонов.
# Посчитать полученные строки в каждом файле.

try:
    import re


    def is_valid_phone(phone):
        return bool(re.fullmatch(r'^\d{11}$', phone.strip()))


    with open('hotline.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    valid_phones = []
    invalid_phones = []

    for line in lines:
        phone = line.strip()
        if is_valid_phone(phone):
            valid_phones.append(phone)
        else:
            invalid_phones.append(phone)

    with open('valid_phones.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(valid_phones))

    with open('invalid_phones.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(invalid_phones))

    print(f"Корректных номеров: {len(valid_phones)}")
    print(f"Некорректных номеров: {len(invalid_phones)}")

except ValueError:
    print("Ошибка")