# binary searching needs a sorted list. it splits the search down into 2 seperate pieces.
# binary will find the first index number (always 0) and the last index number and find the middle index in between them.
# if the value of the middle index number isn't equal to the requested number, everything either greater/lesser in the list is disregarded.
# if the middle index value is lesser, the middle index becomes starting index.
# if the middle index value is greater, the middle index becomes the ending index.
# if the value at the middle index is equal to requested number, the process can end.

list=[1,2,4,5,7,9]

req=int(input("Enter the number you want to find:"))

def binary(list,req):
    low=0
    high=(len(list)-1)

    # the conditioning lets the searching loop repeat until low is either lesser than or equal to high:
    # meaning middle index has been found between the two
    while low<=high:
        mid=((low+high)//2)
        if list[mid] == req:
            return mid 
        elif list[mid]<req:
            low=mid+1 
        else: 
            high=mid-1 
    return -1

result=binary(list,req)

if result>-1:
    print("The number is at index:",result)
else:
    print("The number is not in the list.")



