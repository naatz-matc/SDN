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


def getInterfaceInfo(address, cookie):
    url = "https://" + address + "/api/node/mo/sys/ipv4/inst/dom-default.json?query-target=children"
                                                                            # This function takes in two variables and is designed
    payload = {}                                                            # to get a raw data response that includes the current
                                                                            # interface info of the specified device. Then the returned
    headers = {                                                             # response is converted into json and parsed through
        'Content-Type' : 'applicaton/json',                                 # to isolate the interface part of the response and return
        'Cookie' : 'APIC-cookie=' + cookie                                  # it to the main script
        }
                                                                 # verify = False to accept without a ssl certificate
    response = requests.request("GET", url, headers=headers, verify = False, data=payload)
    return response.json()["imdata"]


def printList(intList):                                                                                 # This function takes in a list
    for element in intList:                                                                             # variable, uses a 'for' loop to 
        print(element["ipv4If"]["attributes"]["dn"] + "\t" + element["ipv4If"]["attributes"]["id"])     # parse through the list to find
                                                                                                        # the specified info and displays
                                                                                                        # the info to the screen



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

ipAddress = input("Please enter the management "                    # asks the user to enter the management IP of the desired device
                  "IP address of the device you "                   # and stores the response in the variable "ipAddress"
                  "want to access: ")

if ipAddress == "10.10.20.177":
    sessionCookie1 = getCookie("10.10.20.177")              # Gets Session Cookie for NX switch. Cookie is good for 600 seconds
    intInfo = getInterfaceInfo(ipAddress, sessionCookie1)   # gets the interface information for the specified host using the 
    printList(intInfo)                                      # getInterfaceInfo() function which takes in the passed through variables 
                                                            # "ipAddress" and "sessionCookie". Then the printList() function displays
                                                            # the information to the screen in a specific way
if ipAddress == "10.10.20.178":
   sessionCookie2 = getCookie("10.10.20.178")               # Gets Session Cookie for NX switch. Cookie is good for 600 seconds 
   intInfo = getInterfaceInfo(ipAddress, sessionCookie2)    # gets the interface information for the specified host using the
   printList(intInfo)                                       # getInterfaceInfo() function which takes in the passed through variables
                                                            # "ipAddress" and "sessionCookie". Then the printList() function displays
                                                            # the information to the screen in a specific way
