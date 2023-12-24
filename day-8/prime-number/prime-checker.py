# prime number checker
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("it's a prime number")
    else:
        print("it's not a prime number")


user_number = int(input("Please Enter an Number: "))
prime_checker(user_number)
