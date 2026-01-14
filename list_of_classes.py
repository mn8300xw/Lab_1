# Create an empty list to store class names
classes = []

print("Enter your class names. Type 'done' when finished.")

while True:
    class_name = input("Enter a class name: ")

    if class_name.lower() == "done":
        break

    classes.append(class_name)

# Print each class name on a new line
print("\nYour classes this semester:")
for class_name in classes:
    print(class_name)