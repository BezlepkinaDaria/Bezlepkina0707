# Составить генератор (yield), который выводит из строки только цифры

try:
    def extract_digits(input_string):
        for char in input_string:
            if char.isdigit():
                yield char


    input_string = "abc123def456"
    digits = ''.join(extract_digits(input_string))

    print("Цифры из строки:", digits)

except ValueError:
    print("Ошибка")