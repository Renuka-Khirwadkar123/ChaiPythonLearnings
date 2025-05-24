>>> f=open(script.py)
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    f=open(script.py)
           ^^^^^^
NameError: name 'script' is not defined
>>> ls
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    ls
NameError: name 'ls' is not defined
>>> print("Hello")
Hello
>>> f=open('script.py')
>>> f.readline()
'import time\n'
>>> f.readline()
'print("Hello World")\n'
>>> f.readline()
>>> f=open('script.py')
>>> f.readline()
'import time\n'
>>> f.readline()
'print("Hello World")\n'
>>> f.readline()
>>> f.readline()
'import time\n'
>>> f.readline()
'print("Hello World")\n'
>>> f.readline()
'import time\n'
>>> f.readline()
'print("Hello World")\n'
>>> f.readline()
>>> f.readline()
'print("Hello World")\n'
>>> f.readline()
>>> f.readline()
'lst=[1,2,3,4,5]\n'
'lst=[1,2,3,4,5]\n'
>>> f.readline()
>>> f.readline()
'username="Renuka"\n'
>>> f.readline()
>>> f=open("script.py")
>>> f.readline()
'import time\n'
>>> f.readline()
'print("Hello World")\n'
>>> f.readline()
'lst=[1,2,3,4,5]\n'
>>> f.readline()
'username="Renuka"\n'
>>> f.readline()
'print(username)'
>>> f.readline()
''
>>> f.readline()
''
>>> f.readline()
''
>>> f.__next()__
  File "<python-input-27>", line 1
    f.__next()__
              ^^
SyntaxError: invalid syntax
>>> f.__next()__()
  File "<python-input-28>", line 1
    f.__next()__()
              ^^
SyntaxError: invalid syntax
>>> f.__next__()
Traceback (most recent call last):
  File "<python-input-29>", line 1, in <module>
    f.__next__()
    ~~~~~~~~~~^^
StopIteration
>>> for line in open("script.txt"):
...     print(line,end='')
... 
Traceback (most recent call last):
  File "<python-input-30>", line 1, in <module>
    for line in open("script.txt"):
                ~~~~^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'script.txt'
>>> for line in open("script.py"):                                                     
...     print(line,end='')
...     
import time
print("Hello World")
lst=[1,2,3,4,5]
username="Renuka"
>>> t(username)
>>> 
>>> 
>>> f=open("script.py")
>>> while True:
...     line=f.readline()
...     if not line: break
...     print(line,end='')
... 
import time
print("Hello World")
lst=[1,2,3,4,5]
username="Renuka"
>>> t(username)
>>> test="Hitesh"
>>> mylist=[1,2,3]
>>> I=iter(mylist)
>>> I
<list_iterator object at 0x000001CBBAE22710>
>>> f=open("script.py")
>>> I=iter(f)
>>> I
<_io.TextIOWrapper name='script.py' mode='r' encoding='cp1252'>
>>> iter(f) is f
True
>>> f.__iter__() is f
True
>>> iter(mylist) is mylist
False
>>> d={'a':1,'b':2}
>>> for k in d.keys():
...     print(k)
...     
a
b
>>> I=iter(d)
>>> I
<dict_keyiterator object at 0x000001CBBAE067F0>
>>> next(I)
'a'
>>> next(I)
'b'
>>> next(I)
Traceback (most recent call last):
  File "<python-input-61>", line 1, in <module>
    next(I)
    ~~~~^^^
StopIteration