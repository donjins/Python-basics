def greet(name):
  print(f"heyy {name} \t this a function")

greet("john")

def add(a, b):
  return a + b

result =add(2 ,3)
print(result)

def ron(name="Greet"):
  print("hello",name)

ron()
ron("don")

def student(names , age):
  print(f"My name is {names},i am {age}")

student(age = 22, names = "Don")

def add_numbers(*args):
  print(sum(args))
  