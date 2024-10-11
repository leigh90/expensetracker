# from flask import render_template, jsonify
# from peach.expenses import expense_blueprint
# from flask import jsonify, request
# from peach.models.category import Expense, Category
# from flask.views import MethodView
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



from peach.expenses import expense_blueprint
from peach.expenses.models import Expense, Account
from flask.views import MethodView

# from peach.models.category import Expense, Account, Wallet

from flask import Flask, jsonify
import flask
import peach
from peach.extensions import db

class ExpenseView(MethodView):
    init_every_request = False

    
    def __init__(self, model):
        self.model = model
        # self.validator = flask.generate_validator(model)
    
    def get(self):
        items = self.model.query.all()
        return jsonify([item.to_json() for item in items])
    

class AccountsView(MethodView):
    init_every_request = False

    def __init__(self, model):
        self.model = model

    def get(self):
        accounts = self.model.query.all()
        return jsonify([accnt.to_json() for accnt in accounts])
    
    # def post(self):
    #     db.session.add(self.model.from_json(flask.request.json))
    #     db.session.commit()
    #     return jsonify(item.to_json())


def register_api(app, model, name):
    expenseitem = ExpenseView.as_view(f"{name}-item", model)
    accountitem = AccountsView.as_view(f"{name}-froup", model)

    expense_blueprint.add_url_rule(f"/{name}/",view_func=expenseitem)
    expense_blueprint.add_url_rule(f"/{name}/",view_func=accountitem)



register_api(peach, Expense, "expenses")
register_api(peach, Account, "accounts") 