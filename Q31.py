try:
    C=int(input("Enter celcius value: "))
except ValueError:
    print("Enter integer.")
else:
    print(f"{C} degrees in Fahrenheit = {(lambda x: (1.8*x+32))(C)}")
