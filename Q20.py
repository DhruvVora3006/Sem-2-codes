def Sum(X):
    return sum(X)
L=[]
print("Enter @ to stop")
try:
    n=input("Enter: ")
    while n!='@':
        L.append(int(n))
        n=input("Enter: ")
except ValueError:
    print("Enter integer or @")
else:
    try:
        print("Sum of elements:",Sum(L))
    except TypeError:
        print("Elements werent all integers.")

