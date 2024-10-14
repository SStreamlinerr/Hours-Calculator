# Hours Calculator 2.0

def intro():
    print("This program will determine how many hours you have done and how much you should be paid. Please imput hour then minute (in 24 hour format)")

def get_details():
    shifts=int(input("How many shifts did you work?"))
    for counter in range(0,shifts):
        shiftN=counter+1
        print("Shift",shiftN)
        startH=int(input("What hour did you start shift"))
        startM=int(input("What minute you start shift"))
        endH=int(input("What hour did you finish shift"))
        endM=int(input("What minute did you finish shift")) 
    return startH,startM,endH,endM,shifts

def calc_hours(startH,startM,endH,endM,shifts):
    hours=[]
    minutes=[]
    for counter in range(0,shifts):
        hour=endH-startH
        if endM<startM:
            minute=(endM-startM)+60
            hour=hour-1
        elif endM==startM:
            minute=0
        elif endM>startM:
            minute=endM-startM
        else:
            print("The information is invalid, please restart program and try again")
        hours.append(hour)
        minutes.append(minute)
    return hours,minutes

def total_hours(hours,minutes,shifts):
    tHours=0
    tMinutes=0
    for counter in range(0,shifts):
        tHours=tHours+hours[counter]
        tMinutes=tMinutes+minutes[counter]
    min2Hr=tMinutes/60
    total=tHours+min2Hr
    return total

def display(total):
    print("You worked for",total,"hours")

#Main program
intro()
startH,startM,endH,endM,shifts=get_details()
hours,minutes=calc_hours(startH,startM,endH,endM,shifts)
total=total_hours(hours,minutes,shifts)
display(total)