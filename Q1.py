print("\n                  PROGRAM FOR PRINTING STUDENT'S PERCENTAGE           \n")

#CREATING A DICTIONARY(EMPTY)
D = {}

n = int(input('How many student record you want to store?? \n'))

#CREATING A LIST TO ADD IN IT
ls = []


for i in range(0, n):

    x = int(input("Enter Roll no: "))
    y = str(input("Enter Student's Name: "))
    z = int(input("Enter Percentage Of The Student: \n"))



    ls.append((x, y, z))

#SORTING
ls = sorted(ls, reverse=True)

print("\n Sorted List Is: \n")

print("Rollno \t\t\t   Name   \t\t\t %\n")

for i in ls:
    # print name and marks stored in
    # second and first position
    # respectively in list of tuples.
    print(i[0], "\t\t\t", i[1], "\t\t\t", i[2],"%")
