n=int(input("enter range for prime no.s"))
#while (n%n==0 , n%1==0):
    #print(n,end="")

for i in range(2,n+1):
    is_prime=True
    for j in range(2,i):
     if i % j==0:
        is_prime=False
        break
    if is_prime:
        print(i)