# This function is set up to take an input in its parentheses
# and defines the device ping function

def pingDevices(deviceDict):
    pingList = []                   # this creates an empty list called 'pingList'
    for device in deviceDict.keys():                         
        pingList.append("ping" + " " + deviceDict[device]["mgmtIP"])
    for element in pingList:        # the first 'for' loop is designed to take the value of each mgmtIP key and      
        print(element)              # add the string 'ping' to it and add them as a new element in the list pingList. 
                        # the second 'for' loop is designed to print out to the 
                        # screen the value of each element in the list 'pingList'.
        
# This function is set up to get a user input that is user defined and 
# has a user generated list of acceptable answers to compare the input to
                
def getInput(prompt,validationList):
        answer = input(prompt)
        while answer not in validationList:
                print("Invalid entry. The following are valid inputs" + str(validationList))
                answer = input(prompt)  # this 'while' loop is set up so that for as long as the user input does not match
                                        # any value in the validation list a error message is displayed and re-propts
        return answer                   # the user until a valid response is provided which will return the valid response
    
# This function is set up to take an input in its parentheses
# and prints out a specified formatted list of the dictionary
    
def printDevices(devices):
    for device in devices.keys(): 
        print(devices[device]["hostname"] + "\t" + devices[device]["type"] + "\t" + devices[device]["mgmtIP"])
                                # this 'for' loop will go through each 'key' in the specified dictionary
                                # and print to the screen the specified values in each nested dictionary

# This function is set up to create a new dictionary with the specified 'key:value'
# pairs in the function and return the dictionary to the main script
        
def getDeviceInfo():
    returnDict = {"type" : "",
                  "hostname" : "",  # creates a dictionary called "returnDict"
                  "mgmtIP" : ""
                  } 
    returnDict["hostname"] = input("Enter device hostname: ")   # asks the user to input the value for the 'hostname' key
    returnDict["mgmtIP"] = input("Enter management IP address: ") # asks the user to input the value for the 'mgmtIP' key

    return returnDict # this returns the created dictionary to the main script

# This function is set up to take an input in its parentheses
# and checks whether the input is a valid IP address

def validateIP(ipString):
        validIP = True  # creates a variable named 'validIP' and sets its value to the boolean value "True"
        ipList = ipString.split(".")# splits the inputted string into a list called 'ipList'  
                                    # where each list element is seperated by the period character
                                                                                    
        if len(ipList) !=4: # checks the length of 'ipList'. If the length doesn't  
            validIP = False # equal 4 it sets the value of 'validIP' to "False"  
        else:
            ipNumCheck = ipString.replace(".","") # creates a variable named 'ipNumCheck', which replaces the period
                                                  # in the string 'ipString' with nothing for every occurance
                                                  
            if ipNumCheck.isnumeric() == False: # checks the variable 'ipNumCheck' to see if only numeric characters are in the string
                validIP = False                 # if there are any alpha or special characters, the value of 'validIP' is set to "False"   
            else:
                ipInteger = ([int(x) for x in ipList]) # creates a new list called 'ipInteger', which is populated by 
                                                       # changing the data type in 'ipList' from strings to integers
                                                       
                ipRange = range(256) # creates a range variable with a range between 0-255
                if ipInteger[0] not in ipRange:
                    validIP = False             # the first three 'if' statements check to see if the first three
                if ipInteger[1] not in ipRange: # elements of the list 'ipInteger' are in the appropriate range,
                    validIP = False             # which is represented by the variable 'ipRange'. If any of them 
                if ipInteger[2] not in ipRange: # are not the value of 'validIP' is set to "False"
                    validIP = False
                if ipInteger[3] not in ipRange or ipInteger[3] ==0: # this final 'if' statement behaves the same way as the previous three
                    validIP = False                                 # with the addition of checking if the last element is equal to zero
                    
        return validIP # returns the variable and its value to the main script

# This function is set up to take an input in its parenteses
# and checks whether the input is a valid device hostname

def validateHost(hostname):
        validHost = True  # creates a variable named 'validHost' and sets its value to the boolean value "True"
        if len(hostname) == 0 or len(hostname) >64: # checks the length of 'hostname'. If the length is equal to zero 
            validHost = False                       # or greater than 64 characters, it sets 'validHost' value to "False"
        else:
            if hostname[0].isalpha() == False: # checks if the first character in 'hostname' is an alpha character. If the
                validHost = False              # first character is not an alpha character, it sets 'validHost' value to "False"
                
            if len(hostname.split()) >1: # checks if 'hostname' string has any spaces between any of its characters
                validHost = False        # If there are any spaces, it sets 'validHost' value to "False"

        return validHost # returns the variable and its value to the main script

# This function is set up to take two user inputs. The first entry is the new dictionary  
# while the second entry is the existing dictionary. It is designed to add a new dictionary 
# to an existing dictionary as a nested dictionary

def updateDictionary(newEntry, existingDict):
    hostname = newEntry["hostname"] # creates the variable 'hostname', defined as the 'value' from the new dictionary 'key' named "hostname"
    
    existingDict[hostname] = newEntry # adds the 'hostname' variable as a new 'key' to the existing dictionary while  
                                      # adding the entire new dictionary as its 'value' pair in the existing dictionary
# existing dictionary
devices = {
    "R1" : {
        "type" : "router",
        "hostname" : "R1",
        "mgmtIP" : "10.0.0.1"
    },

    "R2" : {
        "type" : "router",
        "hostname" : "R2",
        "mgmtIP" : "10.0.0.2"
    },

    "S1" : {
        "type" : "switch",
        "hostname" : "S1",
        "mgmtIP" : "10.0.0.3"
    },

    "S2" : {
        "type" : "switch",
        "hostname" : "S2",
        "mgmtIP" : "10.0.0.4"
    }
}

# This section begins the main code block of this script

printDevices(devices) # prints current devices from the devices dictionary
print("\n")                                                                          # uses the getInput() function with user specified
addDevice = getInput("Do you want to add a device? (y or n) ", ["y", "n", "Y", "N"]) # inputs to create a new variable called 'addDevice' 
                                                                                     
                                                                                     
if addDevice.lower() == "y": # if the value of 'addDevice' is "y", the indented code block below is executed
    
        validDevice = False # creates a variable called 'validDevice' and sets its value to the boolean value "False"
        
        while validDevice == False: # creates a 'while' loop were the below indented code block 
                                    # executes while the value of 'validDevice' is "False
                                    
            deviceType = getInput("Is this a switch or router? (enter s or r) ", ["s","S","r","R"])  
                         # uses the getInput() function with user specified inputs to create a new variable called 'deviceType'
                         
            deviceDict = getDeviceInfo() # uses the getDeviceInfo() function to create a new dictionary variable called 'deviceDict'                                                          
            
            if deviceType.lower() == "s":     # if the value of 'deviceType' is "s", then the value "switch" is added
                deviceDict["type"] = "switch" # as the 'value' to the 'deviceDict' dictionary 'key' of "type"
            else:
                deviceDict["type"] = "router" # if the value of 'deviceType' is not "s", then the value "router" is
                                              # added as the 'value' to the 'deviceDict' dictionary 'key' of "type"

            validHost = validateHost(deviceDict["hostname"])
                                                # uses the validateHost() function using the 'value' paired with the 'key' "hostname"
                                                # from the deviceDict dictionary to create a new variable called 'validHost'

            if validHost == False:
                print("Invalid hostname. Hostname must start with a letter, not be seperated by spaces and less than 64 characters")
                                    # if the value of 'validHost' is "False", then the print message is displayed to the screen
                                    # if the value of 'validHost' is "True", then the following indented code block below is executed
            else:
                validIP = validateIP(deviceDict["mgmtIP"]) # uses the validateIP() function using the 'value' paired with the 'key' "mgmtIP"
                                                           # from the deviceDict dictionary to create a new variable called 'validIP'

                if validIP == False:
                    print("Invalid IP address. IP address must be in the following format: x.x.x.y where x>= 0 and x <= 255 and y cannot be 0")
                                    # if the value of 'validIP' is "False", then the print message is displayed to the screen
                                    
                if validIP == True and validHost == True: # if the values of both 'validIP' and 'validHost' are "True, the value of 
                    validDevice = True                    # 'validDevice' is set to "True". This will allow for the exit of the 'while'
                                                          # loop and the execution of code block below

        updateDictionary(deviceDict, devices) # uses the updateDictionary() function using the new variable 'deviceDict' and 
                                              # existing variable 'devices' to add 'deviceDict' to the 'devices' dictionary
        print("\n")
        print("Update successful!") # print messages are displayed to the screen
        
        pingDevices(devices) # uses the pingDevices() function using the 'devices' dictionary as a user input to create a
                             # list of IP addresses to ping. This will print the list out to the screen
            
else:                                       # if the value of 'addDevice' is "n", the print message
    print("Program ended. Nothing changed") # is displayed to the screen and the script ends 
                                            
