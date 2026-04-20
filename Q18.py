from random import randint
L=[randint(1,10) for i in range(10)]
print("Random List:", L)
print("Cubed list:",end=' ')
print(list(map(lambda x:x**3,L)))
