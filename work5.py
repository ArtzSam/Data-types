input_string = input("Введите строку с раскладкой ENG: ")


def count_x_and_y(string):
    x = string.count('x')
    y = string.count('y')
    result_string = f'x: {x}, y: {y}.'
    return result_string


result = count_x_and_y(input_string)
print(result)
