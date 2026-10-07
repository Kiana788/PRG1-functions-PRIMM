# Stage 1: original
def calculate_total(price, tax_rate=0.20, discount=0):
    subtotal = price - discount
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total

print(f"£{calculate_total(100):.2f}") #£120.00
print(f"£{calculate_total(100, 0.1):.2f}") #£110.00
print(f"£{calculate_total(100, 0.08, 10):.2f}") #£97.20

# Stage 2: Modify - added tip parameter
def calculate_total(price, tax_rate=0.20, discount=0, tip=0.12):
    subtotal = price - discount
    tax = subtotal * tax_rate
    total = subtotal + tax + (subtotal * tip)
    return total

print(f"£{calculate_total(100):.2f}")     # £132.00
print(f"£{calculate_total(100, 0.1):.2f}") # £122.00
print(f"£{calculate_total(100, 0.08, 10):.2f}") # £107.80

# Make: weighted grade calculator
def final_grade(homework_score, test_score, homework_weight=0.30, test_weight=0.70):
    grade = (homework_score * homework_weight) + (test_score * test_weight)
    return grade

print(f"{final_grade(80, 90):.1f}")     # 87.0
print(f"{final_grade(80, 90, 0.5, 0.5):.1f}")  # 85.0
