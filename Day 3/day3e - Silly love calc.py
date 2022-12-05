# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
fmess = ""

comb_name = str.lower(name1 + name2)
tcount = str(sum(map(comb_name.count,["t","r","u","e"])))
lcount = str(sum(map(comb_name.count,["l","o","v","e"])))
fcount = int(tcount+lcount)

if fcount > 90 or fcount < 10:
    fmess = ", you go together like coke and mentos"
elif 40 < fcount < 50:
    fmess = ", you are alright together"

print(f"Your score is {fcount}{fmess}.")
