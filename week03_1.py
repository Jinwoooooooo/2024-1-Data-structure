"""
주어진 문자열을 분할하고,
분할된 항목 하나씩 차례대로 출력하기
"""

s = "Korea/Japan/China"

n = s.split("/")

for item in n:
    print(item)
