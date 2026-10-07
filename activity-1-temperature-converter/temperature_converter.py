def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Predict: what will this print?
print(celsius_to_fahrenheit(0))     # 32.0
print(celsius_to_fahrenheit(100))   # 212.0
print(fahrenheit_to_celsius(32))    # 0.0
print(fahrenheit_to_celsius(212))   # 100.0

# Make: your own converter
temp = float(input("Enter a temperature: "))
unit = input("Is it (C)elsius or (F)ahrenheit? ")
if unit.upper() == "C":
    print(f"{temp}°C = {celsius_to_fahrenheit(temp)}°F")
else:
    print(f"{temp}°F = {fahrenheit_to_celsius(temp)}°C")
