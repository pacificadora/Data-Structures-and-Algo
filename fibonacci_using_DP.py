#fibonacci using memoization
def fibonacci(n):
  a=0
  b=1
  if n<=1:
    return n
  else:
    c=a+b
    a=b
    b=c
  return b
  
  n=int(input())
  res = fibonacci(n)
  print(n)

  
 


