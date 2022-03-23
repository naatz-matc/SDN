# This will create a dictionary named 'router1' with the specified "key": "value" pairs

router1 = {"Host" : "R1", "Brand" : "Cisco", "Model" : "1941", "MgmtIP" : "10.0.0.1",
           "G0/0" : "10.0.1.1 /24", "G0/1" : "10.0.2.1 /24", "G0/2" : "10.0.3.1 /24"}

"""
                SCREENSHOT #1 CODE:
                
The following lines of code are to output the values that the lab
assignment is asking for. They will be commented out when they are
not needed
"""

#print(router1.keys())
#print()
#print(router1.values())
#print()
#print(router1.items())

"""
                SCREENSHOT #2 CODE:
                
This next part will change the IP Address of the G0/2 interface
to 10.1.3.1/24 as well as change the model from 1941 to 2901 WITHOUT
recreating the dictionary. Then we will use a print statement to show
the changes. The print lines can be commented out when not needed.
"""

#router1["Model"] = "2901"
#router1["G0/2"] = "10.1.3.1 /24"

#print(router1.keys())
#print()
#print(router1.values())
#print()
#print(router1.items())

"""
                SCREENSHOT #3 CODE:
                
Here we are going to create a 'for' loop that will cycle through our
entire dictionary and display an output that is similar to the output
in the lab assignment. The following code can be commented out when
not needed.
"""

#for key in router1:
#    print("Key = " + key + "        " + "Value = " + router1[key])

"""
                SCREENSHOT #4 CODE:
                
This next part we will format the output to look more like we are in
the command line of a Cisco router. All of the IP CIDRs will be removed
and the output will be similar to what is in the lab document. The following
code can be commented out when not needed.
"""

for key in router1:
    if len(router1[key]) >=8:
        print(key, end = "\t\t")
    else:
        print(key, end = "\t")
print("\n")   
print("-" * 147)

for key in router1:
    print(router1[key].replace("/24", ""), end = "\t")
print("\n")

"""
This final part of the script defines a function that will prompt the user
to enter an IP address for the management interface. A while loop with a series
of if/elif/else statments inside the function will verify if the user entered
value is a valid IP address. If so the value will be placed in the router1
dictionary and be the new value to the "mgmtIP" key. After the function is defined
a while loop starts that will ask the user if they would like to change the
management IP. If "n" is selected the while loop will break and the script will end.
If "y" is selected the function will launch and will run until a valid IP address
is entered, which will end the function and exit the while loop and print the
success message at the end.
"""

def validateIP():
    badIP = True
    while badIP == True:
        badIP = False
        ipString = input("Enter an IP address for the management interace: ")
        ipList = ipString.split(".")

        if len(ipList) !=4:
            print("IP address must be in the following format: x.x.x.y where x>= 0 and x <= 255 and y cannot be 0")
            badIP = True

        else:
            ipNumCheck = ipString.replace(".","",4)
            
            if ipNumCheck.isnumeric() == False:
                print("IP address must be in the following format: x.x.x.y where x>= 0 and x <= 255 and y cannot be 0")
                badIP = True

            else:
                ipInteger = ([int(x) for x in ipList])
                ipRange = range(256)
    
                if ipInteger[0] not in ipRange:
                    print("IP address must be in the following format: x.x.x.y where x>= 0 and x <= 255 and y cannot be 0")
                    badIP = True
                
                elif ipInteger[1] not in ipRange:
                    print("IP address must be in the following format: x.x.x.y where x>= 0 and x <= 255 and y cannot be 0")
                    badIP = True

                elif ipInteger[2] not in ipRange:
                    print("IP address must be in the following format: x.x.x.y where x>= 0 and x <= 255 and y cannot be 0")
                    badIP = True

                elif ipInteger[3] not in ipRange or ipInteger[3] ==0:
                    print("IP address must be in the following format: x.x.x.y where x>= 0 and x <= 255 and y cannot be 0")
                    badIP = True
                
                else:
                    router1["MgmtIP"] = ipString        
            
validIP = False                
while validIP == False:
    validIP = True
    answer = input("Do you want to change the Management IP address (y or n)? ")
    
    if answer == "n":
        print("Nothing changed!")
        validIP = False
        break
    
    elif answer == "y":
        validateIP()
                      
if validIP == True:
    print("Address Updated!")
    print("\n")
    for key in router1:
        if len(router1[key]) >=8:
            print(key, end = "\t\t")
        else:
            print(key, end = "\t")
    print("\n")
    print("-" * 147)
    for key in router1:
        print(router1[key].replace("/24", ""), end = "\t")
        
                














