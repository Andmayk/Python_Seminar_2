# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно 
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть


number_of_coins = int(input("Введите количество монет: "))

print("Введите какой стороной лежат монеты:  0 - орел, 1 - решка ")

number_of_heads = 0
number_of_tails = 0

for i in range(number_of_coins):
    coin = int(input(f"монета {i+1} орёл или решка (0/1): "))

