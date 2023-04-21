list1 = []
for x in range(20):
    list1.append(x + 1)
print(list1)

list2 = []
for x in list1:
    list2.append(x * x)

print(list2)
