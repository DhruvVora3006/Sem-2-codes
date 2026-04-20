def Sort(X):
    return sorted(L,reverse=True)[1]

print("Enter @ to stop.")
L=[]
try:
    n=input("Enter: ")
    while n!='@':
        L.append(int(n))
        n=input("Enter: ")
except ValueError:
    print("Enter integer or @.")
else:
    print(Sort(L))
