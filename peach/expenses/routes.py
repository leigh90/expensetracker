from flask import render_template
from peach.expenses import expense_blueprint
from flask import jsonify, request
from peach.models.category import Expense
from flask.views import MethodView


@expense_blueprint.route('/', methods=['GET'])
def get_expenses():
    all_expenses = Expense.query.all()
    output = []
    for expense in all_expenses:
        expense_data = {"amount": expense.amount, "paid to": expense.payee, "item": expense.item, "Expense category": expense.category_name}
        output.append(expense_data)

    return {'expenses':output}

# def create_expense():
#     pass


class ExpenseView(MethodView):
    def get(self):
        data = Expense.query.all()
        return data
    
# peach.add_url_rule(
#     "/expenses/all_expenses"
# )









# @app.route('/drink/<id>')
# def get_drink(id):
#     drink = Drink.query.get_or_404(id)
#     print(type(drink))
#     print(request.json)
#     # output = []
#     # drinkone = jsonify(drink.name, drink.description)
#     # output = output.append(drinkone)
#     # return f"drink {output}"
#     return jsonify({drink.name:drink.description})
#     return ({"name":drink.name, "description":drink.description})


# @app.route('/drinks',methods=['POST'])
# def add_drink():
#     drink = Drink(name=request.json['name'],description=request.json['description'])
    
#     db.session.add(drink)
#     db.session.commit()
#     return {'id':drink.id}

# @app.route('/drinks/<id>', methods=["DELETE"])
# def delete_drink(id):
#     drink = Drink.query.get(id)
#     db.session.delete(drink)
#     db.session.commit()
#     return {'message': "Deleted!"}


# @app.route('/books')
# def get_books():
#     rep = jsonify({'books': books})
#     print(type(rep))
#     print(rep)
#     print(rep.headers)
#     print(rep.status_code)
#     data = dejsonify

#     normal = {'books':books}
 
#     return flask.Response(mimetype='application/json')