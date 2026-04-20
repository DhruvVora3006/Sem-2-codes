#Reverse input words and display result
n=input("Enter a sentence: ")
print("OG sentence:",n)
L=n.split()
L1=[]
print("Reversed words:",end=' ')
for i in L:
    print("".join(i[::-1]),end=' ')


