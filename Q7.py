n=input("Enter a sentence: ")
L=n.split()
def isduplicate(X):
    return list(set(X))
print("Unique list:",isduplicate(L))
