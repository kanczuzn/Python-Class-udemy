# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
avg_ht = 0
x = 0
for n in student_heights:
    avg_ht += n
    x += 1
avg_ht = round(avg_ht / x)
print(avg_ht)