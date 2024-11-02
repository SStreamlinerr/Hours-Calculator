# Hours Calculator 3.1
# Struan McKenzie

# import libraries
import FBI_Input

def get_details():
    shifts = FBI_Input.int_input("\nHow many shifts did you work? ")
    rate = FBI_Input.int_input("What is your hourly rate? ")

    #initialise arrays
    hours = []
    minutes = []

    for i in range(shifts):
        shiftN = i + 1
        print("\nShift", str(shiftN) + "/" + str(shifts))

        start = str(input("When did you start shift " + str(shiftN) + "/" + str(shifts) + "? "))
        while len(start) != 4:
            print("Invalid format, please try again\n")
            start = str(input("When did you start shift " + str(shiftN) + "/" + str(shifts) + "? "))

        end = str(input("When did you finish shift " + str(shiftN) + "/" + str(shifts) + "? "))
        while len(end) != 4:
            print("\nInvalid format, please try again")
            end = str(input("When did you finish shift " + str(shiftN) + "/" + str(shifts) + "? "))

        #extracting the hours and minutes from the times given
        startH = int(start[0:2])
        startM = int(start[2:4])
        endH = int(end[0:2])
        endM = int(end[2:4])
       
        #get length of hours worked
        hour = endH - startH
        
        #get length of minutes worked
        if endM < startM:
            minute = (endM - startM) + 60
            hour -= 1

        elif endM == startM:
            minute = 0

        elif endM > startM:
            minute = endM - startM

        else:
            print("\nThe information is invalid, press enter to restart")
            hours, minutes, shifts, rate = get_details()

        hours.append(hour)
        minutes.append(minute)
    
    return hours, minutes, shifts, rate

# to print hours to screen
def total_hours(hours, minutes, shifts, rate):

    # prompt for type of output
    print("\nView total hours ······················ press 1"
          "\nView hours for each shift seperately ·· press 2")
    
    choice = FBI_Input.int_input("")
    while choice != 1 and choice != 2:
        print("Invalid option, try again")
        choice = FBI_Input.int_input("")

    # print total hours to screen
    if choice == 1:
        totalHours, pay = calculate_hours_pay(shifts, hours, minutes)

        print("\nYou worked for", totalHours, "hours")
        print("You have earned: £" + str(pay) + "\n")

        # call subprogram to calculate savings
        saving = savings(pay)
        print("You should put £" + str(saving), "into your savings")

        # prints total hours to file
        print("\nPrint hours to file ····· press 1"
              "\nExit program ············ press 2")
    
        choice = FBI_Input.int_input("")
        while choice != 1 and choice != 2:
            print("Invalid option, try again")
            choice = FBI_Input.int_input("")

        # print to file
        if choice == 1:
            #get location of file
            #file_location = input("\nFull path of hours file? ")
            file_location = "/home/struan-mckenzie/Desktop/Hours.txt"

            month = input("\nWhich month/months were these shifts completed during? ")

            with open(file_location, "a+") as writefile:
                line = month + ":\nHours: " + str(totalHours) + "\nPay: " + "£" + str(pay)
                writefile.write("\n\n" + line)
            writefile.close
            input("Written to file. Press enter to exit")
            exit()
        
        else:
            exit()


    # print seperate hours to screen
    else:
        for i in range(shifts):
            print("\nShift", str(i + 1) + "/" + str(shifts) + ":")
            print("You worked for", hours[i], "hours and", minutes[i], "minutes")

        totalHours, pay = calculate_hours_pay(shifts, hours, minutes)
        print("You earned: £" + str(pay) + "\n")
        
        saving = savings(pay)
        print("You should put £" + str(saving), "into your savings")

        # print seperate hours to file
        print("\nPrint hours to file ····· press 1"
              "\nExit program ············ press 2")
    
        choice = FBI_Input.int_input("")
        while choice != 1 and choice != 2:
            print("Invalid option, try again\n")
            choice = FBI_Input.int_input("")
        
        # print to file
        if choice == 1:
            #file_location = input("\nFull path of hours file? ")
            file_location = "/home/struan-mckenzie/Desktop/Hours.txt"
            month = input("\nWhich month/months were these shifts completed during? ")

            with open(file_location,"a+") as writefile:
                writefile.write("\n\n" + month + ":\n")
                for i in range(len(hours)):
                    line = str("Shift " + str(i + 1) + "/" + str(shifts) + ": You "
                               "worked " + str(hours[i]) + " hours and " + str(minutes[i]) + " minutes\n")
                    writefile.write(line)
                writefile.write("Pay: £" + str(pay))
            writefile.close
            input("Written to file. Press enter to exit")
            exit()

        else:
            exit()

def calculate_hours_pay(shifts, hours, minutes):
    #set total time to 0
    tHours = 0
    tMinutes = 0

    #calculate total
    for i in range(shifts):
        tHours = tHours + hours[i]
        tMinutes = tMinutes + minutes[i]

    min2Hr = tMinutes / 60
    totalHours = tHours + min2Hr
    pay = totalHours * rate

    return totalHours, pay

# calculate savings
def savings(pay):
    perc = FBI_Input.float_input("What percent (e.g: 0.5) of your pay do you want to save? ")
    saving = pay * perc
    return saving


# initiation
print("This program will determine how many hours you have done and how much you should be paid."
      "\nPlease input in 24 hour format, e.g: eleven thirty five is 1135")

hours, minutes, shifts, rate = get_details()

totalHours, pay = total_hours(hours, minutes, shifts, rate) 