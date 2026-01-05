def insertlist():
    l=[]
    n=int(input("Enter the number of elements in list"))
    print("Enter the elements")
    for i in range(n):
        x=input()
        l.append(x)
    return l

print(insertlist())
