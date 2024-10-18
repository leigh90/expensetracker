# from flask import render_template, jsonify
from peach.expenses import expense_blueprint

from .expenseview import ExpenseViewAPI
from flask import jsonify, request
from .models import Expense
from . import expenseview
from flask.views import MethodView
# import datetime
# import dateutil
# from dateutil import parser 

# # TODO
# # 1. View all expenses
# # 2. View expenses by category
# # 3. View expenses by date
# # 4. View expenses by date

# # 5. Get sum of expensesb by category
# # 6. Get sum of expenses by category by time
# # 7. Get sum of expenses in a time range. 


class ExpenseViewAPI(MethodView):
    init_every_request = True

    
    def __init__(self, model):
        self.model = model
    
    def get(self, category_name=None, id=None, **kwargs ):
        if category_name:
            expenses = Expense.query.filter(Expense.category_name==category_name)
            return jsonify([item.to_json() for item in expenses])
        elif id: 
            expenses = Expense.query.filter(Expense.id==id)
            return jsonify([item.to_json() for item in expenses])
        else:
            expenses = self.model.query.all()
            return jsonify([item.to_json() for item in expenses])
        

def register_api(app, model, name):
    expenseitem = ExpenseViewAPI.as_view(f"{name}", model)

    expense_blueprint.add_url_rule(f"/{name}/", view_func=expenseitem)
    expense_blueprint.add_url_rule(f"/{name}/<int:id>",view_func=expenseitem)
    expense_blueprint.add_url_rule(f"/{name}/<string:category_name>",view_func=expenseitem)

expenseview.register_api(expense_blueprint, Expense, "expenses")
# register_api(expense_blueprint, Account, "accounts") 