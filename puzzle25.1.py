#!/usr/bin/python3

import numpy as np

testnum = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 2022, 12345, 314159265 ]

digits = { "=":-2,"-":-1,"0":0,"1":1,"2":2 }
rdigits = { 0:"=",1:"-",2:"0",3:"1",4:"2" }

numbers = []
numsum = 0

def snafu_to_dec(num):
    chars = list(num)
    result = 0
    value = 1
    while len(chars) > 0:
        current = chars.pop()
        result += digits[current] * value
        value *= 5
    return(result)

def dec_to_snafu(num):
    result = []
    while num > 0:
       num = num+2
       remainder = num % 5
       num = num // 5
       result.insert(0,rdigits[remainder])
    return("".join(result))

#with open("input25.tiny") as file:
with open("input25") as file:
    for line in file:
        numbers.append(snafu_to_dec(line.strip()))

for n in numbers:
    print(n)
    numsum += n

print("sum: ",numsum)
print(dec_to_snafu(numsum))
