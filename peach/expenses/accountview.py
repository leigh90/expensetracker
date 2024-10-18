from peach.expenses import expense_blueprint

from flask import jsonify, request
from .models import  Account
from flask.views import MethodView




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
    
    # def post(self):
    #     db.session.add(self.model.from_json(flask.request.json))
    #     db.session.commit()
    #     return jsonify(item.to_json())

def register_accounts_api(app, model, name):
    accountitem = AccountsViewAPI.as_view(f"{name}", model)
    
    expense_blueprint.add_url_rule(f"/{name}/",view_func=accountitem)
    expense_blueprint.add_url_rule(f"/{name}/<int:account_id>",view_func=accountitem) 
    expense_blueprint.add_url_rule(f"/{name}/<string:account_name>",view_func=accountitem)
    # expense_blueprint.add_url_rule(f"/{name}/<string:account_id_no>",view_func=accountitem)
    # expense_blueprint.add_url_rule(f"/{name}/<string:account_type>",view_func=accountitem)
