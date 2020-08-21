for num in range(1,101):
    if not(num % 7 == 0 or num % 10 == 7 or (num // 70 == 1 and num % 70 <10)):
        print(num)
