while True:
    try:
        num1=float(input("Enter the first number: "))
        num2=float(input("Enter the second number: "))
        result=num1/num2
        print("Result: ", result)
        break
    except ValueError:
        print("Enter valid numbers")
        
    except ZeroDivisionError:
        print("Canot be divided by zero. Try Again")    