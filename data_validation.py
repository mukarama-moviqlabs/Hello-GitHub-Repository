name = input("Enter your name: ")
age = input("Enter your age: ")

name = name.strip()

if name == "":
    print("Name cannot be empty")

elif not age.isdigit():
    print("Age must contain numbers only")

else:
    age = int(age)

    if age <= 0 or age > 120:
        print("Please enter a valid age")

    else:
        print("Registration successful!")
        print("Name:", name)
        print("Age:", age)