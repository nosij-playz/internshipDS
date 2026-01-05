#write a python code to check whether the given is palindrome or not
def palindrome(a):
    return a==a[::-1]

a=input("Enter the string  ")
print("Palindrome " +str(palindrome(a)))