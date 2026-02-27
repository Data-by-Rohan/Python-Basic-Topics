#  match with condition statement

number = 15
match number:
    case n if n>=10:
        print("number is greater than 10")
    case _:
        print("number is less then 10")