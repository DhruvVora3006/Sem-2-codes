def isPrime(X):
    if X==1 or X==0:
        return "Neither prime nor composite."
    elif X<0:
        return "Invalid Choice"
    for i in range(2,int(X**0.5)+1):
        if X%i==0:
            return "Composite"
        else:
            continue
    return "Prime"

try:
    n=int(input("Enter number: "))
except ValueError:
    print("Enter integer")
else:
    print(f"Number {n} = {isPrime(n)}")
