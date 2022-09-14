#!/usr/bin/python3.8
import js2py
import sys

Array = []

while True: #while theres still standard input going in
    try: # it will try to add that input to the array
        Array.append(input('')) #adds thge input 
    except EOFError: #go until the input is done (crlt D)
        break #ends 


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
