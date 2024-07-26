f_or_c = int(input('Press 1 for F to C or press 2 for C to F: '))

if f_or_c == 1:
    degrees = int(input('Enter the degrees in F: '))
    result = (degrees - 32) * (5 / 9)
else:
    degrees = int(input('Enter the degrees in C: '))
    result = (degrees * (9 / 5)) + 32

print('Your result is: ', result)
