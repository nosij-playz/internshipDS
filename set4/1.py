#create a list of fruits and add new fruits to list then acess elements using index

l=[]
n=int(input("Enter the number of elements"))
print("Enter the elements")
for i in range(n):
    x=input()
    l.append(x)
for i in range(n):
    print(l[i])