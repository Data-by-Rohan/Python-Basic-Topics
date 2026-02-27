#  skip negative numbers

numbers = 5 , 6 , -2 ,8 ,-3,-1
for i in numbers:
    if (i < 0):
        continue
    print(i)