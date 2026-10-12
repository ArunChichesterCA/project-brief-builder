# Task 2: Run the tests, then break one on purpose
**Goal:** see what automated tests do, and what a failing test looks like.

**Steps**
1. In your Codespace terminal, type `python -m unittest discover -s tests -v` and press Enter.
   *Check: the last lines say `Ran 6 tests` and `OK`.*
2. Open `validation.py`. Change `"Project title"` to `"Project name"`. Save with **Ctrl+S**.
3. Run the tests again (press the up arrow, then Enter).
   *Check: now some tests FAIL. Read the error message.*
4. Change `"Project name"` back to `"Project title"` and save.
5. Run the tests again.
   *Check: `Ran 6 tests` and `OK` again.*

Don't commit anything for this task.

**Done looks like**
- [ ] A comment on this issue with a screenshot of all 6 tests passing
- [ ] In the same comment, one or two sentences in your own words: which tests failed in step 3, and why?

Then click **Close issue**.
