text = input("Введите текст: ")
char = input("Введите символ для удвоения: ")


def double(text, char):
    result = text.replace(char, char * 2)
    return result


result_text = double(text, char)
print("Результат:", result_text)
