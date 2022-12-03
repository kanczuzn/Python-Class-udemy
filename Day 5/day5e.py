# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
import string
import random

run_pass_start = 0
pass_len = 0
pass_num = 0
pass_spc = 0
print("Welcome to the PyPassword Generator!")
while run_pass_start == 0:
    try:
        pass_len = int(input("How long should your password be?\n"))
        pass_num = int(input("What's the minimum amount of numbers in the password?\n"))
        pass_spc = int(input("what's the minimum special characters in your password?"
                         "\n(0 will mean no special characters)\n"))
        if pass_num + pass_spc <= pass_len:
            run_pass_start = 1
        else:
            print("Please try again.")
    except:
        print("Please only pass numbers.")

plist_lett = list(string.ascii_letters)
plist_dig = list(string.digits)
plist_spc = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
pass_dig_ct = 0
pass_spc_ct = 0
run_pass_create = 0

while run_pass_create == 0:
    pass_dig_ct = 0
    pass_spc_ct = 0
    new_pass_list = [''] * pass_len
    new_pass = ""
    for ct in range(0, pass_len):
        if pass_num == pass_len:
            x = 2
        elif pass_spc == pass_len:
            x = 3
        elif pass_spc == 0:
            x = random.randint(1, 2)
        else:
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
    for ct in range(0, pass_len):
        max_lim = round((pass_len / 9) + 1)
        new_pass += new_pass_list[ct]
        if new_pass_list.count(new_pass_list[ct]) > max_lim and pass_len < 90:
            pass_dig_ct = 0
            pass_spc_ct = 0
            ct = len(new_pass_list)
        if ct + 1 < pass_len:
            if new_pass_list[ct] == new_pass_list[ct + 1]:
                if plist_lett.count(new_pass_list[ct + 1]) > 0:
                    while new_pass_list[ct] == new_pass_list[ct + 1]:
                        x = random.randint(0, len(plist_lett) - 1)
                        new_pass_list[ct + 1] = plist_lett[x]
                elif plist_dig.count(new_pass_list[ct + 1]) > 0:
                    while new_pass_list[ct] == new_pass_list[ct + 1]:
                        x = random.randint(0, len(plist_dig) - 1)
                        new_pass_list[ct + 1] = plist_dig[x]
                else:
                    while new_pass_list[ct] == new_pass_list[ct + 1]:
                        x = random.randint(0, len(plist_spc) - 1)
                        new_pass_list[ct + 1] = plist_spc[x]

    if (pass_dig_ct >= pass_num) and (pass_spc_ct >= pass_spc):
        break

print(f"Your new password is: {new_pass}")
