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
    print("Sq List:",list(map(lambda x:x**2,L)))
