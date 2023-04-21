list1 = []
for x in range(20):
    list1.append(x + 1)
print(list1)

list2 = []
for x in list1:
    list2.append(x * x)

print(list2)

list3 = []
for x in list1:
    if x % 2 == 0:
        list3.append(x)
print(list3)