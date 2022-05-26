money = input("Введите сумму, руб:")
money = float(money)
per_cent = {"ТКБ": 5.6, "СКБ": 5.9, "ВТБ": 4.28, "СБЕР": 4.0}
deposit = []
for i in per_cent.keys():
    a = per_cent[i]
    deposit.append(money * a/100)
print("deposit", "-", deposit)
print("Максимальная сумма прибыли, руб: - {}".format(max(deposit)))