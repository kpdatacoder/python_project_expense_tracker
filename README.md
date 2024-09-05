8# Expense and Savings Tracker

This is a simple GUI-based Python application that helps you track your daily income, expenses, and calculate savings. The app stores all data in a JSON file, allowing you to easily view and manage your financial logs.

## Features

- **Add Income**: Log your income with a description and amount.
- **Add Expense**: Track expenses with a description and amount.
- **Calculate Savings**: Automatically calculate your savings by subtracting total expenses from total income.
- **Display Logs**: View all your income, expense, and savings logs in a structured format.

## Project Structure

- `daily_expense_data.json`: Stores all the income, expense, and savings data.
- `main.py`: Contains the core functionality and GUI code for the application.

## Requirements

- Python 3.x
- `tkinter`: For the GUI (comes pre-installed with Python)

## How to Use

1. **Clone or Download** the repository to your local machine.
2. Install the required libraries (if necessary):
   ```bash
   pip install tk
   ```
3. Run the application:
   ```bash
   python main.py
   ```

### Adding Income
- Go to the **Add Income** tab.
- Enter the amount and a description, then click the **Add Income** button.

### Adding Expense
- Go to the **Add Expense** tab.
- Enter the amount and a description, then click the **Add Expense** button.

### Calculating Savings
- Go to the **Savings & Logs** tab.
- Click the **Calculate Savings** button to see your total savings.

### Viewing Logs
- Go to the **Savings & Logs** tab.
- Click the **Display Logs** button to view all your income, expense, and savings logs.

## Data Storage

All income, expense, and savings logs are stored in the `daily_expense_data.json` file in JSON format. This allows the data to persist even when the program is closed.

## Example Logs Format

```json
{
    "income_log": [
        {
            "date": "2024-09-05",
            "amount": 5000,
            "description": "Salary"
        }
    ],
    "expense_log": [
        {
            "date": "2024-09-05",
            "amount": 1500,
            "description": "Groceries"
        }
    ],
    "savings_log": [
        {
            "date": "2024-09-05",
            "total_savings": 3500
        }
    ]
}

