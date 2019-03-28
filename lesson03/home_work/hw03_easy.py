# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    frac_part = number % 1 * (10 ** ndigits)
    if frac_part % 1 * 10 // 1 > 4:
        frac_part +=1
    return (number // 1) + (frac_part // 1 * (10 ** -ndigits))

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    def sum_func(num):
        return sum([int(i) for i in num])

    if len(str(ticket_number)) != 6:
        return 'You input wrong number'
    elif sum_func(str(ticket_number)[:3]) == sum_func(str(ticket_number)[3:]):
        return 'It is your lucky day! You WIN!'
    else:
        return 'You loose :('


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
