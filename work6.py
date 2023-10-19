input_text = input("Введите текст со скобками: ")
def remove(text):
    result = ""
    while True:
        open = text.find('(')
        if open == -1:
            break

        close = text.find(')', open)
        if close == -1:
            break

        result += text[open + 1:close] + "\n"

        text = text[close + 1:]

    return result.strip()


output_text = remove(input_text)
print(output_text)