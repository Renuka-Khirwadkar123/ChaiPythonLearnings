# username="chaicode" #global scope<outside ghar>

# def name():
#     username="chai" #local scope <inside ghar>
#     print(username)

# print(username)
# name()


# x=99

#def func(y):
   # z=x+y
  #  return z

#print(func(1))


#global inside function-bad practice code

# def func3():
#     global x
#     x=100


# func3()
# print(x)

#closure
# def fun1():
#     x=88
#     def func2():
#         print(x)
#     return func2 #returning definition of fun1()

# result=fun1() 
# result()

def s(num):
    def squ(n):
      return n**num
    return squ

result1=s(2)
result=s(3)

print(result1(3))
print(result(2))
