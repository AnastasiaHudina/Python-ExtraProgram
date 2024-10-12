money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

n = 0  # счётчик месяцев
while True:

    if n != 0:  # тк в 1ый месяц увеличения трат на 5% нет -> проверяем условие
        spend = spend + (increase * spend)  # увеличение трат на 5%

    money_capital += salary  # начисление зарплаты

    if spend > money_capital:  # если траты превысили бюджет текущего месяца
        break
    else:
        n += 1  # если траты не превысили -> увеличиваем кол-во успешно прожитых месяцев на один

    money_capital -= spend  # заплатили за месяц

print("Количество месяцев, которое можно протянуть без долгов:", n)