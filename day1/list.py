fruits = ["apple","orange","grape"]
print(fruits[1])
print(fruits[-1])
fruits[1] = "banana"
print(fruits[1])
fruits.append("pineapple")
fruits.insert(1,"pineapple")
fruits.remove("grape")
fruits.pop()
del fruits[2 ]
for fruit in fruits:
    print(fruit)
fruits.append("banana")
# print(fruits)
print(len(fruits))  # Number of items
if "banana" in fruits:
    print("Yes, banana is there")
number = [0,1,2,3,4,5]
print(number[1:4])
present = ["edwin","rose","joseph"]
if "Don" not in present:
    present.append("Don")
    print(present)


favoratefood = ["biriyani","mandi","rice","shake","pufs"]
favoratefood[2] = "pizza"
favoratefood.append("icecream")
print(favoratefood)

num = [1,5,9,6,5]
num.sort()
num.reverse()
print(num)


evennumber = [ ]
even = [1,6,7,4,9,8]
for eve in even:
    if eve % 2 ==0:
        evennumber.append(eve)
print(evennumber)