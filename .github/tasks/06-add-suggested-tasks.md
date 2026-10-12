# Task 6: Feature: add a "Suggested tasks" section
**Goal:** add a new box to the form, make it required, and show it in the brief. This change touches four files, so take it one step at a time.

**Start a branch**
1. `git switch main`, then `git pull`
2. `git switch -c project-tasks`

**1. The form: `app.py`**
3. Find the line `acceptance_criteria = st.text_area(`. Just **above** it, add this line (4 spaces at the start):
   `    project_tasks = st.text_area("Suggested tasks (one per line)")`
4. Further down, find `"acceptance_criteria": acceptance_criteria,`. Just **above** it, add (8 spaces at the start):
   `        "project_tasks": project_tasks,`

**2. The check: `validation.py`**
5. Inside `REQUIRED_FIELDS`, just **above** the `"acceptance_criteria"` line, add (4 spaces):
   `    "project_tasks": "Suggested tasks",`

**3. The brief: `brief_generator.py`**
6. Find `## Acceptance criteria`. Just **above** it, add these three lines, then a blank line:

```
## Suggested tasks

{as_bullets(data['project_tasks'])}
```

**4. The tests**
7. Run the tests now. *Check: some FAIL. That's expected: the pretend forms in the tests don't have the new box yet.*
8. In `tests/test_validation.py`, find `"acceptance_criteria": "Three sample rooms appear",`. Just **above** it add:
   `            "project_tasks": "Build the first feature",`
9. In `tests/test_brief_generator.py`, find `"acceptance_criteria": "The feature works",`. Just **above** it add the same line:
   `            "project_tasks": "Build the first feature",`
10. In the same file, replace the line `self.assertTrue(generate_brief(data).startswith("# Test project"))` with these three lines (8 spaces at the start):

```python
        brief = generate_brief(data)
        self.assertTrue(brief.startswith("# Test project"))
        self.assertIn("- Build the first feature", brief)
```

11. Save everything and run the tests.
    *Check: `Ran 7 tests` and `OK`. If one fails, read the last lines of the error. It's usually a missing comma or wrong indentation.*
12. Run the app and check the new box appears, and its contents show up in the brief.

**Commit, pull request, review, merge**
13. `git add app.py validation.py brief_generator.py tests`
14. `git commit -m "Add suggested project tasks"`
15. `git push -u origin project-tasks`
16. Open a pull request into **main**. Title: `Add suggested project tasks`
17. Description: first line `Closes #6`. Then answer, in your own words: why did the tests fail at step 7, and what did you change to fix them?
18. Partner comment and reply. Merge only when **Tests** has a green tick. Then `git switch main` and `git pull`

**Done looks like**
- [ ] Pull request merged with a green **Tests** tick, and 7 tests passing
- [ ] Your explanation in the pull request description
- [ ] A comment from your partner, and your reply
