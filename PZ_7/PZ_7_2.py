# Дана строка, содержащая цифры и строчные латинские буквы.
# Если буквы в строке упорядочены по алфавиту, то вывести 0;
# в противном случае вывести номер первого символа строки, нарушающего алфавитный порядок.

try:
    def check_alphabetical_order(s):
        for i in range(1, len(s)):
            if s[i] < s[i - 1]:
                return i
        return 0


    s = "abcde123"
    result = check_alphabetical_order(s)
    print(result)

except ValueError:
    print("Ошибка")