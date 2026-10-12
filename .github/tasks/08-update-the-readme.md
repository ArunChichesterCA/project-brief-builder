# Task 8: Write the README
**Goal:** a README tells the next person what the project is and how to use it. Write it for someone who has never seen the app.

**Steps**
1. `git switch main`, then `git pull`
2. `git switch -c update-readme`
3. Open `README.md`. **Replace** the "How this project works" and "Rules" sections with three new sections, written in your own words:
   - `## What the app does`: two or three sentences
   - `## How to use it`: how to run it, and what to type in the form
   - `## Known limitations`: at least two things it can't do yet
4. Keep the "Useful commands" section.
5. Click the preview icon (top right of the file) to check the headings and lists look right.
6. `git add README.md`
7. `git commit -m "Write README for new users"`
8. `git push -u origin update-readme`
9. Open a pull request into **main**. Title: `Write README for new users`. Description: first line `Closes #8`.
10. Ask your partner to read it as if they'd never seen the app, and comment on one thing that's unclear. Fix it if they're right.
11. Merge when **Tests** has a green tick. Then `git switch main` and `git pull`

**Done looks like**
- [ ] Pull request merged with the three new sections, in your own words
- [ ] Partner comment, and your reply or fix
