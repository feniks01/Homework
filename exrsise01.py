class Bill:
    def __init__(self,amount):
        self.amount = amount
        if amount < 0:
            raise ValueError
        if not isinstance(amount,int):
            raise TypeError
    
    def __str__(self):
        my_str = "Amount " + str(self.amount) + " $ bill"
        return my_str
    
    def __repr__(self) -> str:
        my_str = "Amount " + str(self.amount) + "$ bill"
        return my_str
    
    def __int__ (self):
        return int(self.amount)
        
    
    def __eq__(self, bill) -> bool:
        return self.amount == bill.amount
    
    def __hash__(self) -> int:
        return hash(self.amount)

       
a = Bill(10)
b = Bill(5)
c = Bill(10)

print (a)
print (int(a))
print (b)


