# Activity 4: Functions Calling Functions

File: `payslip.py`

Up to now each function has stood on its own. Here one function is built out of
two others.

## Predict

What will each of the three `print` statements output? Work out the third one on
paper before you run anything.
Predict
Call	Output
calculate_gross_pay(38, 12.50)	475.0
calculate_tax(475.00)	95.0
calculate_take_home(38, 12.50)	380.0
The third one on paper: gross = 38 × 12.50 = 475.00. Tax = 475 × 0.20 = 95.00. Take-home = 475 − 95 = 380.0.

## Run

Execute and compare.

## Investigate

- When you call `calculate_take_home` once, how many function calls happen in
  total? Trace it with your partner.
  3 in total - the calculate_take_home call itself, then it calls calculate_gross_pay once, then calculate_tax once. A trace: main → calculate_take_home → calculate_gross_pay (returns 475.0) → calculate_tax (returns 95.0) → back in calculate_take_home, subtract, return 380.0.

- Which function does the multiplication by the hourly rate? Which one knows
  about tax? Neither of them knows about both. Why is that a good thing?
calculate_gross_pay multiplies hours by rate. calculate_tax knows tax. Neither knows both - calculate_gross_pay has no idea tax exists, and calculate_tax doesn't know the pay came from hours × rate. It's a good thing because each function does one job and can be tested, replaced, or reused in isolation (for example calculate_tax works identically on a monthly salary).

- `TAX_RATE` is written in capitals and sits outside every function. What is
  that telling you?
  a constant. The convention says "this value is fixed configuration, don't reassign it". Because it sits at module level, every function can see it without it being passed in.

- What would break if you changed the order of the two lines inside
  `calculate_take_home`?
  tax = calculate_tax(gross_pay) would run before gross_pay exists, so you'd get a NameError (or UnboundLocalError depending on how you ordered it). Order of assignment matters when a later line consumes an earlier variable.

## Modify

- Add a pension deduction of 5% of gross pay, as its own function, and work it
  into the take-home figure.
- Predict the new take-home for 38 hours at £12.50 before you run it.

## Make (stretch)

Optional. Only if you have finished everything above.

- Write `calculate_overtime_pay`, where any hours beyond 37 are paid at 1.5
  times the normal rate, and use it inside a new take-home calculation.
 38 hours at £12.50: normal pay = 37 × 12.50 = 462.50, overtime = 1 × 12.50 × 1.5 = 18.75, gross = 481.25, tax = 96.25, pension = 24.0625, take-home = 360.9375 (floats, so it prints with full noise unless format with :.2f). overtime changes the gross, and because tax and pension are computed from gross, all three deductions shift together that's the payoff of functions built out of functions.