for value in range(1, 5):
    print(value)
    
    
numbers= list(range(1, 6))
print(numbers)


even_numbers = list(range(2, 11, 2))
print(even_numbers)

odd_numbers = list(range(1, 22, 2))
print(odd_numbers)





squares = []
for value in range(81, 99):
    square = value**2
    squares.append(square)
    
print(squares)



cubes = []
for value in range(22, 35):
    cube = value**3
    cubes.append(cube)
    
print(cubes)





squares = [value**2 for value in range(2, 22)]
print(squares)






multiples_of_3 = list(range(3, 33, 3))
print(multiples_of_3)