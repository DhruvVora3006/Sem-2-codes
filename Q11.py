print("Press @ to stop.")
L=[]
def Even_Sum(X):
    return sum([i for i in X if i%2==0])
try:
    n=input("Enter elements: ")
    while n!='@':
        L.append(int(n))
        n=input("Enter elements: ")
except ValueError:
    print("Enter integer or @")
else:
    print(Even_Sum(L))
    
