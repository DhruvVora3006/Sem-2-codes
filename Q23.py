def Rem_Dup(X):
    return list(set(X))
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
    print("OG list:",L)
    print("Uniq List:",Rem_Dup(L))
