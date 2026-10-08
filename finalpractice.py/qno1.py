#for i in range (1,11,1):
    #print(i)

#n=int()
#while (n<=10):
 #   print(n)

n=int(input("Enter a no.:"))
reverse=0
while (n>0):
    digit=n%10
    reverse=reverse % 10 + digit
    n//=10
    print(reverse)


    