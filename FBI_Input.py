#float validation
#dirk grobbelaar

#Function designed to accept a integer and prevent it from crashing python======
def float_input(message_to_print):

    #subfunction for checking validity==========================================
    def int_function(string):
        valid = True
        #looping for lenght of the string
        for i in range(len(string)):
                #checking if current character falss between (0-9)
            if ord(string[i]) > 57 or ord(string[i]) < 48 and ord(string[i]) != 46:
                #setting validity to false if it doesnt meet requirements
                valid = False

        return (valid)
    #subfunction for checking validity==========================================
    integer = str(input(message_to_print))
    #using function to check if it is an integer
    valid = int_function(integer)
    #asking for input till valid is true
    while valid == False:
        integer = str(input("Invlid character were found, please try again"))
        valid = int_function(integer)

    return(float(integer))

#Function designed to accept a integer and prevent it from crashing python======
def bool_input(message_to_print):

    #subfunction for checking validity==========================================
    def bool_function(string):
        valid = True
        #checking if its "True" or "False"
        if string != "True" and string != "False":
            valid = False
        return (valid)
    #subfunction for checking validity
    integer = str(input(message_to_print))
    #using function to check if it is an integer
    valid = bool_function(integer)
    #asking for input till valid is true
    while valid == False:
        integer = str(input(message_to_print))
        valid = bool_function(integer)

    return(bool(integer))

#Function designed to accept a integer and prevent it from crashing python======
def int_input(message_to_print):

    #subfunction for checking validity==========================================
    def int_function(string):
        valid = True
        #looping for lenght of the string
        for i in range(len(string)):
                #checking if current character falss between (0-9)
            if ord(string[i]) > 57 or ord(string[i]) < 48:
                #setting validity to false if it doesnt meet requirements
                valid = False

        return (valid)
    #subfunction for checking validity
    integer = str(input(message_to_print))
    #using function to check if it is an integer
    valid = int_function(integer)
    #asking for input till valid is true
    while valid == False:
        integer = str(input("Invalid character detected, please try again\n"))
        valid = int_function(integer)

    return(int(integer))

#MAIN PROGRAM===================================================================

