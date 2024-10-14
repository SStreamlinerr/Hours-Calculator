# Hours Calculator 3.0

def get_details():
    shifts=int(input("\nHow many shifts did you work? "))
    rate = float(input("What is your hourly rate? "))

    #initialise arrays
    hours=[]
    minutes=[]

    for i in range(shifts):
        shiftN = i+1
        print("\nShift", str(shiftN) + "/" + str(shifts))
        start = str(input("When did you start shift " + str(shiftN) + "/" + str(shifts) + "? "))
        while len(start) != 4:
            print("\nInvalid format, please try again")
            start = str(input("When did you start shift " + str(shiftN) + "/" + str(shifts) + "? "))

        end  = str(input("When did you finish shift " + str(shiftN) + "/" + str(shifts) + "? "))
        while len(end) != 4:
            print("\nInvalid format, please try again")
            end  = str(input("When did you finish shift " + str(shiftN) + "/" + str(shifts) + "? "))

        #extracting the hours and minutes from the times given
        startH = int(start[0:2])
        startM = int(start[2:4])
        endH = int(end[0:2])
        endM = int(end[2:4])

       
        #get length of hours worked
        hour = endH-startH
        #get length of minutes worked
        if endM < startM:
            minute = (endM-startM)+60
            hour = hour-1
        elif endM == startM:
            minute = 0
        elif endM > startM:
            minute = endM-startM
        else:
            print("\nThe information is invalid, press enter to restart")
            hours,minutes,shifts,rate=get_details()
        hours.append(hour)
        minutes.append(minute)
    
    return hours,minutes,shifts,rate

def total_hours(hours,minutes,shifts,rate):

    print("\nView total hours ······················ press 1"
          "\nView hours for each shift seperately ·· press 2")
    
    choice = int(input())
    while choice != 1 and choice != 2:
        print("Invalid option, try again")
        choice = int(input())

    if choice == 1:
        totalHours,pay = calculate_hours_pay(shifts,hours,minutes)

        print("\nYou worked for",totalHours,"hours")
        print("You have earned: £"+str(pay))

        print("\nPrint hours to file ····· press 1"
              "\nExit program ············ press 2")
    
        choice = int(input())
        while choice != 1 and choice != 2:
            print("Invalid option, try again")
            choice = int(input())

        if choice == 1:
            #get location of file
            file_location = input("\nFull path of hours file? ")

            month = input("\nWhich month/months were these shifts completed during? ")

            with open(file_location,"a+") as writefile:
                line = month + ":\nHours: " + str(totalHours) + "\nPay: " + "£"+str(pay)
                writefile.write("\n\n" + line)
            writefile.close
            input("Written to file. Press enter to exit")
            exit()

        else:
            exit()

    elif choice == 2:
        for i in range(shifts):
            print("\nShift",str(i+1)+"/"+str(shifts),":")
            print("You worked for",hours[i],"hours and",minutes[i],"minutes")

        totalHours,pay = calculate_hours_pay(shifts,hours,minutes)
        print("You earned: £"+str(pay))

        print("\nPrint hours to file ····· press 1"
              "\nExit program ············ press 2")
    
        choice = int(input())
        while choice != 1 and choice != 2:
            print("Invalid option, try again")
            choice = int(input())

        if choice == 1:
            file_location = input("\nFull path of hours file? ")
            month = input("\nWhich month/months were these shifts completed during? ")

            with open(file_location,"a+") as writefile:
                writefile.write("\n\n" + month + ":\n")
                for i in range(len(hours)):
                    line = str("Shift " + str(i+1) + "/" + str(shifts) + ": You worked " + str(hours[i]) + " hours\n")
                    writefile.write(line)
                writefile.write("Pay: £" + str(pay))
            writefile.close
            input("Written to file. Press enter to exit")
            exit()
        else:
            exit()

def calculate_hours_pay(shifts,hours,minutes):
    #set total time to 0
    tHours=0
    tMinutes=0

    #calculate total
    for i in range(shifts):
        tHours = tHours+hours[i]
        tMinutes = tMinutes+minutes[i]
    min2Hr = tMinutes/60
    totalHours = tHours+min2Hr
    pay = totalHours*rate
    return totalHours,pay
    




print("This program will determine how many hours you have done and how much you should be paid."
      "\nPlease input in 24 hour format, e.g: eleven thirty five is 1135")

hours,minutes,shifts,rate=get_details()

totalHours,pay=total_hours(hours,minutes,shifts,rate)