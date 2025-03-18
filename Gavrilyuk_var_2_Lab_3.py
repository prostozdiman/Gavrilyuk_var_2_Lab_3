from itertools import combinations

def fibonacci(n):
    """Рівень 1: Рекурсивний пошук n-го числа Фібоначчі."""
    if n <= 0:
        return "Помилка: n має бути більше 0"
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def word_count(text):
    """Рівень 2: Підрахунок слів у рядку без split()."""
    count = 0
    in_word = False
    for char in text:
        if char.isalpha():
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False
    return count

def generate_subsets(chars):
    """Рівень 3: Генерація всіх підмножин множини символів без перестановок."""
    result = []
    for i in range(len(chars) + 1):
        for subset in combinations(chars, i):
            result.append("".join(subset))
    return result

def main():
    while True:
        print("\nОберіть завдання:")
        print("1 - Рівень 1: Число Фібоначчі")
        print("2 - Рівень 2: Підрахунок слів")
        print("3 - Рівень 3: Генерація підмножин")
        print("0 - Вийти")
        choice = input("Ваш вибір: ")
        
        if choice == "1":
            n = int(input("Введіть номер числа Фібоначчі: "))
            print(f"{n}-е число Фібоначчі: {fibonacci(n)}")
        elif choice == "2":
            text = input("Введіть рядок: ")
            print("Кількість слів у рядку:", word_count(text))
        elif choice == "3":
            chars = input("Введіть символи (без пробілів): ")
            subsets = generate_subsets(chars)
            print("Усі підмножини:", subsets)
        elif choice == "0":
            print("Вихід...")
            break
        else:
            print("Некоректний вибір, спробуйте ще раз!")

if __name__ == "__main__":
    main()