string = "15"
number = 7
sum = number + int(string)
print("The sum of number and string is:", sum)
#Concatenating string and number after converting number to string
print(int(string) + number)  # Adding string and number after converting string to integer
print(float(string) + number)  # Adding string and number after converting string to float
print(bool(string))  # Converting string to boolean (non-empty string is True)              
print(bool(""))  # Converting empty string to boolean (empty string is False)
print(bool(0))  # Converting 0 to boolean (0 is False)
print(bool(1))  # Converting 1 to boolean (non-zero number is True)
print(bool(-1))  # Converting -1 to boolean (non-zero number is True
print(bool(None))  # Converting None to boolean (None is False)
print(bool([]))  # Converting empty list to boolean (empty list is False)
print(bool([1, 2, 3]))  # Converting non-empty list to