# PRG1: Functions (PRIM activities)

Day 2 morning. Seven activities, each in its own folder, each with the code and
its tasks together in one place.

## PRIM

Every activity follows the same four steps, in this order:

| Step | What you do |
|---|---|
| **Predict** | Say what the code will do **before** you run it. Write it down. |
| **Run** | Run it. Compare against your prediction. |
| **Investigate** | Work out *why* it behaves that way. |
| **Modify** | Change something specific, predicting the effect before each change. |

The first three steps are the point. Getting a prediction wrong and working out
why is worth more than getting it right, and far more than skipping ahead to
writing code. Most of what you will do professionally is read code, work out
what it does, and change it without breaking it. That is what these four steps
rehearse.

Activities 2 and 4 carry an optional **Make** at the end, and activity 7 ends
with an optional fault swap. All three are stretch: reach them only once you
have finished everything else in that folder. They are the only places in this
session where you write something from nothing.

## How to work through these

Work in pairs. One of you drives, the other questions and challenges, then swap
at each new activity.

You are **not** expected to finish all seven. Depending on your experience you
might spend the whole session on the first two or three. **That is fine.** What
is not fine is running the code before predicting, or reaching Modify without
being able to explain what the original did.

## The activities

| Folder | Focus |
|---|---|
| `activity-1-temperature-converter/` | A single function: parameters, return, one calculation |
| `activity-2-shopping-calculator/` | Default parameters, and what happens when you leave one out |
| `activity-3-password-validator/` | A longer function with several decisions inside it |
| `activity-4-functions-calling-functions/` | Functions built out of other functions |
| `activity-5-return-versus-print/` | The difference between showing a value and handing it back |
| `activity-6-scope/` | Which names are visible where, and what a parameter actually receives |
| `activity-7-broken-functions/` | Three faults to find in code that runs perfectly happily |

Activity 7 is the one to reach if you can. Finding a fault in code that does not
crash is the skill the whole module is built around.

## Running a file

Open the repository in a Codespace, then in the terminal:

```
python activity-1-temperature-converter/temperature_converter.py
```

If `python` is not recognised, use `python3` instead.

Activity 5 (return versus print): prediction, the None explanation, and the fix (add return a + b)
Activity 6 (scope): why value stays 5, the "two papers in different rooms" explanation, and the parameterized version of show_message
Activity 7 (broken functions): the three faults identified (None from the missing return, the wrong subtraction in apply_discount, and the swapped arguments in the call) plus the fixed file producing 20, 60.0, and 25.0
