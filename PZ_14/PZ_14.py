# Из исходного текстового файла (hotline.txt) перенести в первый файл строки с
# корректными номерами телефонов (т.е. в номере должно быть 11 цифр, например,
# 86532547891), а во второй с некорректными номерами телефонов.
# Посчитать полученные строки в каждом файле.

try:
    import re


    def is_valid_phone(phone):
        # Удаляем все нецифровые символы и проверяем длину
        digits = re.sub(r'\D', '', phone)
        return len(digits) == 11


    def process_hotlines(input_file, correct_file, incorrect_file):
        correct_count = 0
        incorrect_count = 0

        with open(input_file, 'r', encoding='utf-8') as infile, \
                open(correct_file, 'w', encoding='utf-8') as cor_file, \
                open(incorrect_file, 'w', encoding='utf-8') as incor_file:

            for line in infile:
                # Извлекаем номер телефона из строки
                phone_match = re.search(r' - (\D*\d[\d\D]*)', line)
                if phone_match:
                    phone = phone_match.group(1).strip()
                    if is_valid_phone(phone):
                        cor_file.write(line)
                        correct_count += 1
                    else:
                        incor_file.write(line)
                        incorrect_count += 1

        return correct_count, incorrect_count


    input_file = 'hotline.txt'
    correct_file = 'correct_hotlines.txt'
    incorrect_file = 'incorrect_hotlines.txt'

    correct_count, incorrect_count = process_hotlines(input_file, correct_file, incorrect_file)

    print(f'Количество строк с корректными номерами: {correct_count}')
    print(f'Количество строк с некорректными номерами: {incorrect_count}')

except ValueError:
    print("Ошибка")