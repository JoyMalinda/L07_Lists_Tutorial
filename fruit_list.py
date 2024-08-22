def fruit_list():
    fruits = []

    while True:
        fruit = input("Name another fruit: ")
        if fruit == "" or fruit in fruits:
            break

        fruits.append(fruit)
    print(fruits)

    print()
    print(f"Your score is {len(fruits)}")

fruit_list()