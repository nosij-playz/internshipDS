#calculate the sum of a number entered by a user
a=int(input("Enter the number"))
s=0
for i in range(1,a+1):
    s+=i
print(s)