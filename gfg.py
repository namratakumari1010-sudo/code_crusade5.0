#Given three positive integers a, b and c. Perform some bitwise operations on them as given below:
#1. d = a ^ a
#2. e = c ^ b
#3. f = a & b
#4. g = ~ e
#Note: ^ is for xor.
#Then print d e f g space seperately. Move the cursor to the next line after printing.
#Then print d e f g space seperately. Move the cursor to the next line after printing.

a = int(input())
b = int(input())
c = int(input())

# code here
d=a**a
e=c**b
f=a*b

print(d, e, f )