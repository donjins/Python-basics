if 7 % 2 == 0:
  print("even")
else:
  print("Odd")


# numb = [10, 25 ,15 ]
# b = numb[0]
# for num in numb:
#  if numb[num] > b:
#   print(b)


quest = int(input(" enter the year"))

if quest % 400 == 0:
  print("leap year")
elif quest % 100 == 0:
  print("Leap year")
elif quest % 4 ==0:
  print("leap year")
else:
  print("not leep year")


secretnumber = 6
chance = 0
while chance < 3:
  val = int(input("enter the number?"))
  print(val)
  if secretnumber == val:
    print("Sucess")
    break
  else:
    print("try again")
  chance += 1


passw = "admin123"
i = 0
while 1 < 5:
  valu = input(" enter the password")
  if passw == valu:

    print("login successfull")
    break
  else:
    print("try again")
  i += 1
print("chance is over")


for x in range(20):
  if x % 3 == 0:
    continue
  print(x)
