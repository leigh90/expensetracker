# from flask import render_template, jsonify
from peach.expenses import expense_blueprint
import flask
from flask import jsonify, request
from .models import Expense
from flask.views import MethodView
from peach.extensions import db
import json



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

    # def post(self, aggregator_name: Text) -> flask.Response:    
    def post(self, payload=None):
        data = json.loads(flask.request.data.decode())
        # validation
        # breakpoint()
        new_expense = Expense(amount=data['amount'], payee=data['payee'], notes=data['notes'], item=data['item'], category_name=data['category_name'] )
        db.session.add(new_expense)
        db.session.commit()
        # breakpoint()
        new_expense= new_expense.to_json()
        # breakpoint()
        # return flask.Response(new_expense,mimetype='application/json', status=200)
        return new_expense

    
    def delete(self, id):
        expense = self.get(id=None)
        # breakpoint()
        db.session.delete(expense)
        db.session.commit()
        
        message = jsonify({"message":"Expense removed "})
        return jsonify(message)
        # return flask.Response(message ,mimetype='application/json', status=200)


    


def register_expense_api(app, model, name):
    expenseitem = ExpenseViewAPI.as_view(f"{name}", model)

    expense_blueprint.add_url_rule(f"/{name}/", view_func=expenseitem)
    expense_blueprint.add_url_rule("/new_expense/", view_func=expenseitem,methods = ['POST'])
    expense_blueprint.add_url_rule("/delete_expense/<int:id>", view_func=expenseitem,methods = ['DELETE'])

    expense_blueprint.add_url_rule(f"/{name}/<int:id>",view_func=expenseitem)
    expense_blueprint.add_url_rule(f"/{name}/<string:category_name>",view_func=expenseitem)
    expense_blueprint.add_url_rule(f"/{name}/<string:category_name>",view_func=expenseitem)

