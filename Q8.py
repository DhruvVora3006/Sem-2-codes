print("Enter @ to stop.")
L=[]
global k
try:
    n=input("Enter a number: ")
    while n!='@':
        L.append(int(n))
        n=input("Enter a number: ")
except ValueError:
    print("enter an integer or @ only")
else:
    k=int(input("Enter divisibility number: "))
def Div(X):
    return [i for i in X if i%k==0]
print(Div(L))
    
