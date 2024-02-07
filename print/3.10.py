k=input("ввести число от 1 до 365:")
w=7 # количество дней в неделе
n=int(k)%w
if int(n)==1:
    print("пн")
elif int(n)==2:
    print("вт")
elif int(n) == 3:
    print("ср")
elif int(n) == 4:
    print("чт")
elif int(n) == 5:
    print("пт")
elif int(n) == 6:
    print("сб")
elif int(n) == 0:
    print("вс")



