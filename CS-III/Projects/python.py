#!/usr/bin/python3.8
import js2py
import sys

Array = []
out = ""

while True: #while theres still standard input going in
    try: # it will try to add that input to the array
        Array.append(input('')) #adds thge input 
    except EOFError: #go until the input is done (crlt D)
        break #ends 


#Array = ["case","farse","abba","aabb","a","fartstat"]

def sort(Array):
    for i in range(1, len(Array)):
        j = i-1
        while (Array[j] > Array[i]) and (j >= 0):
            Array[j+1] = Array[j]
            j=j-1
        
            

js = '''
function sort(Array) { 
for (let i = 0; i < Array.length; i++) {
for (let compare = 0; compare < Array.length; compare++) {
if (Array[i] < Array[compare]) {
Temp = Array[i]
Array[i] = Array[compare]
Array[compare] = Temp
}
}
}
return (Array)
}
'''
res = js2py.eval_js(js)

print(res(Array))
