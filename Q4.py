n=input("Enter string: ")
global v 
global c 
def Count(x):
    v=c=0
    for i in range(len(n)):
        if n[i] in "aeiouAEIOU":
            v+=1
        elif n[i]==' ':
            continue
        else:
            c+=1
    return v,c
v,c=Count(n)
print(f"Vowels: {v}")
print(f"Consonants: {c}")
