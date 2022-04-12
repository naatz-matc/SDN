import requests                                                  # imported module to request information from websites and APIs
import json                                                      # imported module to allow handling of raw json data
    
def printDevices(devices):                                       # This function is set up to take an input in its parentheses
    print("Devices" + "\t\t" + "Mgmt IP")                        # and prints out a specified formatted list of the dictionary
    print("-"*9 + "\t" + "-"*15)
    for device in devices.keys():                                
        print(devices[device]["hostname"] + "\t" + devices[device]["mgmtIP"])
        
                                                                # this 'for' loop will go through each 'key' in the specified dictionary
                                                                # and print to the screen the specified values in each nested dictionary
                                                            
def getCookie(addr):                                            # This function, using the passed through variable representing a                                             
    url = "https://"+ addr + "/api/aaaLogin.json"               # management IP, retrieves the specified device Session Cookie so that
                                                                # we can access and modify this device through its API
    payload= {"aaaUser" :
              {"attributes" :                                   # username and password to access the device
                   {"name" : "cisco",
                    "pwd" : "cisco"}
               }
          }

    response = requests.post(url, json=payload, verify = False)             # the raw data response from the selected device

    
    return response.json()["imdata"][0]["aaaLogin"]["attributes"]["token"]  # converts the response variable into a json format, parses
                                                                            # through the converted data to get the Session Cookie and
                                                                            # returns the Session Cookie to the main script

def changeHostname(address, hostname, cookie):
    url = "https://" + address + "/api/mo/sys.json"
                                                                # This function takes in three variables. "address" representing a
    payload = {                                                 # specified management IP, "hostname" representing the new device
      "topSystem": {                                            # hostame, and "cookie" representing the specified device Session
        "attributes": {                                         # Cookie. This function will send the new hostname to the specified
          "name": hostname                                      # device which will authenticate the communication with the specified
    }}}                                                         # Session Cookie

    headers = {
        'Content-Type' : 'text/plain',
        'Cookie' : 'APIC-cookie=' + cookie
    }
                                                                # verify = False to accept without a ssl certificate
    response = requests.request("POST", url, verify = False, headers=headers, data=json.dumps(payload)) 
                                                                             # sends the payload to the specified device API, which
                                                                             # will changed the device's hostname
def getHostname(address, cookie):
    url = "https://" + address + "/api/node/mo/sys.json?query-target=self"
                                                                            # This function takes in two variables and is designed
    payload = {}                                                            # to get a raw data response that includes the current
                                                                            # hostname of the specified device. Then the returned
    headers = {                                                             # response is converted into json and parsed through
        'Content-Type' : 'applicaton/json',                                 # to isolate the hostname part of the response and return
        'Cookie' : 'APIC-cookie=' + cookie                                  # it to the main script
        }
                                                                 # verify = False to accept without a ssl certificate
    response = requests.request("GET", url, headers=headers, verify = False, data=payload) 
    return response.json()["imdata"][0]["topSystem"]["attributes"]["name"]

def validateHostname(hostname, validationString):
    validHost = True                                # creates a variable named 'validHost' and sets its value to the boolean value "True"
    if len(hostname) == 0 or len(hostname) >64:     # checks the length of 'hostname'. If the length is equal to zero
        print(validationString)                     # or greater than 64 characters, it sets 'validHost' value to "False" and
        validHost = False                           # prints out the 'validationString' message
                          
    else:
        if hostname[0].isalpha() == False:          # checks if the first character in 'hostname' is an alpha character. If the
            print(validationString)                 # first character is not an alpha character, it sets 'validHost' value to "False"
            validHost = False                       # and prints out the 'validationString' message

        else:
            
            if len(hostname.split()) >1:            # checks if the 'hostname' string has any spaces between any of its
                print(validationString)             # characters. If there are any spaces, it sets 'validHost' value to "False"
                validHost = False                   # and prints out the 'validationString'

    return validHost                                # returns the variable and its value to the main script

def validateIPAddress(ipAddr, validationString):
    validIP = True                      # creates a variable named 'validIP' and sets its value to the boolean value "True"
    ipList = ipAddr.split(".")          # asks the user to input an IP address, once entered it creates a list from the user
                                        # input, splitting up the string into list elements by the "." in the IP address
    if len(ipList) !=4:
        print(validationString)         # checks if the length of 'ipList' is not equal to 4, if not we print out the
        validIP = False                 # 'validationString' message, change 'validIP' to "False"

    else:
        ipNumCheck = ipAddr.replace(".","",4)   # creates a new variable by replacing all the "." in 'ipAddr' with nothing
        
        if ipNumCheck.isnumeric() == False:     # checks if all the characters in 'ipNumCheck' are numerical, if not we print 
            print(validationString)             # out the 'validationString' message, change 'validIP' to "False"
            validIP = False                        

        else:
            ipInteger = ([int(x) for x in ipList]) # creates a new variable that changes the date type in 'ipList' to integers
            ipRange1 = range(256)                  # customized integer range variable
            ipRange2 = range(255)                  # customized integer range variable

            if ipInteger[0] not in ipRange1:    # checks if the first list element is in one of the specified range variables
                print(validationString)         # if not we print out the 'validationString' message, change 'validIP' to "False"
                validIP = False                    
            
            elif ipInteger[1] not in ipRange1:  # checks if the second list element is in one of the specified range variables
                print(validationString)         # if not we print out the 'validationString' message, change 'validIP' to "False"
                validIP = False                    

            elif ipInteger[2] not in ipRange1:  # checks if the third list element is in one of the specified range variables
                print(validationString)         # if not we print out the 'validationString' message, change 'validIP' to "False"
                validIP = False                     

            elif ipInteger[3] not in ipRange2 or ipInteger[3] ==0:
                print(validationString)         # checks if the fourth list element is in one of the specified range variables
                validIP = False                 # or if its value is equal to 0, if not in the specified ipRange variable or its
                                                # equal to 0 we print out the 'validationString' message, change 'validIP' to "False"
                                                
    return validIP                              # returns the variable "validIP" back to the main script

###############################
# Start of Main Script #
###############################

sessionCookie1 = getCookie("10.10.20.177")                          # Gets Session Cookie for NX switch. Cookie is good for 600 seconds
device_1_Hostname = getHostname("10.10.20.177", sessionCookie1)     # Gets the current hostname of the specified device

sessionCookie2 = getCookie("10.10.20.178")                          # Gets Session Cookie for NX switch. Cookie is good for 600 seconds
device_2_Hostname = getHostname("10.10.20.178", sessionCookie2)     # Gets the current hostname of the specified device

deviceDict = {
    'device_1' : {                                                   
        'hostname' : device_1_Hostname ,                            # initially defines the dictionary "deviceDict" using the passed
        'mgmtIP' : '10.10.20.177'                                   # through varialbles of 'device_1_Hostname' and 'device_2_Hostname
        },                                                          # previously defined from running the getHostname() function
    'device_2' : {                                                   
        'hostname' : device_2_Hostname ,                        
        'mgmtIP' : '10.10.20.178'
}}

printDevices(deviceDict)                                            # function prints the info from the 'deviceDict'
                                                                    # dictionary in a specified readable format


print()                                                             # blank line printed for readability

validIP = False                                     # This 'while' loop verifies if the user entered a valid IP address by creating a 
while validIP == False:                             # variable that asks for user input. Then it passes that variable to a function called
    validIP = True                                  # validateIPAddress() that will check to see if the user entered IP is valid. If it is
                                                    # the function keeps the control variable 'validIP' "True" and exits the 'while' loop
                                                    
    ipAddress = input("Please enter the management "
                      "IP address of the device you "
                      "want to access: ")
    
    validIP = validateIPAddress(ipAddress, "IP address must be in the following format: x.x.x.y where x>= 0 and x <= 255, "
                                           "and y >=1 and y<=254")

validHost = False                                   # This 'while' loop verifies if the user entered a valid hostname by creating a variable
while validHost == False:                           # that asks for user input. Then it passes that variable to a function called
    validHost = True                                # validateHostname() that will check to see if the user entered hostname is valid. If it
                                                    # is the function keeps the control variable 'validHost' "True" and exits the 'while' loop
                                                    
    newHostname = input("Please enter the new "
                        "hostname for the selected device: ")
    
    validHost = validateHostname(newHostname, "Invalid hostname. Hostname must start with a letter, not be "
                                 "seperated by spaces and less than 64 characters")

# The following 'if' statement is used to decide which Session Cookie
# to use to change the device hostname based on the value of the
# variable "validIP"

sessionCookie1 = getCookie("10.10.20.177")                  # Gets Session Cookie for NX switch. Cookie is good for 600 seconds
sessionCookie2 = getCookie("10.10.20.178")                  # Gets Session Cookie for NX switch. Cookie is good for 600 seconds
   
if ipAddress == "10.10.20.177":
    changeHostname(ipAddress, newHostname, sessionCookie1)      # Changes the hostname of a device using the 'changeHostname() function
                                                                # which takes in the passed through variables "ipAddress", "newHostname"
                                                                # and "sessionCookie"

if ipAddress == "10.10.20.178": 
   changeHostname(ipAddress, newHostname, sessionCookie2)       # Changes the hostname of a device using the 'changeHostname() function
                                                                # which takes in the passed through variables "ipAddress", "newHostname"
                                                                # and "sessionCookie"

device_1_Hostname = getHostname("10.10.20.177", sessionCookie1) # Gets the current hostname of the specified device
device_2_Hostname = getHostname("10.10.20.178", sessionCookie2) # Gets the current hostname of the specified device

deviceDict = {
    'device_1' : {
        'hostname' : device_1_Hostname ,                        # re-defines the dictionary "deviceDict" using the passed through
        'mgmtIP' : '10.10.20.177'                               # varialbles of 'device_1_Hostname' and 'device_2_Hostname that were
        },                                                      # re-defined from running the changeHostname() function
    'device_2' : {
        'hostname' : device_2_Hostname ,
        'mgmtIP' : '10.10.20.178'
}}

print()                                                         # blank line printed for readability

printDevices(deviceDict)                                        # function prints the info from the 'deviceDict'
                                                                # dictionary in a specified readable format
