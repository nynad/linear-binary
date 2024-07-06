# linear searching: the most basic method of searching a list.
# linear searching occurs moving linearlly through a list: you go through every index number 0 and onward, checking each 
# item in a list matching it to the requested item. 

list=[4,78,18,52,12]

req=int(input("What number are you looking for in the list?"))
found=False 

# to cycle through a list, you can use the range function with the length of the list subtracted by 1 to get accurate index numbers
for i in range(len(list)-1):
    if list[i] == req:
        print("The number you requested exists at list index number:",i)
        found=True 

if not found: 
    print("The number does not exist in this list!")

# linear's biggest flaw is that it's too slow. it's simple but not very efficient when it comes to speed.



