
# Set are those list which contain unique element no duplicate data is allowed
s1 = {3,5,23,5,5,5}
s2 = {3,5,2}
# s1.clear() it will empty my set
s1.pop() # remove  element from my set
print(s1)

s1.add(345)
print(s1)  # add element at first

print(s1.intersection(s2))  # it will give all the common element between s1 and s2

print(s1.isdisjoint(s2))    # Return true if there is nothing in common between s1 and s2

print(s2.difference(s1))   # Return the set with removing the common element from s1

print(s1.union(s2))   # return the set with both element of s1 and s2

