## Problem 2

In src/alert.py, handle sending email alerts.

In src/mailer.py, define the email logic.


A pre-commit hook is a tool that automatically runs scripts or commands before a commit is made to a Git repository. 

In our case, we are seeting up the pre-commit ussing 'Ruff', which is a Python linter that checks code quality and style, to ensure that your code is formatted correctly and adheres to best practices before it’s committed.

Using pre-commit hooks is useful because they enforce consistent code formatting and quality automatically, preventing issues from being committed to your repository.Pre-commit ensures that Ruff is run before you make a Git commit. If Ruff finds any issues, it will prevent the commit from being made until those issues are fixed.
