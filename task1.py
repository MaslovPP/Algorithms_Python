# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
def sum_of_digit(num: int) -> int:
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum

print(sum_of_digit(193))

def prod_of_digit(num2: int) -> int:
    prod = 1
    while num2 > 0:
        prod = prod * (num2 % 10)
        num2 = num2 // 10
    return prod

print(prod_of_digit(193))

# Возник вопрос, можно ли эти 2 функции объеденить в одну? У самого пока не получилось.
# Ниже представляю свое первое решение, хотел здать его, но после просмотра второго вебинара вспомнил, что изучаем алгоритмы =)
# a, b, c = [int(i) for i in input('Введите трехзначное число: ')]
# summ = a + b + c
# product = a * b * c
# print(f'Сумма: {summ}\n'
#      f'Произведение: {product}')
