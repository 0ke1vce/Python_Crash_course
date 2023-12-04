# Dictionary are the collection of key:value pair in python
dic1 = {"good": "Something pleasent", "Fetch": "To bring", 1: "number 1"}
print(dic1)

marks = {
    "Naina": 100, "harry": 21, "harshit": 64
}
print(marks)
marks["Shivam"] = 32
print(marks)

print(marks.get("Shivam"))  # it will give corresponding value of the key.
# if the key not present in dictionary it will give NONE.

# marks.clear()  --> empties our dictionary

print(marks.items())  # give a tuple of all key value

print(marks.keys())  # it will give list of all keys

print(marks.values())  # it will give list of all values

# Dictionary are mutable we can modify data in dictionary.
