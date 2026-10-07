# Activity 6: Scope

File: `scope.py`

Two short experiments about which names are visible where.

## Predict

Write down all four lines of output before running anything. Be specific: for
each one, say whether it will be `5`, `10`, `inside` or `outside`.
5
10
inside
outside

## Run

Execute it.

## Investigate

- `double_it(value)` clearly doubles something, and yet `value` is still 5
  afterwards. What exactly did the function receive?
  double_it(value) received the value 5, not the name value. Inside the function, that 5 got copied into a fresh box called number (a completely separate variable that just happens to be a parameter). Doubling it changes only that new box. value never hears about it. Numbers, strings, and booleans are passed this way in Python, so the original is always safe.
  
- Inside `show_message` there is a line `message = "inside"`. After the function
  has run, the outer `message` is unchanged. Explain that to your partner
  without using the word "scope".
  Explaining it without the word "scope": inside the function, the name message is a brand new piece of paper that lives only for the duration of that function. Writing message = "inside" on that paper doesn't touch the different piece of paper with message = "outside written on it in the main part of the file. When the function finishes, its paper is thrown away, and the outer one is still sitting there untouched. Two same-named papers in different rooms.

- If you delete the line `message = "inside"` from inside the function, what do
  you think `show_message()` will print? Predict, then try it.
  If you delete message = "inside", then show_message() will look for a name it can't find locally, and Python will find the outer message = "outside" instead. So it prints outside. This is called "reading from an outer name," and it works, but it's usually considered a code smell because the function's behavior now depends on some name far away in the file.

## Modify

- Change `show_message` so that it takes the message as a parameter instead of
  using a name from outside the function. Which version would you rather be
  handed to maintain, and why?
The parameter version is far better to maintain:

The function is self-contained: everything it needs is visible in one line, its signature. You never have to go hunting through the file to find out what mysterious global name it depends on.
It's reusable: show_message("outside"), show_message("hello"), show_message("error!") all work with zero changes.
It's predictable: no risk that someone renaming or deleting the outer message silently breaks the function.
The original version only ever prints one thing, and its correctness hinges on a variable defined far away that could be changed or deleted at any moment by anyone. A function that takes its inputs as parameters is the standard, and honestly the only sane, way to write maintainable code.