class NegativeNumberError(Exception):
    def __init__(self, number, message="Число не должно быть отрицательным."):
        self.number = number
        self.message = f"{message} Передано: {number}"
        super().__init__(self.message)

    def __str__(self):
        return self.message

def check_positive_number(number):
    if number < 0:
        raise NegativeNumberError(number)
    print(f"Число {number} является положительным.")

# Тесты
try:
    check_positive_number(-5)  # Ожидается исключение
except NegativeNumberError as e:
    print(e)

check_positive_number(10)  # Ожидается успешная проверка
