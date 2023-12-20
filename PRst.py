import random


def finds_elements(a: list, b: list) -> list:

    """
        Функция finds_elements() находит элементы в массиве A,
        которые присутствуют в массиве В в нескольких экземплярах.

        Args:
            a(list): массив A с набором чисел
            b(list): массив B с набором чисел

        Returns:
            Вывод массива созданного внутри функции с удовлетворяющими
            заданию элементами.

        Examples:
            >>>finds_elements([1, 2, 3, 4, 5], [3, 2, 2, 2, 3])
            [2, 3]
    """

    plenty = []

    for element in a:
        if a.count(element) == 1 and b.count(element) > 1:
            plenty.append(element)

    return plenty


def not_finds_elements(a: list, b: list) -> list:

    """
        Функция для нахождения элементов которые, находятся в массиве A,
        но не находятся в массиве B.

        Args:
            a(list): массив A с набором чисел
            b(list): массив B с набором чисел

        Returns:
            Вывод массива созданного внутри функции с удовлетворяющими
            заданию элементами.

        Examples:
            >>>not_finds_elements([1, 7, 10, 11, 5], [3, 2, 2, 2, 3])
            [1, 7, 10, 11, 5]
    """

    plenty = []

    for element in a:
        if a.count(element) != b.count(element) and b.count(element) == 0:
            plenty.append(element)

    return plenty


def all_finds_elements(a: list, b: list) -> list:

    """
        Функция для нахождения элементов, которые находятся в массиве A
        и в массиве B в единственном экземпляре.

        Args:
            a(list): массив A с набором чисел
            b(list): массив B с набором чисел

        Returns:
            Вывод массива созданного внутри функции с удовлетворяющими
            заданию элементами.

        Examples:
            >>>not_finds_elements([259, 7, 10, 11, 666], [259, 2, 2, 2, 666])
            [259, 666]
    """

    plenty = []

    for element in a:
        if a.count(element) == 1 and b.count(element) == 1:
            plenty.append(element)

    return plenty


array_A = [random.randint(0, 30) for number_A in range(50)]
array_B = [random.randint(0, 30) for number_B in range(50)]
print("Program for working with arrays")
print("------------------------------------")
print(f"array_A: {array_A}")
print(f"array_B: {array_B}")

while True:

    print("------------------------------------")

    print("__Menu__")
    print("1) task 1")
    print("2) task 2")
    print("3) task 3")
    print("4) exit")

    menu = input("Enter the item: ")

    print("------------------------------------")

    if menu == '1':
        found = finds_elements(array_A, array_B)

        if found:
            print(f"Elements found: {found}")
        else:
            print("Elements not found")

        print("exit/symbol")
        exitr = input("Enter: ")
        if exitr == "exit":
            break

    elif menu == '2':
        found = not_finds_elements(array_A, array_B)

        if found:
            print(f"Elements found: {found}")
        else:
            print("Elements not found")

        print("exit/symbol")
        exitr = input("Enter: ")
        if exitr == "exit":
            break

    elif menu == '3':
        found = all_finds_elements(array_A, array_B)

        if found:
            print(f"Elements found: {found}")
        else:
            print("Elements not found")

        print("exit/symbol")
        exitr = input("Enter: ")
        if exitr == "exit":
            break

    elif menu == '4':
        break

    else:
        print("Incorrect input")
