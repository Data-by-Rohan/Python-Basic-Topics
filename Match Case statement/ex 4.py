#  case with matching string

command = input("Enter a command: ")
match command:
    case "start":
        print("system is starting...")
    case "stop":
        print("system is stopping..")
    case _:
        print("unknown command")