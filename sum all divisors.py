import math
def sum_of_divisors(n):
    result = 0
    i = 2
    while i<= (math.sqrt(n)):
        if (n % i == 0):
            if (i == (n / i)):
                result = result + i
            else :
                result = result + (i + n/i)
        i =i+1
    return (result + 1)
    
    print (sum_of_divisors(8))