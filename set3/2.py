#Create a loop that print first 10 even numbers
def even(a):
    return a%2==0
for i in range(20):
    if(even(i)):
        print(i)