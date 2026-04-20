print("List 1: ")
def Common():
    return list(set(L1).intersection(set(L2)))
L1=[]
L2=[]
try:
    print("Enter @ to stop.")
    l1=input("Enter: ")
    while l1!='@':
        L1.append(int(l1))
        l1=input("Enter: ")
    print("List 2: ")
    print("Enter # to stop.")
    l2=input("Enter: ")
    while l2!='#':
        L2.append(int(l2))
        l2=input("Enter: ")
except ValueError:
    print("Enter integer or @.")
else:
    print(Common())
