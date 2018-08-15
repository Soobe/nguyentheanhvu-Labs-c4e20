x = int(input("x = "))

opera = input("Operation (+,-,*,/): ")

y = int(input("y ="))

res = 0

if opera == '+':
    res = x + y

elif opera == '-':
    res = x - y

elif opera == '*':
    res = x * y

elif opera == '/':
    res = x / y

print('*'* 10)
print('{} {} {} = {}'.format(x, opera,y,res))
print('*' * 10)               