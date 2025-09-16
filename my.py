def calculator():
    while True:
        try:
            num1 = float(input("Введите первое число: "))
            operator = input("Выберите операцию (+, -, *, /): ")
            num2 = float(input("Введите второе число: "))
            
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Ошибка: деление на ноль!")
                    continue
            else:
                print("Неправильная операция")
                continue

            print(f"Результат: {result}")
        
        except ValueError:
            print("Некорректный ввод числа.")
        
        again = input("Хотите продолжить расчеты? (y/n): ").lower()
        if again != 'y':
            break

# Запускаем калькулятор
calculator()
