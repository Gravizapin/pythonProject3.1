a = int(input('Введите делимое число :'))
d = int(input('Введите число делитель :'))
try:
    if d == 0:
        print('На ноль делить нельзя')

    else:
        def m_func (x,y):
            return x / y
    print(f"Результат деления = {m_func(a,d)}")
except NameError:
    print('Никогда!')