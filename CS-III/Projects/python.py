#!/usr/bin/python3.8
import js2py

#Array = [input()] #last step is to make the array the inp

Array = ["case","farse","abba","aabb","a","fartstat"]

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
