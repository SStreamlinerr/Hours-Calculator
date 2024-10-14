# Hours Calculator 3.0

def get_details():
    shifts=int(input("\nHow many shifts did you work? "))
    rate = float(input("What is your hourly rate? "))

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

        #initialise arrays
        hours=[]
        minutes=[]

        for n in range(shifts):
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

def display(totalHours,pay):
    print("\nYou worked for",totalHours,"hours")
    print("You have earned: £"+str(pay))


print("This program will determine how many hours you have done and how much you should be paid."
      "\nPlease input in 24 hour format, e.g: eleven thirty five is 1135")

hours,minutes,shifts,rate=get_details()

totalHours,pay=total_hours(hours,minutes,shifts,rate)

display(totalHours,pay)