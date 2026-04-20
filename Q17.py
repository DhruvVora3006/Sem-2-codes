try:
    n=int(input("Enter age: "))
except ValueError:
    print("Enter positive integer.")
else:
    if bool((lambda x: x<18)(n)):
        print("Not eligible")
    else:
        print("Eligible")
              
    
