#Display all prime factors
try:
    n=int(input("Enter a number: "))
except ValueError:
    print("Enter an integer")
else:
    print(f"Factors of {n}: ")
    i=1
    while i<=n:
        if n==0:
            print(0)
        print(i,end= ',') if n%i==0 else None
        i+=1
