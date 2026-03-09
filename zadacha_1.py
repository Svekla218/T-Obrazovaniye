def main():
    try:
        user_input = input().split()
        if len(user_input) < 2:
            return

        start = int(user_input[0])
        end = int(user_input[1])

        if start > end:
            return

        a, b = 0, 1
        found_numbers = []

        while a <= end:
            if a >= start:
                found_numbers.append(a)
            a, b = b, a + b

        if found_numbers:
            print(*(found_numbers))
        else:
            print("В заданном диапазоне нет чисел Фибоначчи")

    except ValueError:
        pass

if __name__ == "__main__":
    main()
