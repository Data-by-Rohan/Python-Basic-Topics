#  print factorial number using for loop with if else

num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("factorial not work with negative numbers ")
else:
    for i in range(1,num+1):
        factorial=factorial*i
        print("factorial of", i, "is", factorial)