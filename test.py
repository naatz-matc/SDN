
maskList = ['255','254', '252', '248', '240', '224', '192', '128', '0']

netmask = input("Please enter a subnet mask: ")

validNetmask = False                                                         # This variable is initially set to the boolean value
                                                                             # 'False'
userMaskList = netmask.split(".")
if len(userMaskList) !=4:
    return validNetmask
elif userMaskList[0] not in maskList:                                        # These series of 'if' and 'elif' statements check to
    return validNetmask                                                      # see if each list element in the list variable 
elif userMaskList[1] not in maskList:                                        # "userMaskList" is in the other list variable "maskList"
    return validNetmask                                                      # If not, the variable "validNetmask" is returned to the
elif userMaskList[2] not in maskList:                                        # main script.
    return validNetmask
elif userMaskList[3] not in maskList:
    return validNetmask
else:
    if userMaskList[0] == '255':                                             # Checks to see if the first element in "userMaskList" is
        if userMaskList[1] == '255' and userMaskList[2] == '255':            # equal to '255', if so we then check to see if the next
            if userMaskList[3] != '255':                                     # two list elements are also '255'. Finally if so we check
                validNetmask = True                                          # to see if the last list element is not '255'. If yes we
                return validNetmask                                          # change "validNetmask" to 'True' and return it to the main
            else:                                                            # script, if no we return "validNetmask" to the main script.
                return validNetmask                                             
        elif userMaskList[1] < '255':                                        # Checks to see if the second element in "userMaskList" is 
            if userMaskList[2] == '0' and userMaskList[3] == '0':            # less than '255'. If so we then check to see if the third and
                validNetmask = True                                          # fourth elements are BOTH equal to '0'. If they are we change
                return validNetmask                                          # the value of "validNetmask" to 'True' and return it to the 
            else:                                                            # main script. If the second element is NOT less than '255', we
                return validNetmask                                          # return the unchanged variable "validNetmask" to the main script.
            
        elif userMaskList[2] < '255':               # Checks to see if the third element in "userMaskList" is less than '255'. If so we then
            if userMaskList[3] == '0':              # check to see if the fourth element is equal to '0'. If so we change the value of
                validNetmask = True                 # "validNetmask" to 'True' and return it to the main script. If the third element is NOT
                return validNetmask                 # equal to '0', we return the unchanged variable "validNetmask" to the main script.
            else:
                return validNetmask
    elif userMaskList[0] != '255':
        if userMaskList[1] == '0' and userMaskList[2] == '0' and userMaskList[3] == '0':
            validNetmask = True                     
            return validNetmask                 # This is the part of the function that gets executed if the first element in "userMaskList"
        else:                                   # is NOT equal to '255'. If all of the remaining elements in "userMaskList" equal '0', then
            return validNetmask                 # we change the value of "validNetmask" to 'True' and return it to the main script. If any of
                                                # the remaining elements in "userMaskList" are NOT equal to '0', then we return the value of
                                                # "validNetmask" to the main script.
