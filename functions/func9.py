def even(n):
   for i in range(2,n+1,2):
      yield i
   

for j in even(10):
   print(j)


