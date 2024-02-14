import random

count = 1
comp_num = random.randrange(100)

while True:
    my_num = int(input("Enter a number: "))
    
    if my_num < 1 or my_num>100:
        print("Please enter a number between 1 - 100! ")
        continue

    if comp_num > my_num:
        print("Enter a larger number.")
        count += 1
    elif comp_num < my_num:
        print("Enter a smaller number.")
        count += 1
    elif comp_num == my_num:
        print("You found it! Count:", count)
        break
    else:
        print("Something went wrong! Try again...")