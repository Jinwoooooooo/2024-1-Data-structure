"""
주어진 문자열을 분할하고,
분할된 항목 하나씩 차례대로 출력하기
"""
s = "KOREA/JAPAN/CHINA"
country = s.split("/")
for i in country:
    print(i)
