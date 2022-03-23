# This function is designed to take user input
# and prints out a formatted display to the screen

def printServers(servList):
    print("Server Name" + "\t\t" + "Address") # prints the content to the screen
    print("-" * 40)                           # prints the content to the screen
    for key in servList:
        print(key + "\t\t\t" + servList[key]) # this 'for' statement states that for every 'key' in the
                                              # user inputted dictionary to print a formatted list of
                                              # the dictionary {"key" : "value"} pairs to the screen
                                              
# This function is designed to take user input
# and prints out a formatted display to the screen

def pingPrep(ipList):
    prelimList = list(ipList.values())  # this makes a list out of the 'values' of the inputted dictionary
                                        # and creates a list-type variable named 'prelimList'
                                        
    pingList = ["ping {}".format(ip) for ip in prelimList] # this code block creates a new list called 'pingList', where each list element
    for element in pingList:                               # is filled with the string "ping {}". The "{}" is a placeholder for the values
        print(element)                                     # in the list 'prelimList' iterated through with the one-liner 'for' loop. Then
                                                           # finishes by printing out each element in the list 'pingList'
# main script starts here
# existing dictionary defined        
ntpServer = {
    "Server1" : "221.100.250.75",
    "Server2" : "201.0.113.22",
    "Server3" : "58.23.191.6"
    }

# this line calls the 'printServers()' function with the user input of the 'ntpServer' dictionary
printServers(ntpServer)

print("\n") # prints a blank line to the screen

pingPrep(ntpServer)
