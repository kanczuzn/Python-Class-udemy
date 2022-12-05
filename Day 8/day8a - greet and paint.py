# def greet(x):
#     for ct in range(x):
#         greet=input("Hello, what is your name? ")
#         print(f"Nice to meet you {greet}. "
#               f"I hope you have a great day.")
#         print("Goodbye!")
#
# def greet_with_name(name):
#     print(f"Hello {name}!")
#     print(f"Nice to meet you {name}. "
#           f"I hope you have a great day.")
#     print("Goodbye!")
#
# def greet_with(name,location):
#     print(f"Hello {name}!")
#     print(f"Nice to meet you, {name}.")
#     print(f"I hope the weather is nice in {location}.")
#
# greet_with(name="Steve",location="Texas")


#Write your code below this line 👇

def paint_calc(height, width, cover):
    paint_cans = round(((height*width)/cover)+.5)
    print(f"You'll need {paint_cans} cans of paint.")




#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

