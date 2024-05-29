Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = "ABCDEFGHIJKLMN"
a[1:4]
'BCD'
a[-1]
'N'
a[-2]
'M'
a[-3]
'L'
a[0]
'A'
a[-1:-2]
''
a[-1:2]
''
a[-1::2]
'N'
a[-1::3]
'N'
a[-1::-2]
'NLJHFDB'
a[-1,2]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a[-1,2]
TypeError: string indices must be integers, not 'tuple'
a[-2:]
'MN'
a[-2:]
'MN'
st = "Hello, Python"
st.upper(st)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    st.upper(st)
TypeError: str.upper() takes no arguments (1 given)
st.upper()
'HELLO, PYTHON'
st.lower()
'hello, python'
st
'Hello, Python'
st2 = "     Hello, Python     "
st2.trim()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    st2.trim()
AttributeError: 'str' object has no attribute 'trim'. Did you mean: 'strip'?
>>> 
... 
... st2.trim("")
Traceback (most recent call last):
  File "<pyshell#22>", line 3, in <module>
    st2.trim("")
AttributeError: 'str' object has no attribute 'trim'. Did you mean: 'strip'?
>>> st2.strip()
'Hello, Python'
>>> st2
'     Hello, Python     '
>>> st2 = st2.strip()
>>> st2
'Hello, Python'
>>> st2.replace("l", "L")
'HeLLo, Python'
>>> st2
'Hello, Python'
>>> st2.replace("ll","korea")
'Hekoreao, Python'
>>> s = "Korea/Japan/China"
>>> s.split("/")
['Korea', 'Japan', 'China']
>>> n = s.split("/")
>>> n
['Korea', 'Japan', 'China']
>>> n[0]
'Korea'
>>> len(3)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    len(3)
TypeError: object of type 'int' has no len()
>>> len(n)
3
>>> len(s)
17
>>> s
'Korea/Japan/China'
"""
주어진 문자열을 분할하고,
분할된 항목 하나씩 차례대로 출력하기
"""
country = s.split("/")
for i in country:
  print(country)
