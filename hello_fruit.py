import random

def hello_fruit():
    name = input("What is your name? ")
    fruits = ["Banana","Orange","Apple","Mango"]

    fav = fruits[random.randint(0, 3)]

    print(f"Hello {name}, your favorite fruit is {fav}")

hello_fruit()