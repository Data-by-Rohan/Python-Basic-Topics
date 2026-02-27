#  small fun project using break statement password checker

correct_pass="Rohan@2003"
while True:
    Password = input("Enter Correct Passwored :-")
    if Password==correct_pass:
        print("Access Granted !")
    else:
        print("Please Try again  !")