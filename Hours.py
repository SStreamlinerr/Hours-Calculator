def intro():
    print("This program will determine how many hours you have done and how much you should be paid. Please imput hour then minute (in 24 hour format)")

def get_details():
    hrlyRate=float(input("What is your hourly rate?"))
    startH=int(input("What hour did you start your shift?"))
    startM=int(input("What minute you start your shift?"))
    endH=int(input("What hour did you finish your shift?"))
    endM=int(input("What minute did you finish your shift?"))
    return startH,startM,endH,endM,hrlyRate

def calc_hours(startH,startM,endH,endM):
    hour=endH-startH
    if endM<startM:
        minute=(endM-startM)+60
        minToHr=minute/60
        hour=hour-1
    elif endM==startM:
        minute=0
        minToHr=0
    elif endM>startM:
        minute=endM-startM
        minToHr=minute/60
    else:
        print("The information is invalid, please restart program and try again")
    return hour,minute,minToHr

def calc_pay(hour,minToHr,hrlyRate):
    totalHr=hour+minToHr
    pay=round(totalHr*hrlyRate,2)
    return pay

def display(pay,minute,hour):
    with open("Hours.txt", "a") as f:
        print("You worked for", hour,"hours and", minute,"minutes", file=f)
        print("You should be paid", pay, "pounds", file=f)

#Main program
intro()
startH,startM,endH,endM,hrlyRate=get_details()
hour,minute,minToHr=calc_hours(startH,startM,endH,endM)
pay=calc_pay(hour,minToHr,hrlyRate)
display(pay,minute,hour)