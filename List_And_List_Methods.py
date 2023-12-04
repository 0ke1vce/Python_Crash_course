
# List in python is a collection of different objects like string, int, float and even a list.
# List can be made by --> list_name=[element1, element2, element3]
l1 = [3,5,34,43,"harry"]
print(l1)

# List is mutable once created we can change the data of our list anytime (Modification is very easy).
l1.remove("harry")
print(l1)

# l1.clear() # it will clear our list i.e--> empty our list

l1.sort()  # sort our list in ascending order

l1.pop()  # remove last element from our list

l1.reverse()  # it will reverse our list

l1.extend([34,54,23])  # it will extend our list with another list or element

l1.append(12)  # add 12 at last location.

