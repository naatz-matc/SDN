import requests             #imported module to request information from websites and APIs
import json                 #imported module to allow handling of raw json data

def sendCLI(mgmtIP,commandName):   #this function takes two inputs: a management IP address 
                                   #and a specified device command
    """
    Modify these please
    """
    switchuser='cisco'      #username needed to access the device
    switchpassword='cisco'  #password needed to access the device

    url='https://' + mgmtIP + '/ins'                      #the management IP address for the device being accessed
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

    dictionary = {'Hostname' : response["result"]["body"]["host_name"],         #creates a custom dictionary with our
                  'Memory' : response["result"]["body"]["memory"],              #pre-determined custom keys with the
                  'Type' : response["result"]["body"]["mem_type"],              #values being the parsed-through info
                  'Boot File' : response["result"]["body"]["kick_file_name"],   #from our 'response' variable
                  'Chassis' : response["result"]["body"]["chassis_id"]
                  }

    return dictionary                 #returns the variable to the main script


#########################
# Start of Main Script
#########################

commandResponse1 = sendCLI("10.10.20.177","show version")       #defines the dictionary returned from the function

commandResponse2 = sendCLI("10.10.20.178","show version")       #defines the dictionary returned from the function

commandDictionary = {"device1" : commandResponse1, "device2" : commandResponse2} #creates a nested dictionary using keys called 'device1' &
                                                                                 #'device2' and values of the previously created dictionaries
print()     #added print line for readability

print("Hostname" + "\t" + "Memory" + "\t\t" + "Chassis" + "\t\t\t\t" + "Boot File") #print statements that create column headers for the 
print("-"*10 + "\t" + "-"*10 + "\t" + "-"*23 + "\t\t" + "-"*30)                     #displayed info in a friendly human readable format

for key in commandDictionary:
    print(commandDictionary[key]["Hostname"] + "\t" + str(commandDictionary[key]["Memory"]) + " " + commandDictionary[key]["Type"] +
          "\t" + commandDictionary[key]["Chassis"] + "\t\t" + commandDictionary[key]["Boot File"])
                                                #this 'for' loop is set up so that for each MAIN 'key' in the dictionary "commandDictionary" 
                                                #it will print to the screen the NESTED dictionary 'values' for each specified
                                                #NESTED dictionary 'key' in a friendly human readable format
    
print()     #added print line for readability












