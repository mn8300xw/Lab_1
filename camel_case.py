# Ask the user for a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Convert to camelCase
camel_case = words[0].lower()

for word in words[1:]:
    camel_case += word.capitalize()

# Print the camelCase result
print("camelCase:", camel_case)

# Optional: basic variable name validation
if camel_case[0].isdigit():
    print("Warning: Variable names should not start with a number.")

for char in camel_case:
    if not (char.isalpha() or char.isdigit() or char == "_"):
        print("Warning: Variable name contains invalid characters.")
        break