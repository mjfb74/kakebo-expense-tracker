# Kakebo Expense Tracker

Kakebo Expense Tracker is a web application based on Django that allows users to keep track of their expenses. The name is inspired by the Japanese term Kakeibo, which stands for household finance ledger.

## Features
- Add new expense: Users can record each expense by entering the amount, selecting the category, and adding the vendor and a description.
- View expenses by category: The application displays the sum of expenses for each category in a specific month.
- Detail view: Clicking on a category in the summary view shows a detailed list of all expenses in that category for the chosen month.
- Edit and Delete functionality: The application allows users to edit or delete existing entries.
  
## Usage

The application includes the following paths:
- `/enter_expense/`: Visit this page to enter a new expense.
- `/get_sums/`: Visit this page to select a month and year and view the total sums of expenses for each category for that month.
- `/category_detail/<category>/<year>/<month>/`: Click on a category in the summary view to view detailed information on expenses in that category for the given month.
- `/expenses_list/`: This page displays all the expenses that have been recorded, ordered by date. Each entry includes links to edit or delete the entry.

## Installation and Setup

Please refer to the Django documentation on how to set up and run Django projects. This application uses SQLite as the database, which comes prepackaged with Django.

## Future Work

The application is still under development. Future updates will include features such as budgeting, graphical representation of data, and more.

Contributions are welcome. Please fork the repository and create a pull request with your changes.

## License

MIT
