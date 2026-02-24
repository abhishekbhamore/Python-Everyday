#name = input("What is your name? ")
#age = int(input("What is your age? "))

#future_age = age + 5

#print(f"Hello, {name} ! In 5 years you will be {future_age} years old and today your are {age} years old. Thank you for the using this program.")



# secret_number = 7
# attempts = 0

# while True:

#     try:
#         guess = int(input("guess a number::"))
        
#         attempts += 1
#         if guess < secret_number:
#             print("This is too low, try again.")
#         elif guess > secret_number:

#             print("This is too high, try again.")
#         else:
#             print("Congratulations! You guessed the number.")
#             print(f"you took {attempts} attempts to guess the number.")
#             break      

#     except ValueError:
#         print("This is not an valid number.")


# total = 0

# for i in range(1,6):
#     total = total + i

#     print(total)




numbers = [1, 2, 3, 4, 5]
total = 0
for i in numbers:

    total += i
    average = total / len(numbers)
print(total)
print(average)