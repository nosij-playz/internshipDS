l=[]
l1=[]
n=int(input("Enter the number of elements in list 1"))
print("Enter the elements")
for i in range(n):
    x=input()
    l.append(x)
for i in l:
    l1.append(str(i).lower())
l=set(l1)
print(l)