
# function are block of code which do a specific task
# it improves readability and performance of our code and avoid repetition of code.
def greetHello(name):    # Parameters of our function
    print("hello "+name)

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact    # it means this function is returning a value so at time of calling this function.
# We have to store the value to a variable to access it.

def avg(n1,n2):
    print(f"Average of {n1} and {n2} is ",(n1+n2)/2)
if __name__ == '__main__':
    greetHello("ujjwal")  # Calling our function by giving them arguments.

    Factorial=factorial(5)   # At time of calling we store the value of return number in variable Factorial.
    print(Factorial)

    avg(23,65)
