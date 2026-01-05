l=[]
n=int(input("Enter the number of elements in list"))
print("Enter the elements")
for i in range(n):
    x=input()
    l.append(x)
for i in l:
    if len(i)<5:
        l.remove(i)
print(l)