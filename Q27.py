def Sort(X):
    return sorted(L)
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
    print("OG List:",L)
    print("Sorted List:",Sort(L))
