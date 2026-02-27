#  match case statement day program


day = int(input("enter the day number : "))
match day:
    case 1:
        print("sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case _ :
        print("Invalid day")
    