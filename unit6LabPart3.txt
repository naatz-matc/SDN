import requests                 #imported module to request information from websites and APIs
import json                     #imported module to allow handling of raw json data

def getOSPFNeighbor(mgmtIP):        #this function takes a single input, a management IP address, that 
                                    #is used to gather the OSPF neighbor information from that device
    
    """
    Modify these please
    """
    switchuser='cisco'              #username needed to access the device
    switchpassword='cisco'          #password needed to access the device

    url='https://' + mgmtIP + '/ins'                    #the management IP address for the device being accessed
    myheaders={'content-type':'application/json-rpc'}
    payload=[
      {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
          "cmd": "show ip ospf neighbor",       
          "version": 1
        },
        "id": 1
      }
    ]
        #defining the response we get back from the nxapi. The 'verify=False' is to allow acceptance of untrusted certificates
    response = requests.post(url,data=json.dumps(payload), verify = False, headers=myheaders,auth=(switchuser,switchpassword)).json()

    ospfSW = response["result"]["body"]["TABLE_ctx"]["ROW_ctx"]["TABLE_nbr"]["ROW_nbr"] #creates a list for which each list element
                                                                                        #is a dictionary of the desired information
    for element in ospfSW:      #this 'for' loop creates two seperate dictionaries that
        dict1 = ospfSW[0]       #contain the parsed information that we are looking for
        dict2 = ospfSW[1]

    dictionary = {"int_1" : dict1, "int_2" : dict2} #creates a variable that is a nested dictionary with pre-determined keys and values
                                                    #that are the previously created dictionaries from the 'for' loop
    
    return dictionary           #returns the nested dictionary to the main script


def printOSPFNeighbor(ospfNeighborDict):                                #this function takes in one input, a dictionary, and prints
    print("Router ID" + "\t\t" + "Neighbor ID" + "\t\t" + "Interface")  #out the information from that dictionary in a specified way
    print("-"*15 + "\t\t" + "-"*15 + "\t\t" + "-"*9)
    for key in ospfNeighborDict:
        print(ospfNeighborDict[key]["rid"] + "\t\t" + ospfNeighborDict[key]["addr"] + "\t\t" + ospfNeighborDict[key]["intf"])
                                                                        #this 'for' loop is set up so that for each MAIN 'key' in the
                                                                        #dictionary it will print out the specified NESTED 'values' that
                                                                        #correspond to each specified NESTED dictionary 'key' in a
                                                                        #specified way



#########################
# Start of Main Script
#########################

devicesDict = {                         #previously existing nested dictionary with basic information
    "device1" : {
        
        "hostname" : "dist-sw01",
        "deviceType" : "switch",
        "mgmtIP" : "10.10.20.177"
        },
    
    "device2" : {
        
        "hostname" : "dist-sw02",
        "deviceType" : "switch",
        "mgmtIP" : "10.10.20.178"
        }
    }

"""
this 'for' loop is set up so that for each 'device' in the devicesDict dictionary, a variable called "mgmtIP" is defined as the matching
'value' to each devices ["mgmtIP"] 'key'. Once that variable is defined, it is passed to the getOSPFNeighbor() function which will return a
nested dictionary called 'OSPFNeighbor' with all of the desired information. Next the loop will print out the "hostname" value for each device
in the devicesDict dictionary along with some other text. Finally the loop will pass the variable 'OSPFNeighbor' into the printOSPFNeighbor()
function, which will print out the information in the 'OSPFNeighbor' dictionary into a human friendly format.
"""

for device in devicesDict:
    mgmtIP = devicesDict[device]["mgmtIP"]
    OSPFNeighbor = getOSPFNeighbor(mgmtIP)
    print()     #added print line for readability
    print(devicesDict[device]["hostname"] + " OSPF Neighbors:")
    print()     #added print line for readability
    printOSPFNeighbor(OSPFNeighbor)


