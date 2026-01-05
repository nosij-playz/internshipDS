def add(a):
    if a==0:
        return a
    return a+add(a-1)

n=int(input("Enter a number"))
print("The sum of first",n,"natural numbers is",add(n))
    