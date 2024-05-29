"""
나라이름 목록에서
각 나라명이 동북아 3국이면
    xx는 동북아 3국중의 하나입니다.
아니면
    xx는 동북아 3국에 포함되지 않습니다.
"""

s = "Thai/Miyanma/Vietnam/Japan/Taiwan/Korea/Singapore/China/Cambodia"

n = "Korea/Japan/China"

country1 = s.split("/")
country2 = n.split("/")

for i in country1:
    if i in country2:
        print("{}는 동북아 3국중의 하나입니다.".format(i))
    else:
        print("{}는 동북아 3국에 포함되지 않습니다.".format(i))
