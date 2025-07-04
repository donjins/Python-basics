def greet(name, age):
  print(f"my name is {name},i am {age}")

greet(age=22 , name="don")

def addnumber(*args):
  return sum(args)


print(addnumber(2,3,5))


def show_info(**kwargs):
    print(kwargs)

show_info(name="john", age=25)

\
