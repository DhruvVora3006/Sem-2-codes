L=[]
L1=[]
print("Press @ to stop.")
try:
    n=input("Enter: ")
    while n!='@':
        L.append(int(n))
        n=input("Enter: ")
except ValueError:
    print("Enter a Valid Integer")
    
else:    
    print("entered list:",L)
def Pal(X):
    for j in L:
        if str(j) in str(j)[::-1]:
            L1.append(int(j))
    return L1
    print("Palindromes:",Pal(L))
