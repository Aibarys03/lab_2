balance = 0
currency = "usd"
def deposit(amount):
    global balance
    balance += amount
    return balance
def withdraw(amount):
    global balance
    balance -= amount
    return balance

class Operation:
 def vvod_sredstv(self):
    print("Введите количество денег которые хотите внести:")
    amount = int(input())
    deposit(amount)
    print("Теперь на вашем счету:", balance, currency)
 def vyvod_sredstv(self):
     print("Введите количество денег которые хотите получить:")
     amount = int(input())
     withdraw(amount)
     print("Теперь на вашем счету:", balance, currency)
 def valuta(self):
    print("Выберите валюту:")
    print("Нажмите 1 чтобы поменять валюту на тенге:")
    print("Нажмите 2 чтобы поменять валюту на евро:")
    print("Нажмите 3 чтобы поменять валюту на рубли:")
    print("Нажмите 4 чтобы поменять валюту на доллары:")
    val = int(input())
    if (val == 1):
        currency = "tg"
        print(476 * balance, currency)
    if (val == 2):
        currency = "eur"
        print(464 * balance, currency)
    if (val == 3):
        currency = "rub"
        print(8 * balance, currency)
    if (val == 4):
        currency = "usd"
        print(balance, currency)
c = Operation()

class Glav(Operation):
 def glavonoe_menu(self):
     print("Нажите 1 если хотите посмотреть сколько денег на вашем счету")
     print("Нажите 2 если хотите пополнить денег на вашем счету")
     print("Нажите 3 если хотите вывести деньги на вашем счету")
     print("Нажите 4 если хотите поменять валюту")
     num = int(input())
     if (num == 1):
        print("На вашем счету:",balance,currency)
     if (num == 2):
        c.vvod_sredstv()
     if (num == 3):
        c.vyvod_sredstv()
     if (num == 4):
        c.valuta()
x = Glav()
x.glavonoe_menu()
while True:
    flag = input('Вернуться в главное меню? [y/n]: ')

    if flag == 'y':
        x.glavonoe_menu()
    else:
        break
