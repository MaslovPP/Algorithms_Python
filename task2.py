# 2. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

def func(ch1: str, ch2: str):
    place_1 = ord(ch1) - ord('a') + 1
    place_2 = ord(ch2) - ord('a') + 1
    if place_1 == place_2:
        return

# Не совсем понимаю решение, а именно, почему нельзя ord(ch1) - ord(ch2), ведь ord указывает позицию, насколько я понял.
# А так же, хотелось бы понять, как решать с помощью input.
# Прошу пояснить, если есть такая возможность.

# a = input('Введите первую букву (латиница, нижний регистр):')
# b = input('Введите вторую букву (латиница, нижний регистр):')
# eng_low_alphabet = list('abcdefghijklmnopqrstuvwxyz')
# let_a_index = eng_low_alphabet.index(a) + 1
# let_b_index = eng_low_alphabet.index(b) + 1
# let_c_index = let_b_index - let_a_index
# print(f'{a} - {let_a_index} буква в алфавите.\n'
#       f'{b} - {let_b_index} буква в алфавите.\n'
#       f'Расстояние между буквами: {let_c_index}')
