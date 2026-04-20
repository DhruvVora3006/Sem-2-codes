n=input("Enter string: ")
L=n.split()
def Rem_Vow(X):
    X1=""
    for i in X:
        for j in range(len(i)):
            if i[j] not in "aeiouAEIOU":
                X1+=i[j]
    return X1
print(Rem_Vow(L))
