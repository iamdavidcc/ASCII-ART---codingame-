import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())    # anchura de la letra
h = int(input())    # altura de la letra
t = input()         # Letra a pintar

# Diccionary with possible values:
dicc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'         # for capital letters
dicc1 = 'abcdefghijklmnopqrstuvwxyz'        # for small letters

for i in range(h):
    ans = ""    # empty 'string' to store the answer 
    row = input()
    for letter in t:
        n1 = dicc.find(letter)      # is it a capital letter?
        n2 = dicc1.find(letter)     # is it a small letter?
        if n1>=0:     # cappital letters
            pp = row[(n1)*l:((n1)*l)+l]   # which letter
            ans = ans+pp  # answer
        elif n2>=0:   # small letter
            pp = row[(n2)*l:((n2)*l)+l]   # which letter
            ans = ans+pp    # answer
        else:         # when is not a letter
            pp = row[len(row)-l:len(row)]   # print a '?'
            ans = ans+pp    # anser
    print(ans)
