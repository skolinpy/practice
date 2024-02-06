list1=[1,2,5,"dog",88]
list2=["cat",77," ",18]
tuple1=("bird",2020)
list1.append(99) #добавление элемента в конец списка
print(list1) #[1, 2, 5, 'dog', 88, 99]
list1.insert(2,55) #вставить элемент в индекс 2
print(list1) #[1, 2, 55, 5, 'dog', 88, 99]
print(type(list2[2])) #<class 'str'>
list1.extend(list2) #добавили список 2 к списку 1
print(list1) #[1, 2, 55, 5, 'dog', 88, 99, 'cat', 77, ' ', 18]
list1.extend(tuple1) #добавили кортеж1 к списку 1
print(list1) #[1, 2, 55, 5, 'dog', 88, 99, 'cat', 77, ' ', 18, 'bird', 2020]



