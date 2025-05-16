# Из предложенного текстового файла (text18-3.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках. Сформировать новый файл,
# в который поместить текст в стихотворной форме предварительно заменив символы третей строки их числовыми кодами.

try:
    import string

    with open('text18-3.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        print(line.strip())

    punctuation_count = 0
    for i in range(min(4, len(lines))):
        punctuation_count += sum(1 for char in lines[i] if char in string.punctuation)

    print(f'\nКоличество знаков пунктуации в первых четырёх строках: {punctuation_count}')

    third_line = lines[2]
    encoded_third_line = ' '.join(str(ord(char)) for char in third_line)
    lines[2] = encoded_third_line + '\n'

    with open('output_poem.txt', 'w', encoding='utf-8') as output_file:
        for line in lines:
            output_file.write(line)

except ValueError:
    print("Ошибка")
