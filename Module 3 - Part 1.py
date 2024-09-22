# Module 3 Activities
# David Sanchez
# Write a program which repeatedly reads integers until the user enters “done”. Once “done” is
# entered, print out the total, count, and average of the integers. If the user enters anything
# other than an integer, detect their mistake using try and except and print an error message and
# skip to the next integers.

# Initialize total and count and set to 0
total = 0
count = 0

# Input loop
while True:
    user_input = input("Enter a number or 'done' to finish: ")

    if  user_input == 'done':
        break

# Error handling
    try:
        number = int(user_input)
        total += number
        count += 1

    except ValueError:
        print("Invalid input. Please enter a integer or 'done' to end the program")

# Average calculation and output
    if count > 0:
        average = total / count
        print(f"Total: {total}")
        print(f"Count: {count}")
        print(f"Average: {average}")
    else:
        print("No integers were entered.")