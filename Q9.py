F=[]
def fact(x):
    if x<0:
        print("Invalid")
    a=1
    for i in range(x,0,-1):
        a*=i
    return a

        
try:
    print("Enter @ to stop.")
    n=input("ENTER NUMBER: ")
    while n!='@':
        F.append(int(n))
        n=input("Enter number: ")
except ValueError:
    print("Enter whole number.")
else:
    print(list(map(fact,F)))
    


    
