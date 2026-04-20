print("Enter 10 elements:")
i=1
L=[]
while i<11:
    n=input("Entries: ")
    L.append(n)
    i+=1
print("OG list:",L)
print("1st 5 elements:",L[:5])
print("last 5 elements:",L[-1:-6:-1])
print("2 to 5 elements:",L[2:6])
print("alternate elements:",L[::2])
    
