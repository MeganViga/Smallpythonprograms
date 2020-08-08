list1 = [1,1,'viganesh','sugadev','viganesh',2.5, 2.5]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)