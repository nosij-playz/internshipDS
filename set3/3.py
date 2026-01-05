#write a program to cout the no of vowels in a given input string
a=input("enter the string")
v=['a','e','i','o','u','A','E','I','O','U']
c=0
for i in a:
    for j in v:
        if i==j:
            c+=1

print("count ="+str(c))