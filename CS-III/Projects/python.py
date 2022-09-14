#!/usr/bin/python3.8
Array = []

while True: #while theres still standard input going in
    try: # it will try to add that input to the array
        Array.append(input('')) #adds thge input 
    except EOFError: #go until the input is done (crlt D)
        break #ends 

Temp = []
while Array:
    smallest = min(Array) #finds the "smallest" word
    Temp.append(smallest) #puts it in the temp array
    Array.pop(Array.index(smallest)) #goes to the next index in the original array

print(Temp)
    
