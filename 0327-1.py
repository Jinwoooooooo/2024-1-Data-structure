Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
lst = [10, 20, 30]
lst
[10, 20, 30]
lst[0]
10
lst[1]
20
lst[-1]
30
lst[-2]
20
lst[1]
20

lst[0] = "KOREA"
lst
['KOREA', 20, 30]
lst[1] = True
lst
['KOREA', True, 30]
lst[-1] = ["Apple", "Kiwi" "Mango"]
lst
['KOREA', True, ['Apple', 'KiwiMango']]
lst[-1] = ["Apple", "Kiwi", "Mango"]
lst
['KOREA', True, ['Apple', 'Kiwi', 'Mango']]
lst[-1].upper
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    lst[-1].upper
AttributeError: 'list' object has no attribute 'upper'
lst[-1].Upper
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    lst[-1].Upper
AttributeError: 'list' object has no attribute 'Upper'
lst[-1] = lst.upper
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    lst[-1] = lst.upper
AttributeError: 'list' object has no attribute 'upper'
upper
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    upper
NameError: name 'upper' is not defined. Did you mean: 'super'?
lst.upper
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    lst.upper
AttributeError: 'list' object has no attribute 'upper'
a = "korea"
a.upper
<built-in method upper of str object at 0x0000020E52A483C0>
a
'korea'
a.upper()
'KOREA'
lst[-1] = lst.upper()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    lst[-1] = lst.upper()
AttributeError: 'list' object has no attribute 'upper'
lst = lst[-1].upper()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    lst = lst[-1].upper()
AttributeError: 'list' object has no attribute 'upper'
lst[-1].upper()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    lst[-1].upper()
AttributeError: 'list' object has no attribute 'upper'
lst.upper()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    lst.upper()
AttributeError: 'list' object has no attribute 'upper'
lst.upper([-1])
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    lst.upper([-1])
AttributeError: 'list' object has no attribute 'upper'
lst.upper()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    lst.upper()
AttributeError: 'list' object has no attribute 'upper'
lst[2].upper()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    lst[2].upper()
AttributeError: 'list' object has no attribute 'upper'
lst = lst[-1].upper()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    lst = lst[-1].upper()
AttributeError: 'list' object has no attribute 'upper'
lst = lst.upper([-1])
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    lst = lst.upper([-1])
AttributeError: 'list' object has no attribute 'upper'
lst.upper()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    lst.upper()
AttributeError: 'list' object has no attribute 'upper'
lst[-1][1] = lst.upper()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    lst[-1][1] = lst.upper()
AttributeError: 'list' object has no attribute 'upper'
lst[-1][1].upper()
'KIWI'
lst[-1][1] = lst[-1][1].upper()
lst
['KOREA', True, ['Apple', 'KIWI', 'Mango']]
lst[-1][1] = ["korea", "japan", "china"]
lst
['KOREA', True, ['Apple', ['korea', 'japan', 'china'], 'Mango']]
lst[-1][1][-1] = 100
lst
['KOREA', True, ['Apple', ['korea', 'japan', 100], 'Mango']]
a = [10, 20, 30, 40, 50]


a
[10, 20, 30, 40, 50]
a.append(60)
a
[10, 20, 30, 40, 50, 60]
a.append(70)
a
[10, 20, 30, 40, 50, 60, 70]
a.clear()
a
[]
a = [10,20,30,40,50]
a
[10, 20, 30, 40, 50]
a[0] = 100
b=a
b
[100, 20, 30, 40, 50]
a
[100, 20, 30, 40, 50]
b
[100, 20, 30, 40, 50]
c = 100
c
100
>>> d = c
>>> d
100
>>> c = 50
>>> d
100
>>> a
[100, 20, 30, 40, 50]
>>> b
[100, 20, 30, 40, 50]
>>> b = a.copy()
>>> b
[100, 20, 30, 40, 50]
>>> a
[100, 20, 30, 40, 50]
>>> a[0] = 200
>>> a
[200, 20, 30, 40, 50]
>>> b
[100, 20, 30, 40, 50]
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> a.count(20)
1
>>> a.count(100)
0
>>> a.count(200)
1
>>> a.append(20)
>>> a.count(20)
2
>>> dir(a)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'c', 'd', 'lst']
a
[200, 20, 30, 40, 50, 20]

========== RESTART: C:/Users/jinwoooooo/Desktop/2-1학기/자료구조/0327Mini.py =========
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}
{count}: {attr}

========== RESTART: C:/Users/jinwoooooo/Desktop/2-1학기/자료구조/0327Mini.py =========
1: __add__
1: __class__
1: __class_getitem__
1: __contains__
1: __delattr__
1: __delitem__
1: __dir__
1: __doc__
1: __eq__
1: __format__
1: __ge__
1: __getattribute__
1: __getitem__
1: __getstate__
1: __gt__
1: __hash__
1: __iadd__
1: __imul__
1: __init__
1: __init_subclass__
1: __iter__
1: __le__
1: __len__
1: __lt__
1: __mul__
1: __ne__
1: __new__
1: __reduce__
1: __reduce_ex__
1: __repr__
1: __reversed__
1: __rmul__
1: __setattr__
1: __setitem__
1: __sizeof__
1: __str__
1: __subclasshook__
1: append
1: clear
1: copy
1: count
1: extend
1: index
1: insert
1: pop
1: remove
1: reverse
1: sort

========== RESTART: C:/Users/jinwoooooo/Desktop/2-1학기/자료구조/0327Mini.py =========
1: __add__
2: __class__
3: __class_getitem__
4: __contains__
5: __delattr__
6: __delitem__
7: __dir__
8: __doc__
9: __eq__
10: __format__
11: __ge__
12: __getattribute__
13: __getitem__
14: __getstate__
15: __gt__
16: __hash__
17: __iadd__
18: __imul__
19: __init__
20: __init_subclass__
21: __iter__
22: __le__
23: __len__
24: __lt__
25: __mul__
26: __ne__
27: __new__
28: __reduce__
29: __reduce_ex__
30: __repr__
31: __reversed__
32: __rmul__
33: __setattr__
34: __setitem__
35: __sizeof__
36: __str__
37: __subclasshook__
38: append
39: clear
40: copy
41: count
42: extend
43: index
44: insert
45: pop
46: remove
47: reverse
48: sort

========== RESTART: C:/Users/jinwoooooo/Desktop/2-1학기/자료구조/0327Mini.py =========
1: __add__
2: __class__
3: __class_getitem__
4: __contains__
5: __delattr__
6: __delitem__
7: __dir__
8: __doc__
9: __eq__
10: __format__
11: __ge__
12: __getattribute__
13: __getitem__
14: __getstate__
15: __gt__
16: __hash__
17: __iadd__
18: __imul__
19: __init__
20: __init_subclass__
21: __iter__
22: __le__
23: __len__
24: __lt__
25: __mul__
26: __ne__
27: __new__
28: __reduce__
29: __reduce_ex__
30: __repr__
31: __reversed__
32: __rmul__
33: __setattr__
34: __setitem__
35: __sizeof__
36: __str__
37: __subclasshook__
38: append
39: clear
40: copy
41: count
42: extend
43: index
44: insert
45: pop
46: remove
47: reverse
48: sort
a
[]
a = [10, 20, 30, 40]
a.pop()
40
a

a.reverse()
a
[30, 20, 10]
a = [4, 2, 1, 10, 23, 123, 21, 9]
a.sort
<built-in method sort of list object at 0x000001F90CB7EB80>
a
[4, 2, 1, 10, 23, 123, 21, 9]
a
[4, 2, 1, 10, 23, 123, 21, 9]
a.sort()
a
[1, 2, 4, 9, 10, 21, 23, 123]
a.sort(reverse=True)
a
[123, 23, 21, 10, 9, 4, 2, 1]
a = (10, 20, 30)
type(a)
<class 'tuple'>
a[0]
10
a[-1]
30
a[0] = 100
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    a[0] = 100
TypeError: 'tuple' object does not support item assignment
a
(10, 20, 30)
a
(10, 20, 30)
a.append(40)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    a.append(40)
AttributeError: 'tuple' object has no attribute 'append'
a.index(20)
1
a = list(a)
a
[10, 20, 30]
a.append(40)
a
[10, 20, 30, 40]
a = tuple(a)
a
(10, 20, 30, 40)
a = {1,2,3,4,5}
b = {3,4,5,6,7}
a
{1, 2, 3, 4, 5}
b
{3, 4, 5, 6, 7}
type(a)
<class 'set'>
type(b)
<class 'set'>
a[0]
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    a[0]
TypeError: 'set' object is not subscriptable
a.intersection(b)
{3, 4, 5}
a
{1, 2, 3, 4, 5}
c = a.intersection(b)
c
{3, 4, 5}
c.add(10)
c
{10, 3, 4, 5}
c.pop()
10
c
{3, 4, 5}
c.pop()
3
c
{4, 5}
d = a.copy()
d
{1, 2, 3, 4, 5}
a.difference(b)
{1, 2}
st = {"code":202353059, "age":24, "phone":"010-7990-1021"}
st
{'code': 202353059, 'age': 24, 'phone': '010-7990-1021'}
type(st)
<class 'dict'>
st["code"]
202353059
st.pop()
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    st.pop()
TypeError: pop expected at least 1 argument, got 0
st.pop("age")
24
st
{'code': 202353059, 'phone': '010-7990-1021'}
st["age"]=24
st
{'code': 202353059, 'phone': '010-7990-1021', 'age': 24}
st.keys
<built-in method keys of dict object at 0x000001F90F3AAF00>
st.keys()
dict_keys(['code', 'phone', 'age'])
st.values()
dict_values([202353059, '010-7990-1021', 24])
st.keys()
dict_keys(['code', 'phone', 'age'])
lst = st.kes()
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    lst = st.kes()
AttributeError: 'dict' object has no attribute 'kes'. Did you mean: 'keys'?
lst
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    lst
NameError: name 'lst' is not defined. Did you mean: 'st'?
lst = st.keys()
lst
dict_keys(['code', 'phone', 'age'])
st
{'code': 202353059, 'phone': '010-7990-1021', 'age': 24}
st[lst[0]]
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    st[lst[0]]
TypeError: 'dict_keys' object is not subscriptable
lst
dict_keys(['code', 'phone', 'age'])
