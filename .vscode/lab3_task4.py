x = int(input('Введіть одне чотиризначне число :'))
a = x // 1000
b = (x // 100) % 10
c = (x // 10) % 10
d = x % 10 
sum1 = a + b
sum2 = c + d
is_lucky = sum1 == sum2
print("Число щасливе:", is_lucky)