import requests                                                 # imported module to request information from websites and APIs
import json                                                     # imported module to allow handling of raw json data

                                                            
def getCookie(addr):                                            # This function, using the passed through variable representing a                                             
    url = "https://" + addr + "/api/aaaLogin.json"              # management IP, retrieves the specified device Session Cookie so that
                                                                # we can access and modify this device through its API
    payload = {"aaaUser" :
              {"attributes" :                                   # username and password to access the device
                   {"name" : "cisco",
                    "pwd" : "cisco"}
               }}

    response = requests.post(url, json=payload, verify = False)             # the raw data response from the selected device

    
    return response.json()["imdata"][0]["aaaLogin"]["attributes"]["token"]  # converts the response variable into a json format, parses
                                                                            # through the converted data to get the Session Cookie and
                                                                            # returns the Session Cookie to the main script

def createVLAN(addr, cookie, vlanNum, vlanName):
    url = "https://" + addr + "/api/mo/sys.json"

    payload = {
    "topSystem": {                                                          # this function will create a VLAN on a specified switch.
    "children": [                                                           # the function takes in 4 variables, the management IP address
    {                                                                       # the session cookie, the VLAN number and the VLAN name. The
    "bdEntity": {                                                           # payload code is generated from the NEXOS-DME(REST) API.
    "children": [
    {
        "l2BD": {
            "attributes": {
                "fabEncap": "vlan-" + vlanNum,
                "name": vlanName
    }}}]}}]}}
    
    headers = {
    'Content-Type' : 'text/plain',
    'Cookie' : 'APIC-cookie=' + cookie
    }
                                                                         # verify = False to accept without a ssl certificate
    response = requests.request("POST", url, verify = False, headers=headers, data=json.dumps(payload)) 
                                                                         # sends the payload to the specified device API, which
    print(response)                                                      # will create the interface on the specified device
    print(response.json())
    
                                                                         
def defineVLAN(addr, cookie, VLAN, vlanIP):
    url = "https://" + addr + "/api/mo/sys.json"

    payload = {
    "topSystem": {                                                      # this function will add to the configuration of the specified
    "children": [                                                       # VLAN on the specified switch. the function takes in 4 
    {                                                                   # variables, the management IP address of the switch, the 
    "ipv4Entity": {                                                     # session cookie, the VLAN number and the IP address for the SVI 
        "children": [                                                   # of the VLAN. The payload code is generated from the NEXOS-DME
    {                                                                   # (REST) API.
    "ipv4Inst": {
        "children": [
    {
    "ipv4Dom": {
        "attributes": {
            "name": "default"
    },
    "children": [
    {
        "ipv4If": {
            "attributes": {
                "id": "vlan " + VLAN
        },
    "children": [
    {
    "ipv4Addr": {
        "attributes": {
            "addr": vlanIP
    }}}]}}]}}]}}]}},
    {
    "interfaceEntity": {
        "children": [
    {
        "sviIf": {
            "attributes": {
                "adminSt": "up",
                "id": "vlan " + VLAN
    }}}]}}]}}

    headers = {
    'Content-Type' : 'text/plain',
    'Cookie' : 'APIC-cookie=' + cookie
    }
                                                                         # verify = False to accept without a ssl certificate
    response = requests.request("POST", url, verify = False, headers=headers, data=json.dumps(payload)) 
                                                                         # sends the payload to the specified device API, which
    print(response)                                                      # will implement the changes to the interface configuration
    print(response.json())
    

def vlanHSRPInfo(addr, cookie, VLAN, hsrpID, hsrpIP):
    url = "https://" + addr + "/api/mo/sys.json"

    payload = {
    "topSystem": {                                                      # this function will update the VLAN interface configuration
    "children": [                                                       # with HSRP information. the function takes in 5 variables:
    {                                                                   # the management IP address, the session cookie, the VLAN number, 
    "interfaceEntity": {                                                # the HSRP group ID number and the HSRP IP address.
        "children": [                                                   # The payload code is generated from the NEXOS-DME(REST) API
    {
        "sviIf": {
            "attributes": {
                "id": "vlan " + VLAN
    }}}]}},
    {
    "hsrpEntity": {
        "children": [
    {
        "hsrpInst": {
            "children": [
    {
        "hsrpIf": {
            "attributes": {
                "id": "vlan " + VLAN
    },
        "children": [
    {
        "hsrpGroup": {
            "attributes": {
                "af": "ipv4",
                "id": hsrpID,
                "ip": hsrpIP,
                "ipObtainMode": "admin"
    }}}]}}]}}]}}]}}

    headers = {
    'Content-Type' : 'text/plain',
    'Cookie' : 'APIC-cookie=' + cookie
    }
                                                                         # verify = False to accept without a ssl certificate
    response = requests.request("POST", url, verify = False, headers=headers, data=json.dumps(payload)) 
                                                                         # sends the payload to the specified device API, which
    print(response)                                                      # will implement the changes to the interface configuration
    print(response.json())
    

def vlanOSPFInfo(addr, cookie, VLAN, ospfProcess, ospfArea):
    url = "https://" + addr + "/api/mo/sys.json"

    payload = {
    "topSystem": {
    "children": [                                                       # this function will update the VLAN interface configuration
    {                                                                   # with OSPF routing information. the function takes in 5
    "ospfEntity": {                                                     # variables: the management IP address, the session cookie,
        "children": [                                                   # the VLAN number, the OSPF process ID number and the OSPF
    {                                                                   # area number. The payload code is generated from the NEXOS-DME
        "ospfInst": {                                                   # (REST) AMI
            "attributes": {
                "name": ospfProcess
    },
        "children": [
    {
        "ospfDom": {
            "attributes": {
                "name": "default"
    },
        "children": [
    {
        "ospfIf": {
            "attributes": {
                "advertiseSecondaries": "yes",
                "area": ospfArea,
                "id": "vlan " + VLAN
    }}}]}}]}}]}}]}}

    headers = {
    'Content-Type' : 'text/plain',
    'Cookie' : 'APIC-cookie=' + cookie
    }
                                                                         # verify = False to accept without a ssl certificate
    response = requests.request("POST", url, verify = False, headers=headers, data=json.dumps(payload)) 
                                                                         # sends the payload to the specified device API, which
    print(response)                                                      # will implement the changes to the interface configuration
    print(response.json())


def incrementVlanIPAddress(starterIP):
    ipList = starterIP.split(".")                               # splits the passed through "starterIP" string into list elements by
                                                                # the "." in the IP address and creates a new variable called "ipList"

    ipList[3] = int(ipList[3])                                  # changes the fourth list element data type from a string to an integer
    ipList[3] = ipList[3]+1                                     # adds 1 to the current integer value of the fourth list element
    ipList[3] = str(ipList[3])                                  # changes the fourth list element data type from an integer to a string
    vlanIP = ""                                                 # creates an unassigned bariable called "vlanIP"

    for element in ipList:
        vlanIP = vlanIP + element + "."                         # a 'for' loop that for every element in "ipList" we are going to append
                                                                # each element to the "vlanIP" variable along with a "."
                                                                
    vlanIP = vlanIP.rstrip(".")                         # strips the "." after the last element that was entered to create a valid IP address
                                                            
    return vlanIP                                       # returns the value of the variable "vlanIP" back to the main script
    

###############################
# Start of Main Script #
###############################

device_1_IP = "10.10.20.177"                                        # This section is defining the variables that will be used down below
device_2_IP = "10.10.20.178"                                        # These variable values can be changed depending on the desired 
vlanID = "110"                                                      # configuration. The "device_1_VlanIP" and "device_2_VlanIP" variables
vlanName = "testNXOS"                                               # are blank because their values will be populated by running a function
device_1_VlanIP = ""                                                # below
device_2_VlanIP = ""
hsrpGroup = "10"
hsrpIP = "172.16.110.1"
ospfProcID = "1"
ospfArea = "0.0.0.0"

sessionCookie1 = getCookie("10.10.20.177")                          # Gets Session Cookie for NX switch. Cookie is good for 600 seconds

sessionCookie2 = getCookie("10.10.20.178")                          # Gets Session Cookie for NX switch. Cookie is good for 600 seconds


deviceDict = {
    'device_1' : {
        'cookie' : sessionCookie1,
        'mgmtIP' : device_1_IP,                                     # Creates a dictionary variable called "deviceDict". This dictionary
        'vlan_ID' : vlanID,                                         # is a nested dictionary with 2 main 'keys' (our switches) and 'values'
        'vlan_name' : vlanName,                                     # which are additional dictionaries. The 'values' in the nested
        'vlan_IP' : device_1_VlanIP,                                # dictionary are the variables that were defined above
        'hsrp_group' : hsrpGroup,
        'hsrp_IP' : hsrpIP,
        'OSPF_Proc' : ospfProcID,
        'OSPF_Area' : ospfArea
        },                                                          
    'device_2' : {
        'cookie' : sessionCookie2,
        'mgmtIP' : device_2_IP,
        'vlan_ID' : vlanID,
        'vlan_name' : vlanName,
        'vlan_IP' : device_2_VlanIP,
        'hsrp_group' : hsrpGroup,
        'hsrp_IP' : hsrpIP,
        'OSPF_Proc' : ospfProcID,
        'OSPF_Area' : ospfArea
}}

device_1_VlanIP = incrementVlanIPAddress(hsrpIP)                        # assigns an IP address to the variable by running the
                                                                        # incrementVlanIPAddress function

device_2_VlanIP = incrementVlanIPAddress(device_1_VlanIP)               # assigns an IP address to the variable by running the
                                                                        # incrementVlanIPAddress function 

deviceDict["device_1"]["vlan_IP"] = device_1_VlanIP + "/24"             # adds the 'value' to the specified dictionary 'key' by using the
                                                                        # "device_1_VlanIP" variable and appending the CIDR Address to it
                                                                        
deviceDict["device_2"]["vlan_IP"] = device_2_VlanIP + "/24"             # adds the 'value' to the specified dictionary 'key' by using the
                                                                        # "device_2_VlanIP" variable and appending the CIDR Address to it

"""
The 'for' loop below is set up so that for each device (key) in the main dictionary "deviceDict", the below functions will run.
Each function will run and use the specified nested dictionary 'value' as the passed in variables and make the desired changes
for each device in the "deviceDict" dictionary.
"""

for device in deviceDict:

    createVLAN(deviceDict[device]["mgmtIP"], deviceDict[device]["cookie"], deviceDict[device]["vlan_ID"], deviceDict[device]["vlan_name"])
    
    defineVLAN(deviceDict[device]["mgmtIP"], deviceDict[device]["cookie"], deviceDict[device]["vlan_ID"], deviceDict[device]["vlan_IP"])
    
    vlanHSRPInfo(deviceDict[device]["mgmtIP"], deviceDict[device]["cookie"], deviceDict[device]["vlan_ID"], deviceDict[device]["hsrp_group"], deviceDict[device]["hsrp_IP"])
    
    vlanOSPFInfo(deviceDict[device]["mgmtIP"], deviceDict[device]["cookie"], deviceDict[device]["vlan_ID"], deviceDict[device]["OSPF_Proc"], deviceDict[device]["OSPF_Area"])



