# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100


numbers = list(range(1, 101))

for i in numbers:
    if numbers[i] % 10 == 1:
        print(numbers[i], "процент")
    elif numbers[i] % 10 < 5 and numbers[i] % 10 != 0:
        print(numbers[i], "процента")
    else:
        print(numbers[i], "процентов")



