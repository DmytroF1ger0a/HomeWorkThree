import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []

    numbers = random.sample(range(min, max + 1), quantity)

    numbers.sort()

    return numbers

# Приклад використання функції
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
# Приклад з 6 числами у діапазоні від 1 до 49
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

# Приклад з 5 числами у діапазоні від 1 до 36
lottery_numbers = get_numbers_ticket(1, 36, 5)
print("Ваші лотерейні числа:", lottery_numbers)

# Приклад з некоректними параметрами
lottery_numbers = get_numbers_ticket(1, 10, 11)
print("Ваші лотерейні числа:", lottery_numbers)
