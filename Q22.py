L=[]
e=0
o=0
print("Enter @ to stop")
try:
    n=input("Enter: ")
    while n!='@':
        L.append(int(n))
        n=input("Enter: ")
except ValueError:
    print("Enter integer or @")
else:
    print("Even:",len(list(filter(lambda x: x%2==0,L))))
    print("Odd:",len(list(filter(lambda x: x%2!=0,L))))
