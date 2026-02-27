# check prime number

def is_prime(n):
    if n < 2:
        return "Not Prime"
    for i in range (2,n):
        if n % 2 == 0:
            return "Not prime"
    return "Prime"
print (is_prime(8))
