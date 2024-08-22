from random import randint


def print_list(items, header=None):
    if header != None:
        print(f"{header} {num}")
    for item in items:
        print(f"{item}")
    print()

num = int(input("Enter a number [1-10]: "))
num_list = []

for i in range(13):
    if num > 10 or num < 1:
        print("Error: Enter a number from 1 to 10!")
        break
    else:
        num1 = num*i
        num_list.append(num1)

print_list(num_list, "The Times Table Of")


new_list_even = num_list[0::2]

new_list_odd = num_list[1::2]

print_list(new_list_even, "Even Numbered Values: ")
print_list(new_list_odd, "Odd Numbered Values: ")