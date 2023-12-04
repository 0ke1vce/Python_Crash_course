s="Goku"

# Writing to a file
with open("text.txt","w") as f:
    f.write(s)


# Reading into file
with open("ujjwal.txt","r") as r:
    # s=r.readline()  # read only a line
    # print(s)
    # q=r.read()   # read full file
    # print(q)
    t=r.readlines()  # give a list of lines
    print(t)

# Appending in file
with open("ujjwal.txt","a") as uj:
    uj.write("orewa kami sama\n")