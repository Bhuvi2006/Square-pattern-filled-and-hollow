n=int(input("Enter the number of rows: "))
s=input("Enter the character that you want to print: ")
for row in range(n):
    for col in range(n):
        print(s, end=" ")
    print("\n")
