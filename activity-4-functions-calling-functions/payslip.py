TAX_RATE = 0.20


def calculate_gross_pay(hours_worked, hourly_rate):
    return hours_worked * hourly_rate


def calculate_tax(gross_pay):
    return gross_pay * TAX_RATE


def calculate_take_home(hours_worked, hourly_rate):
    gross_pay = calculate_gross_pay(hours_worked, hourly_rate)
    tax = calculate_tax(gross_pay)
    return gross_pay - tax


print(calculate_gross_pay(38, 12.50))
print(calculate_tax(475.00))
print(calculate_take_home(38, 12.50))
TAX_RATE = 0.20
PENSION_RATE = 0.05


def calculate_gross_pay(hours_worked, hourly_rate):
    return hours_worked * hourly_rate


def calculate_tax(gross_pay):
    return gross_pay * TAX_RATE


def calculate_pension(gross_pay):
    return gross_pay * PENSION_RATE


def calculate_take_home(hours_worked, hourly_rate):
    gross_pay = calculate_gross_pay(hours_worked, hourly_rate)
    tax = calculate_tax(gross_pay)
    pension = calculate_pension(gross_pay)
    return gross_pay - tax - pension


print(calculate_gross_pay(38, 12.50))
print(calculate_tax(475.00))
print(calculate_take_home(38, 12.50))

NORMAL_HOURS = 37


def calculate_overtime_pay(hours_worked, hourly_rate):
    if hours_worked &lt;= NORMAL_HOURS:
        return 0
    overtime_hours = hours_worked - NORMAL_HOURS
    return overtime_hours * hourly_rate * 1.5


def calculate_take_home_with_overtime(hours_worked, hourly_rate):
    normal_pay = min(hours_worked, NORMAL_HOURS) * hourly_rate
    overtime_pay = calculate_overtime_pay(hours_worked, hourly_rate)
    gross_pay = normal_pay + overtime_pay
    tax = calculate_tax(gross_pay)
    pension = calculate_pension(gross_pay)
    return gross_pay - tax - pension


print(calculate_take_home_with_overtime(38, 12.50))
