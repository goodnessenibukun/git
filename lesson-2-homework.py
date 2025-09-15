# lesson-2-homework.py

while True:
    # Ask user for input
    user_input = input("Enter a string: ")

    # If input is empty, end the program
    if user_input == "":
        print("Thanks for playing!")
        break

    # Otherwise, print different string versions
    print("First letter capitalized:", user_input.capitalize())
    print("All lowercase:           ", user_input.lower())
    print("Title case:              ", user_input.title())
    print("All uppercase:           ", user_input.upper())
