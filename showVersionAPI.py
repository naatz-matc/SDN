def sendCLI(commandName):   #this requests to return the output of the sepcified command from a device
    
    import requests         #imported module to request information from websites and APIs
    import json             #imported module to allow handling of raw json data

    """
    Modify these please
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
            #defining the response we get back from the nxapi. The 'verify=False' is to allow acceptance of untrusted certificates
    response = requests.post(url,data=json.dumps(payload), verify = False, headers=myheaders,auth=(switchuser,switchpassword)).json()

    return response                 #returns the variable to the main script


def printResult(varName):           #this function prints out the variable passed through it in a specific way
    
    print("Device hostname: " + varName["result"]["body"]["host_name"])  #parses through the passed through dictionary variable to access
                                                                         #the specified 'value' of the 'key:value' dictionary pair
    
    print("Device memory: " + str(varName["result"]["body"]["memory"]) + " " + varName["result"]["body"]["mem_type"])
                                    #parses through the passed through dictionary variable to access the specified 'value' of the
                                    #'key:value' dictionary pair. The 'memory' value is an integer so it needs to be converted into
                                    #a string to be concatenated



#######################
# Start of Main Script
#######################


commandResponse = sendCLI("show version")   #variable created from executing the function

printResult(commandResponse)                #function runs with the passed in variable
