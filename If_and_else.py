age = int(input("Enter your age\n"))

"""
if(age>18 and age<75):
    print("you can drive")
elif(age==18):
    print("you have to do a driving test")
else:
    print("you can't drive")

print("End of program")
"""

# Match Case in Python--> similar to switch case
match age:
    case 1:
        print("Age is 1")
    case 2:
        print("Age is 2")
    case _:     # Just like default case
        print("Default case ")