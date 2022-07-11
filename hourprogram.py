currentHour = int(input("Enter the current hour: "))
hoursToAdd = int(input("Enter the number of hours to add: "))
remainder = hoursToAdd%24
finalTime=currentHour+remainder
if finalTime>12:
    x=(12-currentHour)
    k=remainder-x
    print(k)
else:
    print(finalTime)
