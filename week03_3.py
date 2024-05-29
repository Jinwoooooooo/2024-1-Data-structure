"""
나라이름 목록에서
각 나라명이 동북아 3국이면
  xx는 동북아 3국 중의 하나입니다.
이니면
  xx는 동북아 3국에 포함되지 않습니다.

"""

s = "Thai/Miyanma/Vietnam/Japan/Taiwan/Korea/Singapore/China/Cambodia"
ss = s.split("/")

n = "Korea/Japan/China"
ne = n.split("/")

for item in ss:
    if item in ne:
        print("{}은 동북아 3국 중의 하나입니다.".format(item))
    else:
        print("{}은 동북아 3국에 포함되지 않습니다.".format(item))
