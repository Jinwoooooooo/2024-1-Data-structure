primes = [2, 3, 5, 7]
n = int(input("1부터 10까지의 수를 입력하세요: "))
if n in primes:
    print("소수")
elif n > 1 and n < 11:
    print("소수 아님")
else:
    print("범위를 벗어남")
