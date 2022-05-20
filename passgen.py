import random
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num=['1','2','3','4','5','6','7','8','9','0']
symbol=['!','@','#','$','%','?','/','|','*','&']
letters=int(input("how many letters do you want?\n"))
nums=int(input("how many nums do you want?\n"))
symbols=int(input("how many symbols do you want?\n"))
password=""
for char in range(1,letters+1):
    password=password+random.choice(letter)
for dig in range(1,nums+1):
    password=password+random.choice(num)
for sym in range(1,symbols+1):
    password=password+random.choice(symbol)
print(password)