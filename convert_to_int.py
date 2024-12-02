def convert_to_int(value):
    try:
        result = int(value)
        print(f"Преобразование успешно: {result}")
        return result
    except ValueError:
        print("Ошибка: Невозможно преобразовать строку в целое число.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
    finally:
        print("Попытка преобразования завершена.")
        
# Тесты
convert_to_int("123")  # Ожидается успешное преобразование
convert_to_int("abc")  # Ожидается ValueError
convert_to_int([1, 2, 3])  # Ожидается Exception
