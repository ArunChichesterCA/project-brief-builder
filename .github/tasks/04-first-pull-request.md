# Task 4: Your first pull request: improve the introduction
**Goal:** make one small change the way a real team does: branch, commit, pull request, review, merge.

**Make the change on a branch**
1. In your Codespace terminal, type `git switch -c improve-introduction`
   *Check: type `git status`. It says `On branch improve-introduction`.*
2. Open `app.py`. Find this line (near the top):
   `st.write("Turn a rough project idea into a clear, structured starting brief.")`
3. Change the words inside the quotes to: `Turn an early project idea into a clear, structured brief.`
4. Save with **Ctrl+S**. Run the app and check the new text appears. Press **Ctrl+C** to stop it.

**Commit and push**
5. Type these three commands, one at a time:
   - `git add app.py`
   - `git commit -m "Improve app introduction"`
   - `git push -u origin improve-introduction`

**Open the pull request**
6. On GitHub, open the **Pull requests** tab and click **New pull request**.
7. Set **base: main** and **compare: improve-introduction**. Click **Create pull request**.
8. Title: `Improve app introduction`
9. Description: first line `Closes #4`, then one sentence saying what you changed.
10. Click **Create pull request**.

**Review and merge**
11. Send your partner the link and ask them to leave one comment. Reply to it. Do the same for theirs.
12. Wait until the **Tests** check has a green tick. Then click **Merge pull request** and **Confirm merge**.
13. Back in the Codespace terminal: `git switch main`, then `git pull`

**Done looks like**
- [ ] Pull request merged with a green **Tests** tick
- [ ] A comment from your partner, and your reply
- [ ] This issue closes by itself when you merge (that's what `Closes #4` does)
