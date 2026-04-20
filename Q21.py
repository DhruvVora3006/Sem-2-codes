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
    print("Max:",(lambda x:max(x))(L))
    print("Min:",(lambda x:min(x))(L))
