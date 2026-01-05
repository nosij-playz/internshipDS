l=[]
n=int(input("Enter the number of elements in list"))
print("Enter the elements")
for i in range(n):
    x=int(input())
    l.append(x)
def sum(s):
    if s==0:
        return 0
    return s[0]+sum(s[1:])
print("The sum of elements in the list is", sum(l))