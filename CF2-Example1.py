'''Example 1, adapted from python-guide.org.

Assume these are the instructions from the professor:
Without using built-in min & max functions, find lowest value of the first list,
and find the greatest value of the second list. If one value is odd
and the other is even, print "These values have different parities"

Below is the student's code:
'''

list = [1, 2, 4, 6, 8, 2, 3]
List = [5, 7, 10, 1, 4]

temp = None
for index in range(len(list)):
    if index == 0:
        temp = list[0]
    else:
        if list[index] < temp:
            temp = list[index]



temp2 = None
for index in range(len(List)):
    if index == 0:
        temp2 = List[0]
    else:
        if List[index] > temp2:
            temp2 = List[index]

print(temp); print(temp2)
if (temp//2 == temp/2 and temp2//2 != temp2/2) or (temp//2 != temp/2 and temp2//2 == temp2/2):
    print("These values have different parities")
