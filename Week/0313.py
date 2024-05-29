Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Hello Python!!")
Hello Python!!
print("Hello Python!!")
Hello Python!!
print("DIT" * 5)
DITDITDITDITDIT
print("DIT" * "KOREA")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print("DIT" * "KOREA")
TypeError: can't multiply sequence by non-int of type 'str'
print("DIT" + "KOREA")
DITKOREA
a = "korea"
print(a + 10)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(a + 10)
TypeError: can only concatenate str (not "int") to str
print(a + '10')
korea10
print(a + 10)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(a + 10)
TypeError: can only concatenate str (not "int") to str
a, b = 200, 300
a
200
b
300
a = 100
b = 3.141592
print("a = %d, b = %f"%(a, b))
a = 100, b = 3.141592
a = 100, b = 3.141592
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
print("a = {}, b = {}".format(a, b)

      asd
      
SyntaxError: '(' was never closed
print("a = {}, b = {}".format(a, b))
      
a = 100, b = 3.141592
print("a = {}, b = {}".format(a, b))
      
a = 100, b = 3.141592
print("a = {1}, b = {0}".format(a, b))
      
a = 3.141592, b = 100
print("a = {x}, b = {y}".format(x=a, y=b))
      
a = 100, b = 3.141592
print("a = {x}, b = {y}".format(x=b, y=a))
      
a = 3.141592, b = 100
print("a = %10d, b = %.3f"(a,b))
      
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print("a = %10d, b = %.3f"(a,b))
TypeError: 'str' object is not callable
print("a = %10d, b = %.3f"%(a,b))
      
a =        100, b = 3.142
print("a = %-10d, b = %.3f"%(a,b))
      
a = 100       , b = 3.142
print("a = {x}, b = {y}".format(x=b, y=a))
      
a = 3.141592, b = 100
print("DIT")
      
DIT



print("DIT")
      
DIT
print("DIT", end = "!!!")
      
DIT!!!
print("a = {x}, b = {y}".format(x=b, y=a), end="!!!!")
      
a = 3.141592, b = 100!!!!
print("KOREA", "JAPAN", "CHINA", sep='/')
      
KOREA/JAPAN/CHINA
print(a, "+", b, "=", a+b)
      
100 + 3.141592 = 103.141592
print(a, "+", b, "=", a+b, end="!!")
      
100 + 3.141592 = 103.141592!!
print(a, "+", b, "=", a+b, sep="/")
      
100/+/3.141592/=/103.141592
print(a, "+", b, "=", a+b, sep=" ")
      
100 + 3.141592 = 103.141592
print(a, "+", b, "=", a+b)
      
100 + 3.141592 = 103.141592
print(a, "+", b, "=", a+b, sep="")
      
100+3.141592=103.141592
print("KOREA", "JAPAN", "CHINA", sep=",")
      
KOREA,JAPAN,CHINA
print("KOREA", "JAPAN", "CHINA", sep=", ")
      
KOREA, JAPAN, CHINA
print("KOREA", "JAPAN", "CHINA", sep="                ")
      
KOREA                JAPAN                CHINA
print("KOREA", "JAPAN", "CHINA", sep="----------")
      
KOREA----------JAPAN----------CHINA
>>> print("KOREA", "JAPAN", "CHINA", sep=",")
...       
KOREA,JAPAN,CHINA
>>> name = input("당신의 이름은 ?")
...       
당신의 이름은 ?팜하니
>>> name
...       
'팜하니'
>>> print("안녕하세요", name, "씨")
...       
안녕하세요 팜하니 씨
>>> print("안녕하세요 %s씨" %(name))
...       
안녕하세요 팜하니씨
>>> print("안녕하세요 {}씨".format(name))
...       
안녕하세요 팜하니씨
>>> print("안녕하세요 {0}씨".format(name))
...       
안녕하세요 팜하니씨
>>> n = input("정수 입력 : ")
...       
정수 입력 : 100
>>> n
...       
'100'
>>> print(int(n)+100)
...       
200
>>> n = int(input("정수 입력 : "))
...       
정수 입력 : 100
>>> n
...       
100
>>> print(n+100)
...       
200
