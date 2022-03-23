import requests                                     # imported module to request information from websites and APIs
import json                                         # imported module to allow handling of raw json data

def sendCLI(mgmtIP):                                # this function returns the output of the sepcified command from a device
    
    switchuser='cisco'                              # username needed to access the device
    switchpassword='cisco'                          # password needed to access the device

    url='https://' + mgmtIP + '/ins'                    # the management IP address for the device being accessed
    myheaders={'content-type':'application/json-rpc'}
    payload=[
      {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
          "cmd": "show ip interface brief",
          "version": 1
        },
        "id": 1
      }
    ]
                                                    # defining the response we get back from the nxapi
    response = requests.post(url,data=json.dumps(payload), verify = False, headers=myheaders,auth=(switchuser,switchpassword)).json()


    return response                                 # returns the variable to the main script

##############################################

def modifyIPAddress(ipAddress):                         # this function changes the value of a passed through IP address
    ipList = ipAddress.split(".")                       # takes the passed through IP address and turns it into a list
    ipList[3] = int(ipList[3])                          # takes the last element of the list and changes it to an integer data type
    ipList[3] = ipList[3]+5                             # takes the last element of the list and increments it the specified value
    ipList[3] = str(ipList[3])                          # takes the last element of the list and changes it back to a string data type
    modifiedIP = ""                                     # creates an empty variable called "modifiedIP"
    for element in ipList:
            modifiedIP = modifiedIP + element + "."     # a 'for' loop that for each list element in "ipList" we append each list element
                                                        # along with a "." to the string variable "modifiedIP".
    modifiedIP = modifiedIP.rstrip(".")                 # strips the last "." in "modifiedIP" to create a valid IP address
            
    return modifiedIP                                   # returns the variable to the main script

###############################################

def changeVlanIP(mgmtIP, vlans, IPAddress):             # this function changes the interface IP address using the passed through variables

    switchuser='cisco'                                  # username needed to access the device
    switchpassword='cisco'                              # password needed to access the device

    url='https://' + mgmtIP + '/ins'                    # the management IP address for the device being accessed
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
          "cmd": "interface " + vlans,                  # the specified interface to be changed
          "version": 1
        },
        "id": 2
      },
      {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
          "cmd": "IP address " + IPAddress + " 255.255.255.0",  # the specified IP Address that the specified
          "version": 1                                          # interface is to be changed to
        },
        "id": 3
      }
    ]
                                                        # defining the response we get back from the nxapi
    response = requests.post(url,data=json.dumps(payload), verify = False, headers=myheaders,auth=(switchuser,switchpassword)).json()

####################################

def printList(varName):                                                 # this function prints out the variable 
    print("Name" + "\t" + "Proto" + "\t" + "Link" + "\t" + "Address")   # passed through it in a specified way
    print("-"*4 + "\t" + "-"*5 + "\t" + "-"*4 + "\t" + "-"*7)
    for dictionary in varName:
        print(dictionary["intf-name"] + "\t" + dictionary["proto-state"] + "\t" + dictionary["link-state"] + "\t" + dictionary["prefix"])
                            # a 'for' loop that for each dictionary in the list "varName" it should print out the
                            # specific ["value"] for each specified dictionary["key"]


#####################################
# Start of Main Script
#####################################

devices = {                                     # this is a dictionary of all of the devices we want to change.
    "dist-sw01" : "10.10.20.177",               # dictionary "keys" are the device names and the "Values" are
    "dist-sw02" : "10.10.20.178"                # the management IP addresses of each device
    }

for key in devices:                                                                     # a variable called "interfaceDict" is created from
    interfaceDict = sendCLI(devices[key])                                               # passing through the current 'devices' dictionary
                                                                                        # key to the sendCLI() function.

    printList(interfaceDict["result"]["body"]["TABLE_intf"]["ROW_intf"])                # the existing interface list for the specified
                                                                                        # device is passed through the printList() function.
    
    for dictionary in interfaceDict["result"]["body"]["TABLE_intf"]["ROW_intf"]:        # this 'for' loop will iterate through each dictionary       
                                                                                        # key and issue a "show ip interface brief" command.
        if dictionary["intf-name"].startswith('V'):                                     # This will result in a data dictionary being returned.        
            dictionary["prefix"] = modifyIPAddress(dictionary["prefix"])                # The next 'for' loop will iterate through the returned
                                                                                        # dictionary and for each specified sub-dictionary value
    for dictionary in interfaceDict["result"]["body"]["TABLE_intf"]["ROW_intf"]:        # if that value begins with a 'V', that sub-dictionary      
        if dictionary["intf-name"].startswith('V'):                                     # specified value is passed through to the                         
            changeVlanIP(devices[key], dictionary["intf-name"], dictionary["prefix"])   # modifyIPAddress() function. The next 'for' loop will   
                                                                                        # iterate through the returned dictionary and for each                    
    newInterfaceDict = sendCLI(devices[key])                                            # specified sub-dictionary value if that value begins                                                                                                                                    
                                                                                        # with a 'V', that sub-dictionary's specified values are
                                                                                        # passed through to the changeVlanIP() function.
    printList(newInterfaceDict["result"]["body"]["TABLE_intf"]["ROW_intf"])
                                                                                # After the last 'for' loop a new variable called
                                                                                # "newInterfaceDict" is created from passing through the
                                                                                # current 'devices' dictionary key to the sendCLI() function.
                                                                                # Then the specified list from "newInterfaceDict" is passed
                                                                                # through the printList() function.

    

























