list1=["dog","cat"," "]
list2=[]
for x in list1: #работает со строкой не работает с интом
    if "c" in x:
        list2.append(x)
print(list2)
list2=[x for x in list1 if "o" in x] # выражение для элемента в списке если условие == true
print(list2)


