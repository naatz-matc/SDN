import requests                    # imported module to request information from websites and APIs
import json                        # imported module to allow handling of raw json data

def sendCLI(mgmtIP,commandName):   # this function returns the output of the sepcified command from a device

    """
    Be sure to run feature nxapi first on Nexus Switch

    """
    switchuser='cisco'              # username needed to access the device
    switchpassword='cisco'          # password needed to access the device

    url='https://' + mgmtIP + '/ins'                      # the management IP address for the device being accessed
    myheaders={'content-type':'application/json-rpc'}
    payload=[
      {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
          "cmd": commandName,       # the string variable that is passed through the function is inserted here
          "version": 1
        },
        "id": 1
      }
    ]

    '''
    verify=False below is to accept untrusted certificate
    '''

                                    # defining the response we get back from the nxapi
    
    interfaceDict = requests.post(url,data=json.dumps(payload), verify=False, headers=myheaders,auth=(switchuser,switchpassword)).json()
    
                                                                               #creating a variable that parses through the json response
    listInterfaces = interfaceDict["result"]["body"]["TABLE_intf"]["ROW_intf"] #and creates a list that contains dictionaries of each 
                                                                               #interface and its information
    return listInterfaces       # returns the variable to the main script

def getDevice(dictionary):                      # this function propmts the user for input and checks their input for validity
    validDevice = False                         # control variable for the 'while' loop is defined as the boolean "False"
    while validDevice == False:                 # a 'while' loop begins and prompts the user for a device

        answer = input("Enter the hostname of the device you want to access: ") # user input is stored in the variable 'answer', which    
        deviceName = answer.lower()                                             # is formatted and stored in the variable 'deviceName'                                  

        validDevice = validateDevice(dictionary, deviceName)                # calls the function "validateDevice()" and passes through the
        if validDevice == False:                                            # local variables 'deviceName' and 'dictionary'
            print("***ERROR*** Device not found. Try again")
                                                                            # after called function runs if 'validDevice' value is "False",
                                                                            # an error message is displayed and stays in the 'while' loop
                                                                            
    deviceIP = dictionary[deviceName]           # creates a variable called 'deviceIP' which is the management IP address
                                                # of the verified 'deviceName' variable found in the passed through 'dictionary' variable
                                            
    return deviceIP                             # returns the value of 'deviceIP' to the main script once out of the 'while' loop

"""    
 validateDevice(deviceName, dictionary) function is used in tandem with the getDevice() function to verify if a user entered
 device is in a dictionary of existing devices. validateDevice(deviceName, dictionary) does not appear in the main script, only
 in the getDevice() function when it is called
"""

def validateDevice(dictionary, deviceName): # this function takes in a dictionary and a string and checks if the string is in the dictionary
    validDevice = False                     # control variable of 'validInt' set to boolean value of "False"
    for key in dictionary:
        if key == deviceName:               # a 'for' loop that iterates through each dictionary key and checks if the
            validDevice = True              # 'deviceName' string is a valid ["key] in the dictionary. If it is, the
                                            # value of 'validDevice' changes to the boolean value "True"
                                            
    return validDevice                      # returns the value of 'validDevice' to the main script or the function that called it

def printDevices(dictionary):
    print("Device" + "\t\t" + "mgmtIP")
    print("-"*10 + "\t" + "-"*15)
    for key in dictionary:
        print(key + "\t" + dictionary[key])

def printList(varName):                                                 # this function prints out the variable 
    print("Name" + "\t" + "Proto" + "\t" + "Link" + "\t" + "Address")   # passed through it in a specified way
    print("-"*4 + "\t" + "-"*5 + "\t" + "-"*4 + "\t" + "-"*7)
    for dictionary in varName:
        print(dictionary["intf-name"] + "\t" + dictionary["proto-state"] + "\t" + dictionary["link-state"] + "\t" + dictionary["prefix"])
                            # a 'for' loop that for each dictionary in the list "varName" it should print out the
                            # specific ["value"] for each specified dictionary["key"]

def getInput(prompt, validationList):       # this function is set up to get user input that is user defined and
    answer = input(prompt)                  # has a user generated list of acceptable answers to compare the input to
    while answer not in validationList:
        print("Invalid entry. The following are valid inputs: " + str(validationList))
        answer = input(prompt)              # a 'while' loop checks the user input from the prompt against a list of valid inputs
                                            # if answer is in the valid list, the value of 'answer' is returned to the main script
    return answer

def getInterface():                         # this function propmts the user for input and checks their input for validity
    validInterface = False
    while validInterface == False:          # a 'while' loop begins and prompts the user for an interface
        
        answer = input("Enter the name of the interface you want to change: ") # user input is stored in the variable 'answer', which 
        intName = answer.capitalize()                                          # is formatted and stored in the variable 'intName'
        
        validInterface = validateInterface(interfaceList,intName)       # calls the function "validateInterface()" and passes through   
        if validInterface == False:                                     # the global variable 'interfaceList' and local variable 'intName'
            print("***ERROR***  Interface not found. Try again")
                                                                        # after called function runs if 'validInterface' value is "False",
                                                                        # an error message is displayed and stays in the 'while' loop
                                                                        
    return intName          # returns the value of 'intName' to the main script once out of the 'while' loop

"""    
 validateInterface(intList, intName) function is used in tandem with the getInterface() function to verify if a user entered
 interface is in a list of existing interfaces. validateInterface(intList, intName) does not appear in the main script, only
 in the getInterface() function when it is called
"""

def validateInterface(intList, intName):    # this function takes in a list and a string and checks if the string is in the list
    validInt = False                        # control variable of 'validInt' set to boolean value of "False"
    for element in intList:
        if element["intf-name"] == intName: # a 'for' loop that iterates through each list element and checks if the 'intName'
            validInt = True                 # string is a ["value"] for any ["intf-name"] dictionary ["key"]. If it is, the
                                            # value of 'validInt' changes to the boolean value "True"

    return validInt                         # returns the value of 'validInt' to the main script or the function that called it


def validateIPAddress(validationString):
    badIP = True                            # creates a variable named 'badIP' and sets its value to the boolean value "True"
    while badIP == True:                    # creates a 'while' loop that is used to check if the user input is valid
        badIP = False
        ipString = input("Enter an IP address for the interace: ")
        ipList = ipString.split(".")        # asks the user to input an IP address, once entered it creates a list from the user
                                            # input, splitting up the string into list elements by the "." in the IP address
        if len(ipList) !=4:
            print(validationString)         # checks if the length of 'ipList' is not equal to 4, if not we print out the
            badIP = True                    # 'validationString' message, change 'badIP' back to "True" and remain in the 'while' loop

        else:
            ipNumCheck = ipString.replace(".","",4) # creates a new variable by replacing all the "." in 'ipString' with nothing
            
            if ipNumCheck.isnumeric() == False:     # checks if all the characters in 'ipNumCheck' are numerical, if not we print 
                print(validationString)             # out the 'validationString' message, change 'badIP' back to "True" and remain
                badIP = True                        # in the 'while' loop

            else:
                ipInteger = ([int(x) for x in ipList]) # creates a new variable that changes the date type in 'ipList' to integers
                ipRange1 = range(256)                  # customized integer range variable
                ipRange2 = range(255)                  # customized integer range variable
    
                if ipInteger[0] not in ipRange1:    # checks if the first list element is in one of the specified range variables
                    print(validationString)         # if not we print out the 'validationString' message, change 'badIP' back to 
                    badIP = True                    # "True" and remain in the 'while' loop
                
                elif ipInteger[1] not in ipRange1:  # checks if the second list element is in one of the specified range variables
                    print(validationString)         # if not we print out the 'validationString' message, change 'badIP' back to
                    badIP = True                    # "True" and remain in the 'while' loop

                elif ipInteger[2] not in ipRange1:  # checks if the third list element is in one of the specified range variables
                    print(validationString)         # if not we print out the 'validationString' message, change 'badIP' back to
                    badIP = True                    # "True" and remain in the 'while' loop 

                elif ipInteger[3] not in ipRange2 or ipInteger[3] ==0:
                    print(validationString)         # checks if the fourth list element is in one of the specified range variables
                    badIP = True                    # or if its value is equal to 0, if not in the specified ipRange variable or its
                                                    # equal to 0 we print out the 'validationString' message, change 'badIP' back to
                                                    # "True" and remain in the 'while' loop
                else:
                    return ipString                 # returns the variable "ipString" back to the main script


def validateCIDR(validationString):                 
    badCIDR = True                                  # creates a control variable called 'badCIDR' and sets its value to the boolean "True"
    while badCIDR == True:                          # creates a 'while' loop that is used to check if the user input is valid
        badCIDR = False                             # changes the control variable to "False" once inside the 'while' loop
        
        CIDR = input("Please enter a subnet in CIDR notation: ") # asks a user for input and stores it in a variable called 'CIDR'
        
        if len(CIDR) >3 or len(CIDR) <2:            # checks to see if the length of 'CIDR' is greater than 3 or less than than 2,
            print(validationString)                 # if not we print the 'validationString' message and change the control variable
            badCIDR = True                          # back to "True" and remain in the 'while' loop

        else:
            if CIDR[0] != "/":                      # checks to see if the first character in 'CIDR' is a "/", if not we print
                print(validationString)             # the 'validationString' message to the screen and change the control variable
                badCIDR = True                      # back to "True" and remain in the 'while' loop

            else:
                CIDRString = CIDR.strip("/")            # creates a new variable called 'CIDRString' by removing the "/" from the
                if CIDRString.isnumeric() == False:     # 'CIDR' string. Then checks to see if the remaining characters in 'CIDRString'
                    print(validationString)             # are numerical. If not we print the 'validationString' message and change the
                    badCIDR = True                      # control variable back to "True" and remain in the 'while' loop

                else:
                    CIDRInt = int(CIDRString)           # creates a new variable called 'CIDRInt' by changing the data type of
                    if CIDRInt <=1 or CIDRInt >=30:    # 'CIDRString' from a string to an integer. Then checks to see if the value
                        print(validationString)         # of 'CIDRInt' is greater than or equal to 1 and less than or equal to 30
                        badCIDR = True                  # if not we print the 'validationString' message and change the control
                                                        # variable back to "True" and remain in the 'while' loop

                    else:
                        return CIDR                     # returns the value of 'CIDR' to the main script and exits the 'while' loop
                    

def changeIntAndIPAddress(mgmtIP, intName, IPAddress, CIDR): # this function changes an interfaces IP address and subnet
                                                             # mask on a specified device using the passed through variables   
    """
    Modify these please
    """
    switchuser='cisco'                                  # username needed to access the device
    switchpassword='cisco'                              # password needed to access the device

    url='https://' + mgmtIP + '/ins'                    # the management IP address for the device being 
                                                        # accessed using the passed through variable 'mgmtIP'
    myheaders={'content-type':'application/json-rpc'}
    payload=[
      {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
          "cmd": "configure terminal",
          "version": 1
        },
        "id": 1
      },
      {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
          "cmd": "interface " + intName,                # the specified interface to be change using
          "version": 1                                  # the passed through variable 'intName'
        },
        "id": 2
      },
      {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
          "cmd": "ip address " + IPAddress + CIDR,      # the specified new IP address and subnet mask by using
          "version": 1                                  # the passed through variables of 'IPAddress' and 'CIDR'
        },
        "id": 3
      }
    ]

                                    #defining the response we get back from the nxapi
    
    response = requests.post(url,data=json.dumps(payload), verify=False, headers=myheaders,auth=(switchuser,switchpassword)).json()

#########################
# Start of Main Script
#########################

devicesDict = {                         # pre-defined dictionary of valid devices and their management IP Addresses
    "dist-sw01" : "10.10.20.177",
    "dist-sw02" : "10.10.20.178"}

updateInterfaces = True                 # creates a control variable called 'updateInterfaces' and sets it to the boolean "True"

while updateInterfaces == True:         # creates a 'while' loop that ask the user if they want to change the
                                        # IP address information on any of the specified devices interfaces
    
    answer = getInput("Would you like to change/update interface address information?: ", ["Y", "y", "N", "n"])
    
    if answer.capitalize() == "N":      # prompts the user if they want to change any interface address information by using the
        print("---END PROGRAM---")      # getInput() function. Once the user returns a valid response that is specified in the 
        updateInterfaces = False        # function the response is stored in the variable 'answer'. We then reach an 'if' statement
                                        # that standardizes the user input with the .capitalize() method and says that if
                                        # answer.capitalize() is equal to "N" we print out the end of program message, change the
                                        # control variable 'updateInterfaces' to "False", exits the 'while' loop and ends the program

    else:                               # this code block runs if 'answer.capitalize()' from above is equal to "Y"

        printDevices(devicesDict)                  # prints out the devices in 'devicesDict' in a specified format

        deviceMgmtIP = getDevice(devicesDict)      # runs the getDevice() function with the dictionary 'devicesDict'
                                                   # and stores the result in the variable 'deviceMgmtIP'

        interfaceList = sendCLI(deviceMgmtIP, "show ip interface brief")  # sends an API request to a device using the sendCLI() function
                                                                            # using the passed through strings and stores the result in a
                                                                            # variable called 'interfaceList'

        printList(interfaceList)            # uses the printList() function with the variable 'interfaceList' to
                                            # print out the information in 'interfaceList' in a specified format       

        changedInterface = getInterface()   # runs the getInterface() function and stores the result in the variable 'changedInterface'
       
        changedIPAddress = validateIPAddress("***ERROR*** IP address must be in the following format: x.x.x.y where x>= 0 and x <= 255, "
                                             "y >=1 and y<=254")    # runs the validateIPAddress() function with the specified error
                                                                    # message and stores the result in the variable 'changedIPAddress'

        changedCIDR = validateCIDR("***ERROR*** CIDR mask must begin with a '/' and be >= 1 and <=30")
                                                                    # runs the validateCIDR() function with the specified error
                                                                    # message and stores the result in the variable 'changedCIDR'
       
        changeIntAndIPAddress(deviceMgmtIP, changedInterface, changedIPAddress, changedCIDR)
                                                                    # sends an API request to a device using the changeIntAndIPAddress()
                                                                    # function to change IP address info on a specified interface on a
                                                                    # specified device using the passed through variables

        interfaceList = sendCLI(deviceMgmtIP, "show ip interface brief")
                                                                    # sends an API request to a device using the sendCLI() function
                                                                    # using the passed through string and variable and stores
                                                                    # the UPDATED result in a variable called 'interfaceList'

        printList(interfaceList)
                                        # uses the printList() function with the variable 'interfaceList' to
                                        # print out the information in 'interfaceList' in a specified format
        





