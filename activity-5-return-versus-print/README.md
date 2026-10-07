# Activity 5: Return versus Print

File: `return_versus_print.py`

Two functions that look almost identical and behave completely differently. This
one catches nearly everybody, so predict carefully.

## Predict

- How many lines of output will this file produce?
That's 5 lines 5, 15, None, 15, 50
- Write down what each line will say, in order.5, 15, None, 15, 50
- What will `first` hold? What will `second` hold?
first holds None
second holds 15

## Run

Execute it. Most pairs get the number of lines wrong before they get the content
wrong.

## Investigate

- `add_and_print(2, 3)` produced output. `add_and_return(2, 3)` on the next line
  did not. Why not? The calculation still happened.
  add_and_print(2, 3) prints because printing is done inside the function. add_and_return(2, 3) on a bare line computes 5 and hands it back... to nobody. The value is simply discarded. The calculation happened; the result evaporated.

- Why does `print(first)` show `None`? Where did `None` come from, given that
  the word `None` appears nowhere in the file?
print(first) shows None because a function that never hits a return statement implicitly returns the special value None. Python inserts it invisibly - the word never appears in your file, but it's what every return-less function hands back.

- The last line multiplies a function call by 10 and it works. Try doing the
  same thing with `add_and_print`. What happens, and why?
  The last line works with add_and_return because it gives back a number you can multiply. With add_and_print you'd get TypeError: unsupported operand type(s) for *: 'NoneType' and 'int' - you'd be trying to multiply None by 10, and None is not a number. print is an action (show text on screen), not a value.

## Modify

- Change `add_and_print` so that the last line of the file would work with it
  too. What did you have to add?

> Almost every function you meet from here on returns rather than prints.
> Printing is how a program talks to a person. Returning is how one piece of a
> program talks to another.
function both shows the answer and hands the value back, so add_and_print(2, 3) * 10 works.