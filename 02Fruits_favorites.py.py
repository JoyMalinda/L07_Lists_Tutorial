def print_list(items, header=None):
    if header != None:
        print(header)
    for item in items:
        print(f"{item}")
    print()


fruits = ["Banana","Orange","Apple","Mango"]

least_fav = input("What is your least favorite fruit? ")
fruits.append(least_fav) # again!

favourite = input("What is your favourite fruit? ")
fruits.insert(0, favourite)

print_list(fruits, "FRUITS, favourite first")

print()
input("Press return to continue ...")
