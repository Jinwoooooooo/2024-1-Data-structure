"""
정수를 입력받은 다음,
양수이면 n은 양수입니다.
아니면
n은 양수가 아닙니다.
"""
n = int(input("정수를 입력하세요: "))
if n > 0:
    print("{}은 양수입니다.".format(n))
else:
    print("{}은 정수입니다.".format(n))
