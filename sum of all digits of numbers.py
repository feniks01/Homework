def sum_of_digits(num):
    result = 0

    for i in range(0,3):
        result += num % 10
        num = num // 10


    return(result)

print(sum_of_digits(235))
print (sum_of_digits(1325132435356))
print(sum_of_digits(123))
print(sum_of_digits(6))
print( sum_of_digits(-10))