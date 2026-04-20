print("Enter # to stop.")
L=[]
try:
    n=input("Enter Numbers: ")
    while n!='#':
        L.append(n)
        n=input("Enter Numbers: ")
except ValueError:
    print("Enter integer or #.")
print(list(filter(lambda x: len(x)%2==0,L)))
