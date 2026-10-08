# for i in range (1,5):
#     for j in range (1,5,1):
#         print("*",end="")
#     print()

for i in range (0,5):
    for j in range (0,5):
        if (i==0 or i==4 or j==0 or j==4):
            print(i,end=" ")
    
        else:
            print(" ",end=" ")
    print()

