def Fact(X):
    if X<0:
        return "Invalid entry."
    elif X==0:
        return 1
    return X*Fact(X-1)
try:
    n=int(input('Enter number: '))
except ValueError:
    print('Enter integer')
else:
    print(Fact(n))
