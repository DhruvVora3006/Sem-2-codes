# Write a Python program to remove all prime numbers from a list using a
# higher order function.
#•   Accept a list of integers from the user. 
#•   Create a function that returns a list with all prime numbers removed. 
#•   Display the result

L=[]
L1=[]
print("Enter @ to stop.")
n=input("Enter elements: ")
while n!='@':
    try:
        L.append(int(n))
    except ValueError:
        print("Enter an integer or @.")
    n=input("Enter elements: ")
    
print("Entered list:",L)

def Rem_prime(X):
    for m in X:
        if (m==0 or m==1):
            L1.append(m)
        else:
            for i in range(2,int(m**0.5+1)):
                if m%i==0:
                    L1.append(m)
                    break
    return L1

print("Corrected List:",Rem_prime(L))

        
            
                
                    
                
        
