isValidName = False

while isValidName == False:
    validLength = False
    while validLength == False:
        userInput = input("Please enter your first and last name: ")
        splitInput = userInput.split()
        if len(splitInput) == 2:
            validLength = True
        elif len(splitInput) < 2:
            print("!!ERROR!! Please enter BOTH your first and last name")
        elif len(splitInput) > 2:
            print("!!ERROR!! Please enter your first and last name only")
    firstName = splitInput[0]
    lastName = splitInput[1]
    firstName1 = firstName.capitalize()
    lastName1 = lastName.capitalize()
    if firstName.isalpha() == False or lastName.isalpha() == False: 
        print("!!ERROR!! Please enter your first and last name with no numeric or\n"
              "special characters")
    elif firstName1.isalpha() == True and lastName.isalpha() == True:
        isValidName = True


print(f"Welcome to Python, {firstName1}. {lastName1} is a really interesting surname!\n"
      f"Are you related to the famous Victoria {lastName1}?")







