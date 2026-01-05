#find the count of occurance of each element

l=[]
n=int(input("Enter the number of elements"))
print("Enter the elements")
for i in range(n):
    x=input()
    l.append(x)
c=[]
for i in l:
    c.append(l.count(i))
print(l)
print(c)
