import fractions

# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def convert_number(num: int, mode: str) -> str:
    result = ''
    convert: int = 2
    match mode:
        case "bin":
            convert = 2
        case "oct":
            convert = 8
        case "hex":
            convert = 16
    while num >= 1:
        res = num % convert
        if convert == 16:
            if res == 10:
                res = 'a'
            if res == 11:
                res = 'b'
            if res == 12:
                res = 'c'
            if res == 13:
                res = 'd'
            if res == 14:
                res = 'e'
            if res == 15:
                res = 'f'
        result += str(res)
        num = num // convert
    return result[::-1]


print(convert_number(21, mode="bin"), f"assert: {bin(21)}")
print(convert_number(21, mode="oct"), f"assert: {oct(21)}")
print(convert_number(1200, mode="hex"), f"assert: {hex(1200)}")
