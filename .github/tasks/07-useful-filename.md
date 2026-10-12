# Task 7: Feature: a useful download filename
**Goal:** downloaded briefs are all called `project_brief.md` at the moment. Make the filename match the project title, and test it.

**Start a branch**
1. `git switch main`, then `git pull`
2. `git switch -c useful-filename`

**Add the function**
3. Open `brief_generator.py`. Go to the very **end** of the file, add a blank line, then paste:

```python
def safe_filename(title):
    """Turn a project title into a safe download filename."""
    characters = []
    for character in title.lower():
        if character.isalnum():
            characters.append(character)
        elif character in {" ", "-", "_"}:
            characters.append("-")
    name = "".join(characters).strip("-")
    return f"{name or 'project'}-brief.md"
```

**Use it in the app**
4. Open `app.py`. Change `from brief_generator import generate_brief` to:
   `from brief_generator import generate_brief, safe_filename`
5. Find `file_name="project_brief.md",` and change it to:
   `file_name=safe_filename(title),`

**Add two tests**
6. Open `tests/test_brief_generator.py`. Change the first import line to:
   `from brief_generator import as_bullets, generate_brief, safe_filename`
7. Just **above** `if __name__ == "__main__":`, paste (4 spaces at the start):

```python
    def test_filename_uses_title(self):
        self.assertEqual(safe_filename("Room Booking Helper"), "room-booking-helper-brief.md")

    def test_empty_title_still_gives_filename(self):
        self.assertEqual(safe_filename(""), "project-brief.md")
```

8. Save and run the tests. *Check: `Ran 9 tests` and `OK`.*
9. Run the app with the title `Room Booking Helper`, build the brief and download it.
   *Check: the file is called `room-booking-helper-brief.md`.*
10. Now try the title `Tea & Biscuits`. Look at the filename you get.

**Commit, pull request, review, merge**
11. `git add app.py brief_generator.py tests`
12. `git commit -m "Create useful brief filenames"`
13. `git push -u origin useful-filename`
14. Open a pull request into **main**. Title: `Create useful brief filenames`
15. Description: first line `Closes #7`. Then answer: what filename did `Tea & Biscuits` give? Is that OK, and how might you improve it?
16. Partner comment and reply. Merge only when **Tests** has a green tick. Then `git switch main` and `git pull`

**Done looks like**
- [ ] Pull request merged with a green **Tests** tick, and 9 tests passing
- [ ] Your answer about `Tea & Biscuits` in the pull request description
- [ ] A comment from your partner, and your reply
