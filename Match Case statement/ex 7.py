#  matching list 

data = [1,2]
match data:
    case [x,y]:
        print(f"list with two elements {x} and {y}")
    case _:
        print("something else")

    # second example

point = [0,5,10]
match point:
    case [0,y,z]:
        print(f"satrt with 0 ,other values {y} and {z}")
    case _:
        print("something else")