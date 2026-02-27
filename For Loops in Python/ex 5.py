#  print multiplication table using for loop

table = int(input("Enter Table Number: "))
for i in range(1,11):
    print(f"{table} x{i}  =", table*i)