# Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    if number < 2:
        print("Please input a valid number.")
    else:
        for ct in range(2,number):
            if number % ct == 0:
                is_prime = False
                break
        if is_prime == False:
            print("It's not a prime number.")
        else:
            print("It's a prime number.")
# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
