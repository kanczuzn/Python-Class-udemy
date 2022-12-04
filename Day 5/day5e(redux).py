import string
import random

run_pass = True
pass_len = 0
pass_spc = ""
print("Welcome to the PyPassword Generator!")
while run_pass is True:
    while pass_len < 3:
        try:
            pass_len = int(input("How long should your password be?\n"))
            if pass_len < 3:
                print("Please specify a length over 3.")
                pass_len = 0
        except:
            print("Please only pass numbers.")
            pass_len = 0
    try:
        pass_num = input("Would you like numbers in your password?(y/n)\n").lower()[0]
    except:
        pass_num = "n"
    pass_spc = input("What special characters are possible in your password?"
                         "\n(Leave blank for none)\n").strip()

    plist = []
    new_pass = []
    p_letter = list(string.ascii_letters)
    plist += p_letter
    if pass_num == "y":
        p_digit = list(string.digits)
        plist += p_digit
    if len(pass_spc) > 0:
        p_spc = list(pass_spc)
        plist += p_spc

    run_pass_create = True

    while run_pass_create is True:

        for ct in range(pass_len):
            new_pass += random.choice(plist)
        if len(new_pass) == pass_len:
            if pass_num == "y":
                pass_check_num = len([x for x in p_digit if x in new_pass])
                if pass_check_num == 0:
                    pass_check = True
                    while pass_check is True:
                        rand_int = random.randint(0,pass_len-1)
                        if new_pass[rand_int] in p_letter:
                            new_pass[rand_int] = random.choice(p_digit)
                            pass_check = False
            else:
                pass_check_num = 1

            if len(pass_spc) > 0:
                pass_check_spc = len([x for x in p_spc if x in new_pass])
                if pass_check_spc == 0:
                    pass_check = True
                    while pass_check is True:
                        rand_int = random.randint(0,pass_len-1)
                        if new_pass[rand_int] in p_letter:
                            new_pass[rand_int] = random.choice(p_spc)
                            pass_check = False
            else:
                pass_check_spc = 1

            for ct in range(0,pass_len-1):
                limit = (pass_len/round(len(plist)/2))+1
                while new_pass[ct] == new_pass[ct+1]:
                    new_pass[ct+1] = random.choice(plist)
                while (new_pass.count(new_pass[ct]) > limit) and (pass_len < (len(plist) * 5) and
                                                                  pass_check_num > 0 and pass_check_spc > 0):
                    pass_check_val = new_pass[ct]
                    while new_pass[ct] == pass_check_val:
                        new_pass[ct] = random.choice(plist)
                        if pass_num == "y":
                            pass_check_num = len([x for x in p_digit if x in new_pass])
                            if pass_check_num == 0:
                                pass_check = True
                                while pass_check is True:
                                    rand_int = random.randint(0, pass_len - 1)
                                    if new_pass[rand_int] in p_letter:
                                        new_pass[rand_int] = random.choice(p_digit)
                                        pass_check = False
                        else:
                            pass_check_num = 1

                        if len(pass_spc) > 0:
                            pass_check_spc = len([x for x in p_spc if x in new_pass])
                            if pass_check_spc == 0:
                                pass_check = True
                                while pass_check is True:
                                    rand_int = random.randint(0, pass_len - 1)
                                    if new_pass[rand_int] in p_letter:
                                        new_pass[rand_int] = random.choice(p_spc)
                                        pass_check = False
                        else:
                            pass_check_spc = 1
                run_pass_create = False
            print(f"Your new password is: {''.join(new_pass)}")
        run_pass_create = input("\nWould you like to create another? (y/n)\n").lower()[0]

        if run_pass_create == "y":
            pass_len = 0
            pass_num = ""
            pass_spc = ""
        else:
            run_pass = False