import numbers
from tkinter import N


def nan_expand(num):
    a=""
    for i in range(num):
        a += "not a " 
    if num !=0: 
        a+= "NAN"
    return 0

print (nan_expand(0))
print (nan_expand(1))
print (nan_expand(2))
print (nan_expand(3))

