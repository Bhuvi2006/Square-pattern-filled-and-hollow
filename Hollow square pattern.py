#hollow square
n=int(input("Enter the number of rows: "))
s=input("Enter the character that you want to print: ")
for row in range(n):
    for col in range(n):
        if row==n-1 or col== n-1 or row==0 or col ==0:
            print(s, end=" ")
        else:
            print(" ", end=" ")
    print("\n")
