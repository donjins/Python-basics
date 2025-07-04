def greet(name, age):
  print(f"my name is {name},i am {age}")

greet(age=22 , name="don")

def addnumber(*args):
  return sum(args)


print(addnumber(2,3,5))


def show_info(**kwargs):
    print(kwargs)

show_info(name="john", age=25)

def factorial(n):
   if n == 1:
      return 1
   return n * factorial( n - 1)

print(factorial(5))

#recursion

def countozero(n):
   if n == 0:
      print("Done")
   else:
      print(n)
      countozero(n-1)

countozero(5)

def factorials(m):
   if m == 1:
      return 1
   else:
      return m * factorials(m - 1)
factorials(5)

def sum(o):
  if o == 1:
     return 1
  else:
     return o + sum( o - 1 )
print(sum(5))


def printnum(p):
   if p == 0:
      return
   printnum(p - 1)
   print(p, end='')
printnum(10)

def power(x , y):
   if y == 0:
      return 1
   return x * power(x , y -1)
print(power(2,3))

def reverse(s):
    if s == "":
        return ""
    return reverse(s[1:]) + s[0]

print(reverse("hello"))

