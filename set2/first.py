# write a program to check even or odd a number

a=int(input("Enter the number"))
def odd(a):
    return a%2!=0
if(odd(a)):
    print("Odd\n")
else:
    print("Even\n")
    