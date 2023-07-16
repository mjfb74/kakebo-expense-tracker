# Kakebo Expense Tracker

Kakebo Expense Tracker is a web application that allows users to keep track of their expenses and gain insights on their spending habits.

## Features

- **Expense Entry**: Enter individual expenses including category, amount, vendor, date, and a description.
- **Expense Summaries**: View a summary of total expenses for a specified month by category.
- **Category Details**: Click on a category in the summary view to see detailed information on expenses for that category in a particular month.

## Installation

To install the application, follow these steps:

1. Clone the repository:
    ```
    git clone https://github.com/mjfb74/kakebo-expense-tracker.git
    ```
2. Setup a virtual environment and activate it:
    ```
    python3 -m venv env
    source env/bin/activate
    ```
3. Install the required dependencies from the `requirements.txt` file:
    ```
    pip install -r requirements.txt
    ```
4. Run the Django server:
    ```
    python manage.py runserver
    ```

## Usage

The application includes the following paths:

- `/enter_expense/`: Visit this page to enter a new expense.
- `/get_sums/`: Visit this page to select a month and year and view the total sums of expenses for each category for that month.
- `/category_detail/<category>/<year>/<month>/`: Click on a category in the summary view to view detailed information on expenses in that category for the given month.
