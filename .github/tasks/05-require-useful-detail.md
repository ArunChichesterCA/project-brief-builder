# Task 5: Feature: require useful detail
**Goal:** stop people submitting briefs that are too vague, and add a test that proves it works.

**Start a branch**
1. Make sure you're up to date: `git switch main`, then `git pull`
2. `git switch -c minimum-detail-validation`

**Change the code**
3. Open `validation.py`. Delete everything in it and paste this in:

```python
REQUIRED_FIELDS = {
    "title": "Project title",
    "problem": "Problem to solve",
    "users": "Intended users",
    "outcome": "Desired outcome",
    "essential_features": "Essential features",
    "out_of_scope": "Out of scope",
    "constraints": "Constraints",
    "acceptance_criteria": "Acceptance criteria",
}

MINIMUM_LENGTHS = {
    "problem": 20,
    "users": 10,
    "outcome": 20,
}


def validate_brief(brief_data):
    """Return a list of clear validation messages."""
    problems = []
    for field, label in REQUIRED_FIELDS.items():
        if not brief_data.get(field, "").strip():
            problems.append(f"{label} is required.")
    for field, minimum in MINIMUM_LENGTHS.items():
        value = brief_data.get(field, "").strip()
        if value and len(value) < minimum:
            label = REQUIRED_FIELDS[field]
            problems.append(f"{label} needs more detail (at least {minimum} characters).")
    return problems
```

**Add a test**
4. Open `tests/test_validation.py`. Find the line `if __name__ == "__main__":`
5. Just **above** it, paste this. Keep the four spaces at the start of each line:

```python
    def test_short_problem_needs_more_detail(self):
        messages = validate_brief({"problem": "Too vague"})
        self.assertIn(
            "Problem to solve needs more detail (at least 20 characters).",
            messages,
        )
```

6. Save both files and run the tests.
   *Check: `Ran 7 tests` and `OK`.*

**Commit, pull request, review, merge**
7. `git add validation.py tests/test_validation.py`
8. `git commit -m "Require useful detail in key fields"`
9. `git push -u origin minimum-detail-validation`
10. Open a pull request into **main**. Title: `Require useful detail in key fields`
11. Description: first line `Closes #5`. Then answer, in your own words: what does the new code check, and what does someone see if they type "Too vague" as the problem?
12. Ask your partner for one comment, and reply. Merge only when **Tests** has a green tick.
13. `git switch main`, then `git pull`

**Done looks like**
- [ ] Pull request merged with a green **Tests** tick, and 7 tests passing
- [ ] Your explanation in the pull request description
- [ ] A comment from your partner, and your reply
