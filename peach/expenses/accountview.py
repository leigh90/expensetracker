from peach.expenses import expense_blueprint
import flask
from flask import jsonify, request
from .models import  Account
from flask.views import MethodView
from peach.extensions import db
import json



class AccountsViewAPI(MethodView):
    init_every_request = False

    def __init__(self, model):
        self.model = model

    def get(self, account_id=None, account_name=None, account_type=None, account_id_no=None, **kwargs):
        if account_id:
            print(account_id)
            accounts =  Account.query.filter(Account.id==account_id)
            return jsonify([item.to_json() for item in accounts])
        elif account_name: 
            accounts = Account.query.filter(Account.name== account_name)
            return jsonify([item.to_json() for item in accounts])
        elif account_type: 
            accounts = Account.query.filter(Account.type.name==type)
            return jsonify([item.to_json() for item in accounts])
        elif account_id_no: 
            accounts = Account.query.filter(Account.identification_number==account_id_no)
            return jsonify([item.to_json() for item in accounts])
        else:
            accounts = self.model.query.all()
            return jsonify([accnt.to_json() for accnt in accounts])
    
    def post(self, payload=None):
        data = json.loads(flask.request.data.decode())
        # validation
        # breakpoint()
        new_account = Account(name=data['name'], identification_number=data['id_no'], type=data['type'], balance=data['balance'] )
        db.session.add(new_account)
        db.session.commit()
        # breakpoint()
        new_account = new_account.to_json()
        # return flask.Response(new_account,mimetype='application/json', status=200)
        return new_account
    
    def delete(self, account_id):
        account = self.get(account_id)
        db.session.delete(account)
        db.session.commit()
        
        message = {"message":"Account removed"}
        return flask.Response(message, mimetype='application/json', status=200)

 

def register_accounts_api(app, model, name):
    accountitem = AccountsViewAPI.as_view(f"{name}", model)
    
    expense_blueprint.add_url_rule(f"/{name}/",view_func=accountitem)
    expense_blueprint.add_url_rule("/new_account/", view_func=accountitem,methods = ['POST'])
    expense_blueprint.add_url_rule("/delete_account/<int:account_id>", view_func=accountitem,methods = ['DELETE'])

    expense_blueprint.add_url_rule(f"/{name}/<int:account_id>",view_func=accountitem) 
    expense_blueprint.add_url_rule(f"/{name}/<string:account_name>",view_func=accountitem)
