money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

month=0

while money_capital >= spend:
    money_capital += salary
    money_capital -= spend
    money_capital = money_capital * (1 + increase)
    spend = spend * (1 + increase)
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)