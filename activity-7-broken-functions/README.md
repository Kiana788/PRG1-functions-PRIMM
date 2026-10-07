# Activity 7: Broken Functions

File: `broken_functions.py`

Three things in this file are wrong. None of them crash. The code runs, prints
three results, and two of those results are simply incorrect while the third is
not a result at all.

This is what most real faults look like. Code that crashes tells you where to
look. Code that quietly returns the wrong number does not.

## Predict

Read all three functions and the three calls at the bottom. For each call, work
out on paper what the answer **should** be:

- The area of a 4 by 5 rectangle
- £80 with 25% off
- 50 as a percentage of 200
Predictions:
Area of a 4 by 5 rectangle: 20
£80 with 25% off: 60 (i.e. 60.0)
50 as a percentage of 200: 25.0
what i actually got:
None
55.0
25.0


## Run

Execute the file. Compare what you got with what you expected.

## Investigate

For each of the three, work out what went wrong. Be precise: name the line and
say what it does versus what it was meant to do.

Two useful questions:

- One of the outputs is `None`. What does that tell you about the function that
  produced it?
- One of the faults is **not inside a function at all**. Which one, and what
  does that tell you about where faults can live?

  1. calculate_area - the missing return
Line: area = length * width
What it does: computes the area, stores it in a local variable, and then the function ends without a return statement. Python hands back None invisibly.
What it was meant to do: return area
This is the fault that produces None. The message: the function never finished its job of handing back a value. The work happened and was thrown away.
2. apply_discount - the bug that isn't where you'd look
Line: return price - discount_percent
What it does: subtracts 25 (the raw percentage) from 80, giving 55.0.
What it was meant to do: subtract the calculated reduction: return price - reduction. Note the function even computes reduction correctly on the line above, and then never uses it. This is the cruelest kind of fault: the correct variable exists, is correct, and is simply ignored on the crucial line.
3. convert_to_percentage - the fault that's not in a function at all
1. calculate_area - the missing return
Line: area = length * width
What it does: computes the area, stores it in a local variable, and then the function ends without a return statement. Python hands back None invisibly.
What it was meant to do: return area
This is the fault that produces None. The message: the function never finished its job of handing back a value. The work happened and was thrown away.
2. apply_discount - the bug that isn't where you'd look
Line: return price - discount_percent
What it does: subtracts 25 (the raw percentage) from 80, giving 55.0.
What it was meant to do: subtract the calculated reduction: return price - reduction. Note the function even computes reduction correctly on the line above, and then never uses it. This is the cruelest kind of fault: the correct variable exists, is correct, and is simply ignored on the crucial line.
3. convert_to_percentage - the fault that's not in a function at all
The function is completely correct: (part / whole) * 100 = (200 / 50) * 100 = 400.0... wait, no. Let's recheck. 200 / 50 = 4.0, so the function returns 400.0. Hmm, so the output would actually be 400.0, not 25.0.
Actually re-reading the call: convert_to_percentage(200, 50) - the call is wrong. The person wanted "50 as a percentage of 200" but passed the arguments the wrong way round: part is 200 and whole is 50. The function itself is fine; the call at the bottom is the fault. This teaches the important lesson: faults can live outside the functions, in the arguments you pass. The function is innocent; the caller is confused.
So the actual three outputs are:
None
55.0
400.0

## Fault log

Fill this in with your partner. You will do exactly this, marked, in Task 2.

| # | What you saw | What was wrong | How you fixed it |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
#	What you saw	What was wrong	How you fixed it
1	None|	calculate_area computes area but has no return statement, so Python returns None|	Add return area as the last line of the function
2	55.0|	apply_discount subtracts the raw discount_percent (25) instead of the computed reduction|	Change the return to return price - reduction
3	400.0|The function is correct; the call passes the arguments in the wrong order: part=200, whole=50| Change the call to convert_to_percentage(50, 200)

## Modify

Fix all three. Run it again. You should get `20`, `60.0` and `25.0`.

## Stretch: swap faults

Optional, and worth reaching if you can.

Write a function with a deliberate fault of your own, of a kind not used here,
and swap with another pair. Can they find it? Can you find theirs? Planting a
fault that survives someone else's reading is harder than it sounds, and it
teaches you a great deal about where your own attention goes when you read.

Faults that survive a quick read tend to be ones that look plausible at a glance:
A function that returns the right shape of value but slightly wrong formula, e.g. return (f - 32) * 5 / 4 instead of * 5 / 9 for Celsius.
An off-by-one: for i in range(1, len(items)) skipping the first item.
Using &lt;= where &lt; was needed.
A correct-looking call that passes arguments in a subtly wrong order, like the percentage one above.
Shadowing a parameter with a local variable that then gets returned.
The best planted faults are the ones that still produce a plausible-looking number, not None or a crash.