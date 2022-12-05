# 🚨 Don't change the code below 👇
import math

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = weight/height**2

if BMI < 18.5:
    BMI_desc = "are underweight"
elif 18.5 <= BMI < 25:
    BMI_desc = "have a normal weight"
elif 25 <= BMI < 30:
    BMI_desc = "are slightly overweight"
elif 30 <= BMI < 35:
    BMI_desc = "are obese"
else:
    BMI_desc = "are clinically obese"

print(f"Your BMI is {math.floor(BMI+.5)}, you {BMI_desc}.")
print(round(2.5))
