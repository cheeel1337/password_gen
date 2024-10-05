import random
symbols = '+-/*!&$#?(!"£$%^&*()^%^&*)'
lenght = input('Введите длину пароля: ')
password = ''

for i in range(int(lenght)):
    password += random.choice(symbols)

print(password)
