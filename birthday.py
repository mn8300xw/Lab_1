import datetime

# Converts month name to a number
months = {
    "january": 1, "february": 2, "march": 3, "april": 4,
    "may": 5, "june": 6, "july": 7, "august": 8,
    "september": 9, "october": 10, "november": 11, "december": 12
}

# Gets the current computer date
current_month = datetime.datetime.now().month

# Ask the user for their name
name = input("What is your name? ")

# Ask the user for the month they were born in
birth_month = input("What month were you born in? ").lower()
input_month = months.get(birth_month)

# Count the number of characters in the name input
letter_count = 0
for char in name:
    if char.isalpha():
        letter_count += 1

# Display the information
print("Hello,", name + "!")
print("Number of letters:", letter_count)

if input_month is None:
    print("Invalid month name.")
elif input_month == current_month:
    print("Happy birthday month!")
else:
    print("Your birthday is passed or is yet to come.")



