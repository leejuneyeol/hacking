from random import *

user_pw = input('pwd: ')

password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

already_try = []
n = 0
guess = ""
while guess != user_pw:
    guess = ""
    for letter in range(len(user_pw)):
        guess_letter = password[randint(0, 35)]
        guess = str(guess_letter)+str(guess)
    if guess in already_try:
        pass
    else:
        already_try.append(guess)
        print(guess)
        n += 1
print("Your PW is ", guess)
print('try: ', n)