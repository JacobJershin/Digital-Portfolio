#!/usr/bin/python3.9
A = []
while True: #while theres still standard input going in
    try: # it will try to add that input to the array
        A.append(input('')) #adds thge input
    except EOFError: #go until the input is done (c
        break
def q(a):
    if len(a) <= 1:
        return a
    else:
        return q([i for i in a[1:] if i < a[0]]) + [a[0]] + q([i for i in a[1:] if i >= a[0]])
print(q(A))
