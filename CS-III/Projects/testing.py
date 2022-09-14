#!/usr/bin/python3.8
import sys

Array = []

while True: #while theres still standard input going in
    try: # it will try to add that input to the array
        Array.append(input('')) #adds thge input 
    except EOFError: #go until the input is done (crlt D)
        break #ends 

Array.sort()
print(Array)
