def reverse(n):
    rev = 0
    while (n != 0):
        rev = (rev * 10) + (n % 10)
        n //= 10
    return rev

def getSum(n):
 
    n = reverse(n)
    sumOdd = 0
    sumEven = 0
    c = 1
 
    while (n != 0):
 
        if (c % 2 == 0):
            sumEven += n % 10
        else:
            sumOdd += n % 10
        n //= 10
        c += 1
 
    print("Sum odd =", sumOdd)
    print("Sum even =", sumEven)
 
n=int(input("enter number: "))
getSum(n)