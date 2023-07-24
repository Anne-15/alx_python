def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    a = 3
    while a * a <= number:
        if number % a == 0:
            return False
        a += 2
    return True
