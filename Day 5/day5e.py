# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
import string
import random

print("Welcome to the PyPassword Generator!")
pass_len = int(input("How long should your password be?\n"))
pass_num = int(input("What's the minimum amount of numbers in the password?\n"))
pass_spc = int(input("How many special characters should be in your password?\n"))
plist_lett = list(string.ascii_letters)
plist_dig = list(string.digits)
plist_spc = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
pass_dig_ct = 0
pass_spc_ct = 0

while pass_num >= pass_dig_ct and pass_spc >= pass_spc_ct:
    pass_dig_ct = 0
    pass_spc_ct = 0
    new_pass = ""
    for ct in range(1,pass_len+1):
        x = random.randint(1,3)
        if x == 1:
            y = random.randint(0,len(plist_lett)-1)
            new_pass += plist_lett[y]
        elif x == 2:
            y = random.randint(0, len(plist_dig)-1)
            new_pass += plist_dig[y]
            pass_dig_ct +=1
        else:
            y = random.randint(0, len(plist_spc)-1)
            new_pass += plist_spc[y]
            pass_spc_ct +=1
    if pass_num <= len(plist_dig)-1 and pass_spc <= len(plist_spc)-1:
        for ct in range(1,len(new_pass)-1):
            if new_pass.count(new_pass[ct]) > 2:
                pass_dig_ct = 0
                pass_spc_ct = 0

print(f"Your new password is: {new_pass}")
