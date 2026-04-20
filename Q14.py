print("Enter @ to stop.")
L=[]
L1=[]
try:
    n=input("Enter: ")
    while n!='@':
        L.append(int(n))
        n=input("Enter: ")
except ValueError:
    print("Enter integer or @.")
k=int(input("Enter target sum: "))
for i in range(len(L)):
    for j in range(len(L)):
        if L[i]+L[j]==k:
            L1.append((L[i],L[j]))
print(L1)
