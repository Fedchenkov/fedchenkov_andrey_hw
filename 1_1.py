# Реализовать вывод информации о промежутке времени в зависимости от его
# продолжительности duration в секундах:
# a. до минуты: <s> сек;
# b. до часа: <m> мин <s> сек;
# c. до суток: <h> час <m> мин <s> сек;
# d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек

user_second = int(input("Введите количество секунд: "))
if user_second >= 60 and user_second < 3600:
    minutes = user_second // 60
    second = user_second % 60
    print(minutes, "min", second, "sec")
elif user_second >= 3600:
    hours = user_second // 3600
    minutes = (user_second % 3600) // 60
    second = user_second % 60
    print(hours, "hour", minutes, "min", second, "sec")
else:
    print(user_second, "sec")