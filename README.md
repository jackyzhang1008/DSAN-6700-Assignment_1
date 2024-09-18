# DSAN-6700-Assignment_1

project/
│
├── src/
│   ├── email_system/     # Module for Problem 3 (Email alert system)
│   │   ├
│   │   ├── mailer.py
│   │   └── alert.py
│   ├── ml_system/        # Module for Problem 4 (ML model training & inference)
│   │   ├── __init__.py
│   │   ├── train.py
│   │   ├── inference.py
│   │   └── visualize.py
├── tests/
│   ├── test_mailer.py    # Unit tests for email system (Problem 3)
│   └── test_train.py     # Unit tests for ML system (Problem 4)
├── README.md             # Unified README
├── pyproject.toml        # Poetry configuration file
└── .github/
    └── workflows/
        └── ci.yml        # Unified CI/CD workflow for both problems


# Project Title: Email Alert System

## Overview

This project provides an email alert system using a Python package that sends email notifications to users. The project is built with modern Python packaging techniques using `Poetry` and leverages `GitHub Actions` for Continuous Integration (CI). The email alert functionality is implemented through two Python scripts: `alert.py` and `mailer.py` under the directory `src/`. The `alert.py` script is responsible for sending email alerts, while the `mailer.py` script defines the email logic. The project also includes a pre-commit hook using `Ruff` to ensure that code is formatted correctly and adheres to best practices before it’s committed.

## Features

-   Send email alerts via a local SMTP server.
-   Structured as a Python package using `Poetry`.
-   Automatic formatting and linting using `pre-commit` hooks.
-   Continuous Integration (CI) pipeline with `GitHub Actions`.

### Steps

1.  Clone the repository:

    ``` 
    git clone https://github.com/jackyzhang1008/DSAN-6700-Assignment_1.git
    cd DSAN-6700-Assignment_1/problem_3
    ```

2.  Set up the virtual environment using Poetry: `poetry install`

3.  Start the local SMTP debugging server: `poetry run python -m smtpd -n -c DebuggingServer localhost:1025`

4.  In a separate terminal, run the email alert script: `poetry run python src/alert.py -s sender@example.com -r recipient@example.com -j "Subject" -b "Email Body` .After running the email alert script, the SMTP terminal will display the email message that was "sent." It won’t actually send the email, but you will see the details printed in the terminal.