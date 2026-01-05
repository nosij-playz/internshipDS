
def transform(x):
    def padakkam(a, b):
        result = x(a, b)
        return result*int(input("Enter multiplier: "))
    return padakkam

@transform
def add(a,b):
    return a+b

print(add(2,3))