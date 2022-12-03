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
    new_pass_list = [''] * pass_len
    new_pass = ""
    for ct in range(0, pass_len):
        x = random.randint(1, 3)
        if x == 1:
            y = random.randint(0, len(plist_lett) - 1)
            new_pass_list[ct] = plist_lett[y]
        elif x == 2:
            y = random.randint(0, len(plist_dig) - 1)
            new_pass_list[ct] = plist_dig[y]
            pass_dig_ct += 1
        else:
            y = random.randint(0, len(plist_spc) - 1)
            new_pass_list[ct] = plist_spc[y]
            pass_spc_ct += 1
    if pass_len < 1000:
        for ct in range(0, pass_len):
            max_lim = round((pass_len / 23) + 1)
            new_pass += new_pass_list[ct]
            if new_pass_list.count(new_pass_list[ct]) > max_lim:
                pass_dig_ct = 0
                pass_spc_ct = 0
                ct = len(new_pass_list)
            elif ct + 1 < pass_len:
                if new_pass_list[ct] == new_pass_list[ct + 1]:
                    if plist_lett.count(new_pass_list[ct + 1]) > 0:
                        while new_pass_list[ct] == new_pass_list[ct + 1]:
                            y = random.randint(0, len(plist_lett) - 1)
                            new_pass_list[ct + 1] = plist_lett[y]
                    elif plist_dig.count(new_pass_list[ct + 1]) > 0:
                        while new_pass_list[ct] == new_pass_list[ct + 1]:
                            y = random.randint(0, len(plist_dig) - 1)
                            new_pass_list[ct + 1] = plist_dig[y]
                    else:
                        while new_pass_list[ct] == new_pass_list[ct + 1]:
                            y = random.randint(0, len(plist_spc) - 1)
                            new_pass_list[ct + 1] = plist_spc[y]

print(f"Your new password is: {new_pass}")
