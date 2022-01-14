# light = 'zxc'
# if light == 'green':
#     print("GO")
# elif light == 'yellow':
#     print("Wait")
# elif light == 'red':
#     print("Stop")
# else:
#     print("What?")

age = int(input("Сколько вам лет? "))

count = ''
if 18 - age == 1:
    count = 'год'
elif 18 - age == 2 or 18 - age == 3 or 18 - age == 4:
    count = 'года'
else:
    count = 'лет'

if age >= 18:
    print("Добро пожаловать")
else:
    print(f"Вход доступен только для лиц возрастов 18 лет и старше, вам не хватает {18-age} {count}")
