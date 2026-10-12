# Task 9: Use your app for real: write a brief for your next project
**Goal:** use the app you've built to plan a real project. The best brief may become what you build next, so make it good.

**The idea:** an *Innovation tool finder*: a simple page or app that helps ACCA staff find the right innovation tool for a job. It builds on the tool pages you wrote for the SharePoint site.

**Steps**
1. Before using the app, write some notes. Think about: who would use it? What problem does it solve for them? What *must* it do, and what can wait?
2. `git switch main`, then `git pull`, then `git switch -c tool-finder-brief`
3. Run the app and fill in every box using your notes. Use real tool names, but **no client or case information**.
4. Build the brief and download it.
5. In the Codespace, drag the downloaded file into the `briefs` folder.
6. `git add briefs`
7. `git commit -m "Add innovation tool finder brief"`
8. `git push -u origin tool-finder-brief`
9. Open a pull request into **main**. Title: `Add innovation tool finder brief`. Description: first line `Closes #9`, then one sentence on the hardest decision you made (for example, what you left out of scope).
10. Ask your partner to review it: is anything vague, or missing? Reply, and improve the brief if they're right.
11. Merge when **Tests** has a green tick.

**Done looks like**
- [ ] Your brief merged into the `briefs` folder
- [ ] Every section filled in with your own thinking
- [ ] Partner comment, and your reply
