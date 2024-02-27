name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')


while True:
    print("please type your name")
    name = input()
    if name == "Your name":
        break
print("Thank you!")


while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
         continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
         break
print('Access granted.') 

total = 0
for num in range(101):
    total= total + num

print(total)    

total = 0
while total < 101:
    print(total)
    total=total+1

import random
for i in range(5):
    print(random.randint(1,10))

for i in range(1,10,5):
    print(i)
