# Ввод: In the hole in the ground there lived a hobbit
string = input("Введите строку (не менее 15 символов): ")

if len(string) < 15:
    print("Введена строка слишком короткая.")
else:
    # slize [ 0 - 0 - step ]
    output = string[::2]
    print("Результат:", output)

# Вывод: I h oei h rudteelvdahbi

# else:
#   output = string[::2]
#   print("Результат:", output)
#   break