import xml.etree.ElementTree as ET
import xmltodict
import xml.dom.minidom
from lxml import etree
from ncclient import manager
from collections import OrderedDict

def netconfGetIntInfo(device):                                      # This function makes a NETCONF API call to a specified device. The API call
                                                                    # in this case is for the interface information from the specified device.
    netconf_filter = """                 
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface></interface>
    </interfaces>
       
    """

    with manager.connect(host=device['host'],port=device['port'],username=device['username'],password=device['password'],hostkey_verify=False) as m:

        netconf_reply = m.get_config(source = 'running', filter = ("subtree",netconf_filter))


    netconf_data = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]      # Parse returned XML to Dictionary

    interfaces = netconf_data["interfaces"]["interface"]                        # Create List of Interfaces

    return interfaces


def printIntInfo(interfaces):                                                                 # This function takes in the passed through
                                                                                              # ordered dictionary variable "interfaces" and 
    print("Interface" + "\t\t" + "IP Address" + "\t   " + "Netmask" + "\t\t" + "Description") # is designed to print out the specified info in
    print("-"*16 + "\t" + "-"*15 + "\t   " + "-"*14 + "\t" + "-"*25)                          # a human-readable format. The function has a
    for interface in interfaces:                                                              # 'for' loop to iterate through all of the 
        if not interface["name"].startswith("L"):                                             # interfaces and print out their specified info.
            print(interface["name"] + "\t" + interface["ipv4"]["address"]["ip"] + "\t   " +   # ther is also an 'if not' statement designed to 
                  interface["ipv4"]["address"]["netmask"] + "\t" + interface["description"])  # omit the iteration of the Loopback interface.


def validateInterface(ordDict, inputInt):               # This function checks to see if the interface represented by 
                                                        # the variable "inputInt" is in the list variable "ordDict".
    validInt = False                                    # First a boolean-value variable called "validInt" is initially
                                                        # set to 'False'. Next we iterate through the list to see if the
    for interface in ordDict:                           # value of inputInt is in the specified spot of the ordered 
        if inputInt == interface["name"]:               # dictionary. If it is we change the value of "validInt" to 
            validInt = True                             # 'True', if not it will remain 'False' and we then return the
                                                        # value of "validInt" to the main script.
    return validInt


def validateIPAddress(ipString):        # This function verifies if the passed through variable is a valid IP address
    
    validIP = False                     # Boolean-value variable initially set to 'False'
    
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


def validateNetmask(netmask, netmaskList):
    validNetmask = False                                                    # This variable is initially set to the boolean value
                                                                            # 'False'
    userMaskList = netmask.split(".")
    if len(userMaskList) !=4:
        return validNetmask
    elif userMaskList[0] not in maskList:                                   # These series of 'if' and 'elif' statements check to
        return validNetmask                                                 # see if each list element in the list variable 
    elif userMaskList[1] not in maskList:                                   # "userMaskList" is in the other list variable "maskList"
        return validNetmask                                                 # If not, the variable "validNetmask" is returned to the
    elif userMaskList[2] not in maskList:                                   # main script.
        return validNetmask
    elif userMaskList[3] not in maskList:
        return validNetmask
    else:
        if userMaskList[0] == '255':                                        # Checks to see if the first element in "userMaskList" is
            if userMaskList[1] == '255' and userMaskList[2] == '255':       # equal to '255', if so we then check to see if the next
                if userMaskList[3] != '255':                                # two list elements are also '255'. Finally if so we check
                    validNetmask = True                                     # to see if the last list element is not '255'. If yes we
                    return validNetmask                                     # change "validNetmask" to 'True' and return it to the main
                else:                                                       # script, if no we return "validNetmask" to the main script.
                    return validNetmask                                             
            elif userMaskList[1] < '255':                                   # Checks to see if the second element in "userMaskList" is 
                if userMaskList[2] == '0' and userMaskList[3] == '0':       # less than '255'. If so we then check to see if the third and
                    validNetmask = True                                     # fourth elements are BOTH equal to '0'. If they are we change
                    return validNetmask                                     # the value of "validNetmask" to 'True' and return it to the 
                else:                                                       # main script. If the second element is NOT less than '255', we
                    return validNetmask                                     # return the unchanged variable "validNetmask" to the main script.
                
            elif userMaskList[2] < '255':           # Checks to see if the third element in "userMaskList" is less than '255'. If so we then
                if userMaskList[3] == '0':          # check to see if the fourth element is equal to '0'. If so we change the value of
                    validNetmask = True             # "validNetmask" to 'True' and return it to the main script. If the third element is NOT
                    return validNetmask             # equal to '0', we return the unchanged variable "validNetmask" to the main script.
                else:
                    return validNetmask
        elif userMaskList[0] != '255':
            if userMaskList[1] == '0' and userMaskList[2] == '0' and userMaskList[3] == '0':
                validNetmask = True                     
                return validNetmask             # This is the part of the function that gets executed if the first element in "userMaskList"
            else:                               # is NOT equal to '255'. If all of the remaining elements in "userMaskList" equal '0', then
                return validNetmask             # we change the value of "validNetmask" to 'True' and return it to the main script. If any of
                                                # the remaining elements in "userMaskList" are NOT equal to '0', then we return the value of
                                                # "validNetmask" to the main script.


def updateDeviceInfo(inputInt, ipString, netmask, deviceInfo):  # This function takes in four variables: "inputInt", "ipString", "netmask"
    for interface in deviceInfo:                                # and a list variable called "deviceInfo". A 'for' loop is used to see which
        if interface["name"] == inputInt:                       # interface in "deviceInfo" matches the interface represented by "inputInt".
            interface["ipv4"]["address"]["ip"] = ipString       # Once that interface is found, the corresponding ordered dictionary values
            interface["ipv4"]["address"]["netmask"] = netmask   # are changed to the other passed through variables of "ipString" & "netmask".

    return deviceInfo                                           # Returns the updated variable "deviceInfo" to the main script.


#######################################
    # Main Script Starts Below #       
#######################################

router = {"host": "10.10.20.175", "port" : "830",               # A dictionary variable with 'key:value' pair values
          "username":"cisco","password":"cisco"}                # that are needed to make the NETCONF.

devInfo = netconfGetIntInfo(router)                             # Runs the netconfGetIntInfo() function and returns the resulting 
                                                                # ordered dictionary to a variable called "devInfo".
                                                                
printIntInfo(devInfo)                                           # Takes the variable "devInfo" and prints out the specified info
                                                                # defined in the printIntInfo() function.
                                                                
print()                                                         # Blank line printed for readability

modifyInterface = input("Would you like to modify an interface?: ") # Ask the user if they would like to modify an interface & stores the
                                                                    # response in the variable "modifyInterface"

if modifyInterface.lower() == "y" or modifyInterface.lower() == "yes":  # An 'if' statement that takes the user response in "modifyInterface"
                                                                        # and checks to see if it meets the specified criteria. If so, then
                                                                        # the following codeblock is ran. Otherwise the script will jump down
                                                                        # to the corresponding 'else' line.
                                                                        
    modifyDevice = True                                 # This part of the code sets a control variable, "modifyDevice" to the boolean
    while modifyDevice == True:                         # value 'True'. The below codeblock will run as long as the variable
                                                        # "modifyDevice" is equal to 'True'.

        validIntName = False                                            # Boolean control variable "validIntName" is set to 'False'

        while validIntName == False:                                    # A 'while' loop to validate the interface begins
            
            intToChange = input("Which interface would you like to modify?: ")  # Prompts the user to enter an interface to change

            validIntName = validateInterface(devInfo, intToChange)              # Sets the boolean variable "validIntName" by running the
                                                                                # validateInterface() function with the passed through variables
                                                                                # "devInfo" & "intToChange".

            if validIntName == False:
                print()                                                                         # If the value of "validIntName" is 'False', an error
                print("Invalid interface. Please choose an interface from the list above.")     # message is printed to the screen and we stay in the
                                                                                                # 'while' loop. If the value is 'True', we exit the
            else:                                                                               # 'while' loop.
                print()

        validIntIP = False                                              # Boolean control variable "validIntIP" is set to 'False'

        while validIntIP == False:                                      # A 'while' loop to validate the IP address begins

            ipToChange = input("Enter a new IP address for " + intToChange + ": ")  # Prompts the user to enter an IP address

            validIntIP = validateIPAddress(ipToChange)                  # Sets the boolean variable "validIntIP" by running the "validateIPAddress()"
                                                                        # function with the passed through variable "ipToChange".
            if validIntIP == False:
                print()
                print("Invalid IP address. IP address must be in the "  # If the value of "validIntIP" is 'False', an error message is printed to the
                      "following format: x.x.x.y where x >=0 and x <="  # screen and we stay in the 'while' loop. If the value is 'True', we exit
                      "255, and y >=1 and y <=254")                     # the 'while' loop.
            else:
                print()

        maskList = ['255','254', '252', '248', '240', '224', '192', '128', '0'] # List variable containing all the possible netmask octet values

        validNetmask = False                                            # Boolean control variable "validNetmask" is set to 'False'

        while validNetmask == False:                                    # A 'while' loop to validate the IP address begins

            maskToChange = input("Enter the netmask address for " + intToChange + ": ") # Prompts the user to enter a netmask address

            validNetmask = validateNetmask(maskToChange, maskList)      # Sets the boolean variable "validNetmask" by running the "validateNetmask()"
                                                                        # function with the passed through variables "maskToChange" & "maskList".
                                                                        
            if validNetmask == False:                                   # If the value of "validNetmask" is 'False', an error message is printed to
                print()                                                 # the screen and we will stay in the 'while' loop. If the value is 'True',
                print("**** ERROR: Invalid netmask ****")               # we exit the 'while' loop.

            else:
                print()

        devInfo = updateDeviceInfo(intToChange, ipToChange, maskToChange, devInfo) # Updates the value of "devInfo" by running the
                                                                                   # updateDeviceInfo() function with the passed through variables
                                                                                   # "intToChange", "ipToChange", "maskToChange", & the existing value
                                                                                   # of "devInfo".
                                                                                   
        printIntInfo(devInfo)                                   # Runs the function printIntInfo() with the passed through variable "devInfo"

        print()                                                 # Blank line printed for readability
        
        modifyAgain = input("Would you like to modify another interface?: ")
    
        if modifyAgain.lower() == "y" or modifyAgain.lower() == "yes":      # This section of code prompts the user if they would like to
            modifyDevice = True                                             # modify another interface on the device. If the user input, 
        else:                                                               # represented by the variable "modifyAgain", meets the specified
            modifyDevice = False                                            # criteria, the control variable from above, "modifyDevice"
            print()                                                         # remains set to 'True' and we stay in the 'while' loop. If 
            print("*-*-* SCRIPT ENDED *-*-*")                               # "modifyAgain" does not meet the specified criteria, the value of
                                                                            # the control variable is changed to 'False', the print statement
                                                                            # is printed to the screen and we exit the 'while' loop and end 
                                                                            # the script. 
                                          
else:
    print()                                         # Blank line printed for readability
    
    print("*-*-* SCRIPT ENDED *-*-*")               # This last line of the script is where we will end up if the user entered
                                                    # anything other than "Y" or "Yes" on line 159. This will print out the print
                                                    # message and end the script.




          
