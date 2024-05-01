class Koshelek:
    system = "СБЕР"

    def __init__(self, valuta, name):
        self._balance = 0
        self.valuta = valuta
        self.name = name

    def popolnenie(self, summ_p):
        self._balance += summ_p
        print(f"{Koshelek.system}\n{self.name}: Пополнение на сумму {summ_p}. Ваш баланс {self._balance} {self.valuta}")

    def info(self):
        print(f"Ваш баланс {self._balance} {self.valuta}")

    def oplata(self, pokupka):
        if pokupka > self._balance:
            print(
                f"{Koshelek.system}\n{self.name}: На вашем счете недостаточно средств (Недостающая сумма {pokupka - self._balance} {self.valuta})")
        else:
            self._balance -= pokupka
            print(
                f"{Koshelek.system}\n{self.name}: Товар на сумму {pokupka} оплачен. Ваш баланс {self._balance} {self.valuta}")


class CryptoKoshelek(Koshelek):
    def __init__(self, name, valuta):
        super().__init__(valuta, name)
        self._coins = self._balance

    def crypto_info(self):
        print(f"{self.name}: Ваш баланс {self._coins} {self.valuta}")

    def convert(self):
        btc = 72000
        eth = 3500
        usd = 0
        if self.valuta.upper() == "BTC":
            usd = self._coins * btc
        if self.valuta.upper() == "ETH":
            usd = self._coins * eth
        print(f"{self.name}: Ваш баланс {usd} USD ({self._coins} {self.valuta})")


name = input("Введите имя кошелька: ")
not_correct = True
while not_correct:
    valuta = str(input("Укажите наименование валюты: ")).upper()
    if valuta in ['RUB', 'USD', 'EUR']:
        not_correct = False
    else:
        print("Данная валюта не обрабатывается")

new = Koshelek(valuta, name)
print("Выберите тип операции:")
print("1 - Пополнение")
print("2 - Баланс")
print("3 - Оплата")
print("4 - Перейти в криптокошелек")
print("5 - Конвертация криптовалюты (Только в криптокошельке)")

crypto = False

while True:
    op = int(input())
    if op == 1:
        summ = float(input("Сумма пополнения: "))
        new.popolnenie(summ)
    elif op == 2:
        new.info()
    elif op == 3:
        summ = float(input("Сумма оплаты: "))
        new.oplata(summ)
    elif op == 4:
        valuta_cr = input("Введите наименование криптовалюты: ").upper()
        if valuta_cr in ['BTC', 'ETH']:
            new = CryptoKoshelek(name, valuta_cr)
            crypto = True
        else:
            print("Данная валюта не обрабатывается")
    elif op == 5:
        if crypto:
            new.convert()
        else:
            print("Данная операция доступна только в криптокошельке")
