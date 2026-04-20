n = input("Enter sentence: ")
L = n.split()
global d
def Cou_fre(X):
    d={}
    for i in X:
       if i.lower() not in d:
           d[i]=1
       else:
           d[i]+=1
    print(d)
Cou_fre(L)
        
