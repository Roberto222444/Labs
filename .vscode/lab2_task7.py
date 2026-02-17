x = int(input("Введіть число:"))
hundred = x // 100
ten = (x // 10) % 10
unit = x % 10 
y = (unit * 100) + (ten * 10) + hundred
print ("Число:", x)
print ("Дзеркальне число:", y)