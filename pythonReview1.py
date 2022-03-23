# Asks the user for their name and age
userName = input("Enter your first name: ")
userAge = input ("Enter your age: ")

# Converts the age input into a integer for mathmatical
# calculations then converts the results back to a string
convertAge = int(userAge)
ageMath = convertAge + 5
newAge = str(ageMath)

print(f"Hello {userName}. in five years you will be {newAge} years old!")

