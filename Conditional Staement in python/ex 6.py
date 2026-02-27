import time
t = time.strftime("%H:%M:%S")
time = int(input("Enter the time in 24 hour format: "))
if time >= 0 and time < 12 :
    print ("Good Morning sir")
elif time >= 12 and time < 18 :
    print("Good Afternoon sir")
elif time >= 18 and time <24:
    print("Good Evening sir")
    