
L=[]
try:
    n=int(input("Enter: "))
except ValueError:
    print("Enter postitive integer.")
else:  
    def Fibo(X,a=0,b=1):
        if X<0:
            return 
        elif X==0:
            return a
        else:
            print(a,end=' ')
            Fibo(X-1,b,a+b)
            
    Fibo(n))   
    
