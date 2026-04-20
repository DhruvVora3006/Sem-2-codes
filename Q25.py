def Concat(X,Y):
    return list(X+Y)
L1=[]
L2=[]
print("List 1")
print("Enter @ to stop")
try:
    n=input("Enter: ")
    while n!='@':
        L1.append(int(n))
        n=input("Enter: ")
except ValueError:
    print("Enter integer or @")
print("List 2:")
print("Enter $ to stop")
try:
    n=input("Enter: ")
    while n!='@':
        L2.append(int(n))
        n=input("Enter: ")
except ValueError:
    print("Enter integer or $")
else:
    print(Concat(L1,L2))
