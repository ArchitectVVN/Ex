def validate_user_input(data):
    try:
        if not isinstance(data, dict):
            raise TypeError("Данные должны быть словарем.")
        
        if "name" not in data or not isinstance(data["name"], str):
            raise ValueError("Ключ 'name' отсутствует или имеет некорректное значение.")
        
        if "age" not in data or not (isinstance(data["age"], int) and data["age"] > 0):
            raise ValueError("Ключ 'age' отсутствует или возраст некорректен.")
        
        print("Данные корректны.")
    except Exception as e:
        raise ValueError("Ошибка проверки данных.") from e

# Тесты
validate_user_input({"name": "Alice", "age": 30})  # Ожидается успешная проверка
try:
    validate_user_input({"age": 30})  # Ошибка: Отсутствует 'name'
except ValueError as e:
    print(e)

try:
    validate_user_input({"name": "Alice", "age": "thirty"})  # Ошибка: Некорректное значение 'age'
except ValueError as e:
    print(e)

try:
    validate_user_input("not a dict")  # Ошибка: Некорректный тип данных
except TypeError as e:
    print(e)
