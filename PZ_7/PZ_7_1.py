# Дан символ C.
# Вывести два символа, первый из которых предшествует символу C в кодовой таблице, а второй следует за символом C.

try:
    def prev_next_symbols(char):
        prev_char = chr(ord(char) - 1)
        next_char = chr(ord(char) + 1)
        return prev_char, next_char


    symbol = 'C'
    prev_symbol, next_symbol = prev_next_symbols(symbol)
    print(f"Предыдущий символ: {prev_symbol}, Следующий символ: {next_symbol}")

except ValueError:
    print("Ошибка")
