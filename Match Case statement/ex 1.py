x = 4
#  x is the variable to match 
match x:            # if x is 0
    case 0:
        print("x is zero")               #  case with if condition 
    case 4 if x % 2 == 0:
        print("x is 4 and even")
    case _ if x % 2 == 0:
        print("x is even but not 4")
    case _:
        print("print x")