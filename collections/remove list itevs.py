list1=[1,2,3,"cat",88," ","cat"]
list1.remove("cat") #удаляет элемент первого вхождения
print(list1) #[1, 2, 3, 88, ' ', 'cat']
list1.pop(3) #удаляет эленмент под указанным индексом
print(list1) #[1, 2, 3, ' ', 'cat']
# del list1[1] #удаляет список (на печати будет ошибка)
list1=[1,2,3,"cat",88," ","cat"]
del list1[1] #удаляет эленмент списка по индексу
print(list1) #[1, 3, 'cat', 88, ' ', 'cat']
list1.clear() #очищает указанный список
print(list1) #[]
