class Calculator:
    def add(self, a, b=0, c=0):
        return a+b+c
    
calc=Calculator()
print("Add 2 numbers:", calc.add(10,5))    
print("Add 3 numbers:", calc.add(10,5,6))    
print("Add 1 number:", calc.add(10))    