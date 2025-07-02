s = set([1,2,3])
print(s)

se = {1,2}
se.add(3)
se.remove(3)
print(se)


a = {1,2,3}
b = {3,4,5}

print(a|b) #union all elements without repeat
print(a&b) #intrsection means common element
print(a-b)
print(a^b) #symetric - common remove add other print

a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))
print(b.issuperset(a))
print(a.isdisjoint({5, 6})) 

colors = {"red", "blue", "green"}
for color in colors:
    print(color)

num = [1,2,3,4,3,4,5]
uniq= list(set(num))
print(uniq)

fs = frozenset([1, 2, 2, 3])
print(fs)  # frozenset({1, 2, 3})

combo = {
    frozenset(["apple", "banana"]): "fruit combo",
    frozenset(["carrot", "beet"]): "veggie combo"
}

print(combo[frozenset(["banana", "apple"])])  # fruit combo
fs = frozenset([1, 2, 3, 1, 2])
print(len(fs))
