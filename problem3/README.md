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

    ``` bash
    git clone https://github.com/jackyzhang1008/DSAN-6700-Assignment_1.git
    cd DSAN-6700-Assignment_1/problem3
    ```

2.  Set up the virtual environment using Poetry: `bash poetry install`

3.  Start the local SMTP debugging server: `bash poetry run python -m smtpd -n -c DebuggingServer localhost:1025`

4.  In a separate terminal, run the email alert script: `bash poetry run python src/alert.py`