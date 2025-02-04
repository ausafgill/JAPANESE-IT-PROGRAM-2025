
first_name = input("Enter your firstname: ")
last_name = input("Enter your lastname: ")


first_name = first_name.upper()
last_name = last_name.lower()


length = len(first_name) + len(last_name)



print(f"First name(Upper): {first_name}")
print(f"Last name(lower): {last_name}")
print(f"Sum of letters in your first and last name: {length}")