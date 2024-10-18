# from flask import render_template, jsonify
from peach.expenses import expense_blueprint

from flask import jsonify, request
from .models import Expense
from flask.views import MethodView


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
        
    # def post(self):
    #     # errors = self.validator.validate(request.json)

    #     # if errors:
    #     #     return jsonify(errors), 400

    #     db.session.add(self.model.from_json(request.json))
    #     db.session.commit()
    #     return jsonify(item.to_json())
    


def register_expense_api(app, model, name):
    expenseitem = ExpenseViewAPI.as_view(f"{name}", model)

    expense_blueprint.add_url_rule(f"/{name}/", view_func=expenseitem)
    expense_blueprint.add_url_rule(f"/{name}/<int:id>",view_func=expenseitem)
    expense_blueprint.add_url_rule(f"/{name}/<string:category_name>",view_func=expenseitem)
