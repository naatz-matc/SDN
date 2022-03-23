# This functon is desiged to take user input
# and return a variable to the main script

def checkName(userInput):
    result = True                  # defines a variable named 'result' and assigning it a boolean value of "True"
    splitInput = userInput.split() # takes the user input string and splits it into a list
    
    if len(splitInput) < 2:        # 'if' statement which says if the amount of elements in the 'splitInput' list is less
        result = False             # than 2, the 'result' variable changes to "False", prints the message to the screen and 
        print("!!ERROR!! Please enter BOTH your first and last name") # retruns the 'result' variable to the main script
        return result
    
    elif len(splitInput) > 2:      # 'elif' statement which says if the amount of elements in the 'splitInput' list is greater
        result = False             # than 2, the 'result' variable changes to "False", prints the message to the screen and
        print("!!ERROR!! Please enter your first and last name only") # returns the 'result' variable to the main script
        return result

    else:  # 'else' statement that is executed if the amount of elements in the 'spliInput' list is equal to 2 
        firstName = splitInput[0]  # assigns the value of the first element of 'splitInput' to this variable 
        lastName = splitInput[1]   # assigns the value of the second element of 'splitInput' to this variable
        global firstName1          # this makes the variable useable outside of the function
        firstName1 = firstName.capitalize() # capitalizes the first letter of 'firstName' and assigns the result to the variable
        global lastName1           # this makes the variable useable outside of the function
        lastName1 = lastName.capitalize()   # capitalizes the first letter of 'firstName' and assigns the result to the variable

        if firstName.isalpha() == False or lastName.isalpha() == False:                  # 'if' statement that says if the variables 'firstName'
            result = False                                                               # OR 'lastName' have any numeric or special characters 
            print("!!ERROR!! Please enter your first and last name with no numeric or\n" # in them to print the message to the screen, change  
                  "special characters")                                                  # the 'result' variable to "False" and returns it to
            return result                                                                # the main script
    
        elif firstName.isalpha() == True and lastName.isalpha() == True:    # 'elif' statement that says if the variables 'firstName' AND
            return result                                                   # 'lastName' do not have any numeric or special characters in them
                                                                            # to return the unchanged 'result' variable to the main script
# This is where the main script begins
                                                                            
isValidName = False # creates a variable named 'isValidName' and assigns it the boolean value "False"

while isValidName == False or None:                              # creates a 'while' loop that states while the previously created varialbe
    userInput = input("Please enter your first and last name: ") # has a value of "False" or "None" to ask for user input and to store that
    isValidName = checkName(userInput)                           # in a variable called 'userInput' and pass that variable into a function
                                                                 # called 'checkName()', which will become the new value of 'isValidName'
                                                                 
print(f"Welcome to Python, {firstName1}. {lastName1} is a really interesting surname!\n"
      f"Are you related to the famous Victoria {lastName1}?") # prints the message to the screen







