import requests                                             # imported module to request information from websites and APIs
import json                                                 # imported module to allow handling of raw json data

def getInterfaces(deviceIP):
    
    url = "https://" + deviceIP + ":443/restconf/data/ietf-interfaces:interfaces"

                                                            # This function is desined to send a YANG RESTCONF API
    username = 'cisco'                                      # request to an IOS XE device. The variable "deviceIP"
    password = 'cisco'                                      # is passed through to be used in the URL. The specific
    payload={}                                              # URL here grabs the interface information for the device
    headers = {                                             # and the username and password variables allow access
      'Content-Type': 'application/yang-data+json',
      'Accept': 'application/yang-data+json',
      'Authorization': 'Basic cm9vdDpEX1ZheSFfMTAm'
    }

    response = requests.request("GET", url, auth = (username,password), verify = False, headers=headers, data=payload)

    interfaceDict = response.json()                   # Here the response from the device is converted into JSON, 
                                                      # assigned to a variable called "interfaceDict"
                                                      
    newList = []                                      # Creates a new empty list variable called "newList"
    
# This 'for' loop is set up so that for each dictionary in each list element if the dictionary value that is paired with the dictionary
# key "name" DOES NOT begin with 'L', then append a new dictionary to the variable "newList" with the hardcoded in dictionary keys and
# the specified dictionary values.

    for element in interfaceDict["ietf-interfaces:interfaces"]["interface"]:
        if not element["name"].startswith("L"):
            newList.append({"interface" : element["name"], "IP address" : element["ietf-ip:ipv4"]["address"][0]["ip"]})

    return newList                                    # returns the variable "newList" to the main script

def getIntState(deviceIP):

    url = "https://" + deviceIP + ":443/restconf/data/interfaces-state"

                                                            # This function is desined to send a YANG RESTCONF API
    username = 'cisco'                                      # request to an IOS XE device. The variable "deviceIP"
    password = 'cisco'                                      # is passed through to be used in the URL. The specific
    payload={}                                              # URL here grabs the interface state information for the device
    headers = {                                             # and the username and password variables allow access
      'Content-Type': 'application/yang-data+json',
      'Accept': 'application/yang-data+json',
      'Authorization': 'Basic cm9vdDpEX1ZheSFfMTAm'
    }

    response = requests.request("GET", url, auth = (username,password), verify = False, headers=headers, data=payload)

    intStateDictionary = response.json()               # Here the response from the device is converted into JSON,
                                                       # assigned to a variable called "intStateDictionary"
                                                       
    newList = []                                       # Creates a new empty list variable called "newList"
    
# This 'for' loop is set up so that for each dictionary in each list element if the dictionary value that is paired with the dictionary
# key "name" DOES NOT begin with 'L', then append a new dictionary to the variable "newList" with the hardcoded in dictionary keys and
# the specified dictionary values.
    
    for element in intStateDictionary["ietf-interfaces:interfaces-state"]["interface"]:
        if not element["name"].startswith("L"):
            newList.append({"interface" : element["name"], "MAC address" : element["phys-address"]})

    return newList                                      # returns the variable "newList" to the main script

def combinedIntList(intList, intStateList):
                                                        # This function is designed to take in two list variables. It starts off by 
    newList = []                                        # creating an empty list variable called "newList". Then it transitions into
                                                        # a 'for' loop that for each dictionary in intList we create two new variables
    for element in intList:                             # called "intName" & "intIP" that get their values from the specified
        intName = element["interface"]                  # dictionary values. Then we transition into another 'for' loop that is running
        intIP = element["IP address"]                   # inside the first 'for' loop. The second 'for' loop states that for each
                                                        # dictionary in intStateList we create two new variables called "interName" &
        for element in intStateList:                    # "intMAC" that get their values from the specified dictionary values.
            interName = element["interface"]            # Finally we reach an 'if' statement where if the value of intName equals
            intMAC = element["MAC address"]             # interName we append a dictionary to the variable "newList" with the hardcoded
                                                        # dictionary key and specified dictionary value. 
            if intName == interName:                    
                newList.append({"interface" : intName, "IP address" : intIP, "MAC address" : intMAC})

    return newList                                      # returns the variable "newList" to the main script
    
def printIntInfo(interfaceList):
                                                                         
    print()                                                              
    print("Interface" + "\t\t" + "IP Address" + "\t" + "MAC Address") 
    print("-"*16 + "\t" + "-"*13 + "\t" + "-"*17)                       
    for element in interfaceList:
        print(element["interface"] + "\t" + element["IP address"] + "\t" + element["MAC address"])

                                                                    # This function takes in the variable "interfaceList" and uses it to
                                                                    # print out the specified information in a specifically formatted way


def validateIPAddress(ipString):        # This function verifies if the passed through variable is a valid IP address
    
    validIP = False
    
    ipList = ipString.split(".")        # Takes the passed through variable 'ipString' and splits up the
                                        # string into list elements seperated by the "." in the IP address
    if len(ipList) !=4:
        return validIP                  # checks if the length of 'ipList' is not equal to 4, if not we return
                                        # the value of 'validIP' to the main script.

    else:
        ipNumCheck = ipString.replace(".","",4) # creates a new variable by replacing all the "." in 'ipString' with nothing
        
        if ipNumCheck.isnumeric() == False:     # checks if all the characters in 'ipNumCheck' are numerical, if not we 
            return validIP                      # return the value of 'validIP' to the main script.                        

        else:
            ipInteger = ([int(x) for x in ipList]) # creates a new variable that changes the date type in 'ipList' to integers
            ipRange1 = range(256)                  # customized integer range variable
            ipRange2 = range(255)                  # customized integer range variable

            if ipInteger[0] not in ipRange1:    # checks if the first list element is in one of the specified range variables
                return validIP                  # if not we return the value of 'validIP' to the main script. 
            
            elif ipInteger[1] not in ipRange1:  # checks if the second list element is in one of the specified range variables
                return validIP                  # if not we return the value of 'validIP' to the main script.

            elif ipInteger[2] not in ipRange1:  # checks if the third list element is in one of the specified range variables
                return validIP                  # if not we return the value of 'validIP' to the main script. 

            elif ipInteger[3] not in ipRange2 or ipInteger[3] ==0:
                return validIP                  # checks if the fourth list element is in one of the specified range variables
                                                # or if its value is equal to 0, if not in the specified ipRange variable or its
                                                # equal to 0 we return the value of 'validIP' to the main script.
            else:
                validIP = True
                return validIP                  # changes the value of 'validIP' to the boolean value "True" 
                                                # and returns the value of 'validIP' to the main script.


def updateDevInterface(devIPAddr, devIntName, devIntIP):
    url = "https://" + devIPAddr + ":443/restconf/data/ietf-interfaces:interfaces/interface=" + devIntName
    username = 'cisco'
    password = 'cisco'                                                  # This function is desined to send a YANG RESTCONF API request to
    payload={"ietf-interfaces:interface": {                             # an IOS XE device. The variables "devIPAddr" & "devIntName" are
                        "name": devIntName,                             # passed through to be used in the URL. The specific URL here 
                        "description": "Configured by RESTCONF",        # allows us to access the interface represented by the variable
                        "type": "iana-if-type:ethernetCsmacd",          # "devIntName" and allows us to change the IP address of the 
                        "enabled": "true",                              # selected interface, which is represented by the variable
                        "ietf-ip:ipv4": {                               # "devIntIP" in the code block here.
                                        "address": [{
                                            "ip": devIntIP,
                                            "netmask": "255.255.255.252"
    }]}}}

    headers = {
      'Authorization': 'Basic cm9vdDpEX1ZheSFfMTAm',
      'Accept': 'application/yang-data+json',
      'Content-Type': 'application/yang-data+json'
    }

    response = requests.request("PUT", url, auth=(username,password),headers=headers, verify = False, data=json.dumps(payload))
    
    print(response.text)





###################################
     # Start of Main Script #
###################################

deviceIP = "10.10.20.175"                                   # The IP address of the device we want to access

intList = getInterfaces(deviceIP)                           # List variable defined by running the getInterfaces() function

intStateList = getIntState(deviceIP)                        # List variable defined by running the getIntState() function

combinedList = combinedIntList(intList, intStateList)       # Function that combines "intList" & "intStateList" into one list

print()                                                     # Prints a blank line for easier readability

printIntInfo(combinedList)                                  # Function that prints out the interface information in a specified format

print()                                                     # Prints a blank line for easier readability

modifyInterface = input("Would you like to modify an interface?: ") # Ask the user if they would like to modify an interface & stores the
                                                                    # response in the variable "modifyInterface"

if modifyInterface.lower() == "y" or modifyInterface.lower() == "yes":  # An 'if' statement that takes the user response in "modifyInterface"
                                                                        # and checks to see if it meets the specified criteria. If so, then
                                                                        # the following codeblock is ran. Otherwise the script will jump down
                                                                        # to the corresponding 'else' line.

                                                                        # This part of the code sets a control variable, "modifyDevice" to
    modifyDevice = True                                                 # the boolean value 'True'. The below codeblock will run as long as
    while modifyDevice == True:                                         # the variable "modifyDevice" is equal to 'True'.

        validIntName = False
        while validIntName == False:                                        # This section of code is used to validate a user input.
                                                                            # First we set a control variable, "validIntName" to the
            intName = input("Which interface do you want to modify?: ")     # boolean value 'False'. Next we create a 'while' loop 
                                                                            # that for as long as the value of the control variable is 
            if intName in str(intList):                                     # false will prompt the user to enter the name of an 
                validIntName = True                                         # interface, defined as "intName". We then take that variable
                                                                            # and use it in an 'if' statement that will check to see if the
            else:                                                           # user input string is in the variable 'intList' after 'intList'
                print("Invalid interface")                                  # is converted into a string. If it is the control variable is 
                print()                                                     # changed to "True" and exits the 'while' loop. Otherwise the 
                                                                            # error message is printed and we remain in the 'while' loop.


        validIntIP = False
        while validIntIP == False:                                          # This section of code is used to validate a user input.
                                                                            # First we set a control variable, "validIntIP" to the boolean
            intIP = input("Enter a new IP address for " + intName + ": ")   # value 'False'. Next we create a 'while' loop that for as long
                                                                            # as the value of the control variable is false will prompt the 
            if validateIPAddress(intIP) == True:                            # user to enter a new IP address for the previously selected
                validIntIP = True                                           # interface, defined as "intIP". We then take that variable and
                                                                            # use it in an 'if' statement that will check to see if the user
            else:                                                           # input string meets the criteria for a valid IP address. If it is
                print("Invalid IP address. IP address must be in the "      # the control variable is changed to "True" and exits the 'while'
                      "following format: x.x.x.y where x>= 0 and x <= "     # loop. Otherwise the error message is printed and we remain in
                      "255, and y >=1 and y<=254")                          # the 'while' loop.
                print()


        updateDevInterface(deviceIP, intName, intIP)                # The updateDevInterface() function runs to update the interface
                                                                    # IP address of the user selected interface.


        intList = getInterfaces(deviceIP)                           # Re-runs the getInterfaces() function to update the "intList" 
                                                                    # variable with the user made changes
                                                                    
        combinedList = combinedIntList(intList, intStateList)       # Re-runs the combinedIntList() function to update the "combinedList"
                                                                    # variable with the user made changes
                                                                    
        print()                                                     # Prints a blank line for easier readability

        printIntInfo(combinedList)                                  # Function that prints out the interface information in a specified format

        print()                                                     # Prints a blank line for easier readability
    
        modifyAgain = input("Would you like to modify another interface?: ")
    
        if modifyAgain.lower() == "y" or modifyAgain.lower() == "yes":      # This section of code prompts the user if they would like to
            modifyDevice = True                                             # modify another interface on the device. If the user input, 
        else:                                                               # represented by the variable "modifyAgain", meets the specified
            modifyDevice = False                                            # criteria, the control variable from above, "modifyDevice" 
            print("*-*-* SCRIPT ENDED *-*-*")                               # remains set to 'True' and we stay in the 'while' loop. If 
                                                                            # "modifyAgain" does not meet the specified criteria, the value of
                                                                            # the control variable is changed to 'False', the print statement
                                                                            # is printed to the screen and we exit the 'while' loop and end 
                                                                            # the script.


else:
    print("*-*-* SCRIPT ENDED *-*-*")               # This last line of the script is where we will end up if the user entered
                                                    # anything other than "Y" or "Yes" on line 182. This will print out the print
                                                    # message and end the script.











