n = int(input("1~10범위의 정수 입력:"))

primes = [2, 3, 5, 7]

if n in primes:
    print("{}는 소수입니다.".format(n))
elif n > 1 and n < 11:
    print("{}는 소수가 아닙니다.".format(n))
else:
    print("{}는 잘못된 입력입니다.".format(n))
