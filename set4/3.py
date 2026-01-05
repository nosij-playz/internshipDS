#Create a new list and concatinate both
l=[]
n=int(input("Enter the number of elements in list 1"))
print("Enter the elements")
for i in range(n):
    x=input()
    l.append(x)
l1=[]
n1=int(input("Enter the number of elements in list 1"))
print("Enter the elements")
for i in range(n1):
    x=input()
    l1.append(x)
print("Before Concate")
print("first List"+str(l))
print("Second List "+str(l1))
for i in l1:
    l.append(i)
print("Concated List "+str(l))