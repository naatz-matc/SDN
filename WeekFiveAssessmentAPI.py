def sendCLI(commandName):   #this requests to return the output of the sepcified command from a device
    
    import requests         #imported module to request information from websites and APIs
    import json             #imported module to allow handling of raw json data

    """
    Be sure to run feature nxapi first on Nexus Switch

    """
    switchuser='cisco'      #username needed to access the device
    switchpassword='cisco'  #password needed to access the device

    url='https://10.10.20.177/ins'                      #the management IP address for the device being accessed
    myheaders={'content-type':'application/json-rpc'}
    payload=[
      {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
          "cmd": commandName,       #the string variable that is passed through the function is inserted here
          "version": 1
        },
        "id": 1
      }
    ]

    '''

    verify=False below is to accept untrusted certificate

    '''
    #defining the response we get back from the nxapi
    interfaceDict = requests.post(url,data=json.dumps(payload), verify=False,headers=myheaders,auth=(switchuser,switchpassword)).json()
    
                                                                               #creating a variable that parses through the json response
    listInterfaces = interfaceDict["result"]["body"]["TABLE_intf"]["ROW_intf"] #and creates a list that contains dictionaries of each 
                                                                               #interface and its information
    return listInterfaces       #returns the variable to the main script



def printList(varName):                                                 #this function prints out the variable 
    print("Name" + "\t" + "Proto" + "\t" + "Link" + "\t" + "Address")   #passed through it in a specific way
    print("-"*4 + "\t" + "-"*5 + "\t" + "-"*4 + "\t" + "-"*7)
    for dictionary in varName:
        print(dictionary["intf-name"] + "\t" + dictionary["proto-state"] + "\t" + dictionary["link-state"] + "\t" + dictionary["prefix"])
                            #a 'for' loop that for each dictionary in the list "varName" it should print out the
                            #specific ["value"] for each specified dictionary["key"]

#######################
# Start of Main Script
#######################

interfaceList = sendCLI("show ip interface brief")

printList(interfaceList)


