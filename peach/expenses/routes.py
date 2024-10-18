from . import expense_blueprint
from .models import Expense, Account

from .expenseview import register_expense_api
from .accountview import register_accounts_api

# TODO
# 1. View all expenses
# 2. View expenses by category
# 3. View expenses by date
# 4. View expenses by date

# 5. Get sum of expensesb by category
# 6. Get sum of expenses by category by time
# 7. Get sum of expenses in a time range. 



register_expense_api(expense_blueprint, Expense, "expenses")
register_accounts_api(expense_blueprint, Account, "accounts") 