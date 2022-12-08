import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*_"

while True:
    password_length = int(input("Enter The Length of Required Password: "))

    password_count = int(input("Enter The Number of Required Password: "))

    for i in range(0, password_count):
        password = ""
        for j in range(0, password_length):
            password_characters = random.choice(characters)
            password = password + password_characters
        print("The Generated Password is ", password)

    repeat = input(
        "Do You Want to Generate More Passwords? Then Type 'YES' And 'NO'")
    if repeat == "no" or repeat == "NO":
        break

print("Thank You!")
