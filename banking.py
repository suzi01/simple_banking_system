# Write your code here
import random

def login_screen():
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')
    
def successful_login():
    print('1. Balance')
    print('2. Log out')
    print('0. Exit')

def luhn_card_num(card_num):
    arr = list(card_num)
    results = [int(i) for i in arr]
    print(results)
    for i in range(len(results)):
      if i%2 ==0:
        results[i]= results[i]*2
    print(results)
    for n, i in enumerate(results):
      if i>9:
        results[n] = i-9
    print(results)
    Sum = sum(results)
    print(Sum)
    int_checksum = None
    if Sum%10 == 0:
      int_checksum = 0
    else:
      num = Sum%10
      int_checksum = 10 - num
    check_sum = str(int_checksum)
    print(check_sum)
    return check_sum


account = []
login_screen()

option = input()
while True:
    if option == '0':
        print('Bye!')
        exit()
    if option == '1':
        NII = '400000'
        account_num = random.randint(0,999999999)
        if account_num < 1000000000: 
            account_num = str(account_num).zfill(9) 
        else:
            account_num = str(account_num) 
        unfinished_card_num = NII + account_num
        last_digit = luhn_card_num(unfinished_card_num)
        
        card_num = unfinished_card_num + last_digit
        
        pin_num = random.randint(0,9999)
        if pin_num <1000:
            pin_num = str(pin_num).zfill(4)
        else:
            pin_num = str(pin_num)
        
        
        print('Your card has been created')
        print('Your card number:')
        print(card_num)
        print('Your card PIN:')
        print(pin_num)
        account.append(card_num)
        account.append(pin_num)
        login_screen()
        option = input()
    
    if option == '2':
        print('Enter your card number:')
        user_card = input()
        print('Enter your PIN:')
        user_pin = input()
        if (user_pin != account[1]) or (user_card != account[0]):
            print('Wrong card number or PIN!')
            login_screen()
            option = input()
        else:
            print('You have successfully logged in!')
            successful_login()
            option2 = input()
            while option2 != '0':
                if option2 == '1':
                    print ('Balance: ', 0)
                    successful_login()
                    option = input()
                if option2 == '2':
                    print('You have successfully logged out!')
                    login_screen()
                    option = input()
                    break
            else:
                print('Bye!')
                exit()
