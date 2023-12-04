name = "harry"
print(name)

print(name[0:3])  # it will print from indexing 0 to (n-1) character here that is 2
# above line of code will give Har
print(name[1:4])

x = name
x.capitalize()  # it will capitalise my string
print(x)

print(x.count("r"))  # it will give 2 as there are 2 r in my string

print(x.endswith("ry"))  # it will return true because my string ends with ry. if not returns false.

print(x.find("r"))  # Return the lowest index in the string where substring sub is found if not found returns -1

print(x.index("y"))  # return the index of the substring

print(x.isalpha())  # Return True if all characters in the string are alphabetic and there is at least one character,
# False otherwise

print(x.isdigit())  # Return True if all characters in the string are digits and there is at least one character,
# False otherwise.

x.lower()  # change my string to lower case
x.upper()  # change my string to upper case

print(x.isupper())  # Return True if String is uppercase
print(x.islower())  # Return True if String is lowercase

print(x.isspace())  # Return True if there are only whitespace characters in the string and there is at least one
# character, False otherwise.

a = "Code with "
print(a.join(x))  # Join a string with every character of our string.

x.replace("r", "p")  # Return a copy of the string with all occurrences of substring old replaced by new.

x.title()   # Return a title cased version of the string where words start with
# an uppercase character and the remaining characters are lowercase.

print(len(x))   # return length of string

age = 18
print(f"Hello this is me and i am {age} year old")

