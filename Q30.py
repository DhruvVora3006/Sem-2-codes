try:
    a=int(input("Enter base: "))
    b=int(input("Enter power: "))
except ValueError:
    print("Enter integer.")
else:
    print(f"{a}^{b} = {(lambda x,y:x**y)(a,b)}")
