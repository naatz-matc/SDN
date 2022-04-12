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

    interfaceDictionary = response.json()                   # Here the response from the device is converted into JSON, 
                                                            # assigned to a variable called "interfaceDictionary", and
    return interfaceDictionary                              # returned to the main script



def printInterfaces(intDict):
                                                                        # This function takes in the variable "intDict" and uses it to
    print()                                                             # print out the specified information in a specifically formatted
    print("Interface" + "\t\t" + "Address" + "\t\t" + "Netmask")        # way. This format has an 'if not' statement which will omit printing
    print("-"*16 + "\t" + "-"*15 + "\t" + "-"*15)                       # out the information regarding any Loopback interfaces
    for element in intDict["ietf-interfaces:interfaces"]["interface"]:
        if not element["name"].startswith("L"):
            print(element["name"] + "\t" + element["ietf-ip:ipv4"]["address"][0]["ip"] + "\t" + element["ietf-ip:ipv4"]["address"][0]["netmask"])


##########################
# Start of Main Script
##########################

deviceIP = "10.10.20.175"                                   # The IP address of the device we want to access

interfaceDict = getInterfaces(deviceIP)                     # Dictionary variable defined by running the getInterfaces() function

printInterfaces(interfaceDict)                              # Interface information for the device printed out by passing the
                                                            # "interfaceDict" dictionary variable into the printInterfaces() function

