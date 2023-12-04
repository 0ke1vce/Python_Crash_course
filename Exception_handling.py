
# Try and except statement are used to handle exception in python

try:
    a=int(input("Enter your number : "))
    print(a+3)
except:
    print("Exception occured..")

try:
    x=10
    y=0
    print(x/y)
except Exception as E:    # to get our exception we can write as except Exception as Var_name
    print(E)