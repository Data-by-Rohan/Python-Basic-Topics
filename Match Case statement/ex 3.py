# Multiple values in one case


day = 7
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("weekday")
    case 6 | 7:
        print("weekend")
    case _:
        print("Invalid day")