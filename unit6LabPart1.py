#########################
# Start of Main Script
#########################

devicesDict = {                 #this variable is defining a nested dictionary consisting of two devices as the 'keys'
    "device1" : {               #and dictionaries full of specific device information as the corresponding 'values'
        
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

print("Host" + "\t\t" + "Type" + "\t" + "Mgmt IP")          #print statements that create column headers for the
print("-"*10 + "\t" + "-"*6 + "\t" + "-"*12)                #displayed info in a friendly human readable format

for key in devicesDict:
    print(devicesDict[key]["hostname"] + "\t" + devicesDict[key]["deviceType"] + "\t" + devicesDict[key]["mgmtIP"])

    #this 'for' loop is set up so that for each MAIN 'key' in the dictionary "devicesDict"
    #it will print to the screen the NESTED dictionary 'values' for each specified
    #NESTED dictionary 'key' in a friendly human readable format
