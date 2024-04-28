def caching_fibonacci():
    cache = {}  # Створюємо пустий словник для зберігання обчислених значень

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:  # Перевіряємо, чи вже є значення n у кеші
            return cache[n]
        else:
            # Обчислюємо число Фібоначчі за допомогою рекурсії
            result = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = result  # Зберігаємо обчислене значення у кеші
            return result

    return fibonacci

# Приклад використання з домашнього завдання:
fib = caching_fibonacci()
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
