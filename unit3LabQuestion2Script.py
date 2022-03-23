# This function is designed to take user input
# and prints out a formatted display to the screen

def printServers(servList):
    print("Server Name" + "\t\t" + "Address") # prints the content to the screen
    print("-" * 40)                           # prints the content to the screen
    for key in servList:
        print(key + "\t\t\t" + servList[key]) # this 'for' statement states that for every 'key' in the
                                              # user inputted dictionary to print a formatted list of
                                              # the dictionary {"key" : "value"} pairs to the screen
# main script starts here
# existing dictionary defined
ntpServer = {
    "Server1" : "221.100.250.75",
    "Server2" : "201.0.113.22",
    "Server3" : "58.23.191.6"
    }

# this line calls the 'printServers()' function with the user input of the 'ntpServer' dictionary
printServers(ntpServer) 
