# Module 3 Activities
# David Sanchez
# Write a program which repeatedly reads integers until the user enters “done”. Once “done” is
# entered, print out the total, count, and average of the integers. If the user enters anything
# other than an integer, detect their mistake using try and except and print an error message and
# skip to the next integers.

# Write another program that prompts for a list of numbers as above and at the end prints out both the
# maximum and minimum of the numbers instead of the average.

# Initialize list to store numbers.
numbers = []

# Input Loop
while True:
    user_input = input("Enter a number or 'done' to finish: ")

    if  user_input == 'done':
        break

# Error Handling
    try:
        number = int(user_input)
        numbers.append(number)

    except ValueError:
        print("Invalid input. Please enter a numeric value or 'done' to end the program")

    if numbers:
        print("Maximum:", max(numbers))
        print("Minimum", min(numbers))
    else:
        print("No numbers were entered.")






