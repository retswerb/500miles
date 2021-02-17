#import
from datetime import date

#get current date (curDate)
curDate = date.today()

#set target miles
annualMiles = 500

#count how many days since beginning of year (daysElapsed)
dateNewYear = date(2020, 12, 31)
testDate = date(2021, 12, 31) #use for testing if needed
daysElapsed = curDate - dateNewYear
daysGone = daysElapsed.days

#Calculate percentage (yearPercent = daysGone / 365)
yearPercent = daysGone/365

print("Today's date is", str(curDate) + ".")
print(daysGone, "days have gone by in 2021.")

#input number of miles run (milesRun)
#handle non-numbers gracefully
while True:
    try:
        milesRun = input("How many miles have you run this year? (Enter 'Miles' to change mileage goal from " + str(annualMiles) + " miles) ")
        #change goal if needed
        if milesRun == "Miles" or milesRun == "miles":
            annualMiles = input("Enter your annual mileage goal: ")
            annualMiles = float(annualMiles)
            milesRun = 0
        #back to accepting mileage input
        else:
            milesRun = float(milesRun)
            break
    except ValueError:
        print("Please enter the number of miles you've run so far.")
        continue

milesRun = round(milesRun, 2)

#calculate target (targetMiles = yearPercent * 500)
targetMiles = yearPercent*annualMiles
targetMiles = round(targetMiles, 2)

#compare milesRun to targetMiles
#print you are on target / above target / below target with amount over/under
if milesRun == targetMiles:
    print("Whoa! You're exactly on target!")
elif milesRun < targetMiles:
    milesBehind = round((targetMiles - milesRun), 2)
    print("Time to get running! You're", milesBehind, "miles behind today's target,", targetMiles, "miles.")
elif milesRun > targetMiles:
    milesAhead = round((milesRun - targetMiles), 2)
    print("Great job! You're %s miles ahead of today's target, %s miles." % (milesAhead, targetMiles))
