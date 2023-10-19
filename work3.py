n = int(input("Введите натуральное число n - степень: "))
n_values = input("Введите список чисел через запятую: ")
numbers = [int(n) for n in n_values.split(",")]
result = [num**n for num in numbers]
print(result)