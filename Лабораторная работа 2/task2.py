salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0
sum_salary = salary * months
sum_spend = 0

for i in range(months+1):
    sum_spend += spend * (1+increase)
print(sum_spend)

money_capital = round((sum_spend - sum_salary), 0)
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)