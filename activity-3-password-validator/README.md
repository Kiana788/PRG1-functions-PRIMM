# Activity 3: Password Validator

File: `check_password_strength.py`

This is a longer function than the previous two. Read it all the way through
before predicting anything.

## Predict

For each of the four test passwords, predict the score out of 4 and which
pieces of feedback will appear.
Password	Score	Feedback
"hello"	1/4	"at least 8 characters", "uppercase letters", "numbers"
"Hello123"	4/4	nothing
"PASSWORD"	2/4	"lowercase letters", "numbers"
"MyPass123!"	4/4	nothing
Reasoning: hello is 5 chars (too short), all lowercase, no digits. PASSWORD is 8 chars so passes length, all caps so passes uppercase, but no lowercase and no digits. MyPass123! passes all four - note the ! contributes nothing; there's no special character check yet, which is exactly what Modify asks for.

## Run

Execute and compare against your predictions. Which one did you get most wrong,
and why?

## Investigate

- What does `any()` do? Describe it in one sentence without using the word "any".
 it goes through a collection and comes back True as soon as at least one item passes the test, or False if none do.

- How do `.isupper()`, `.islower()` and `.isdigit()` work?
The three string methods: char.isupper() is True only for a letter that is uppercase (so '1'.isupper() is False, not an error); .islower() same for lowercase; .isdigit() is True for the characters 0 to 9.

- Why does `"PASSWORD"` score so badly? It is a long password.
length is only one of four independent checks. Each check is a separate if, so a 40-character password of all caps still loses the lowercase and digit points. Length alone never substitutes for the other requirements.

- This function returns **two** things on one line. Find where those two values
  are picked up again further down the file.
  return score, feedback packs them into a tuple. They're picked up in score, issues = check_password_strength(pwd) - tuple unpacking, positional order matters: first returned value goes to the first variable.

## Modify

- Add a check for special characters such as `!@#$%^&*`.
- Return a rating of "Weak", "Medium" or "Strong" based on the score.
Predict step for the modification:
Scores are now out of 5, so update the /4 in the print to /5.
"hello": still 1/5, gains a special-character complaint.
"Hello123": 4/5, gains "special character" feedback, rating "Medium".
"PASSWORD": still 2/5, rating "Weak".
"MyPass123!": 5/5, rating "Strong" - this is the only one the ! now earns a point for.