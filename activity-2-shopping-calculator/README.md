# Activity 2: Shopping Calculator

File: `shopping_calculator.py`

## Predict

What will each of the three `print` statements show? Pay close attention to how
many arguments each call actually supplies.
Call	Prediction
calculate_total(100)	£120.00 (tax_rate defaults to 0.20, discount defaults to 0)
calculate_total(100, 0.1)	£110.00 (0.1 goes into tax_rate, discount still 0)
calculate_total(100, 0.08, 10)	£97.20 (subtotal 90, tax 7.20)

## Run

Execute the file and check your predictions.

## Investigate

- What is `tax_rate=0.20` doing in the function definition? How is it different
  from `price`?
tax_rate=0.20 in the definition is a default value. If the caller supplies nothing for that position, tax_rate becomes 0.20. price has no default, so it's required - the call fails without it.

- The second call passes only two values. Which parameter received `0.1`, and
  how do you know?
  tax_rate, because arguments match parameters by position: first argument → price, second → tax_rate. discount keeps its default of 0. You can prove it: the output is £110.00, which is exactly 100 + 10% tax. If 0.1 had gone into discount you'd get a different number.

- What happens if you do not supply a discount at all?
No discount supplied: discount stays at 0, so subtotal = price - 0 = full price. Nothing crashes; the default just quietly applies.

- What does `:.2f` do in the `print` statements? Remove it and see.
:.2f is a format spec: show the number as a float with exactly 2 decimal places (and rounds). Remove it and you get raw floats like £120.0 and £97.20000000000002 - floating point noise appears. Good demonstration that formatting hides ugly values.

## Modify

- Add a `tip` parameter with a default of 12%, and work it into the total.
- Predict the new output for all three existing calls before you run it. Two of
  them should change. Do they?
  calculate_total(100)=£132.00 (120 + 12 tip)
  calculate_total(100, 0.1)= £122.00 (110 + 12 tip)
  calculate_total(100, 0.08, 10)= £107.80 (97.20 + 10.80 tip)

## Make (stretch)

Optional. Only if you have finished everything above.

- Write a weighted final grade calculator. The final grade is 30% homework plus
  70% test:

  `final_grade = (homework_score * 0.30) + (test_score * 0.70)`

  Use default parameters for the two weights, so the function still works if the
  course weighting changes later.
