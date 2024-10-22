# # 1. View all expenses
# @expense_blueprint.route('/', methods=['GET'])
# def get_expenses():
#     all_expenses = Expense.query.all()
#     output = []
#     for expense in all_expenses:
#         expense_data = {"amount": expense.amount, "paid to": expense.payee, "item": expense.item, "Expense category": expense.category_name}
#         output.append(expense_data)
    
#     # response = jsonify({all_expenses})
#     print(output)

#     return output

# # 2. View expenses by category
# @expense_blueprint.route('/category/<category_name>', methods=['GET'])
# def get_expense_by_category(category_name):
#     category_name = category_name.capitalize()
    
#     # get category from url
#     # retrieve it from the db
#     #  check list of expenses where expense.category_name == categoryfromurl
#     all_categories = Category.query.all()
#     # print(all_categories)
#     category_list = []
#     for single_category in all_categories:
#         # print({"id":single_category.id, "name":single_category.name}) 
#         category_list.append(single_category.name)
#         # print(category_list)
#     # Check if category exists
#     if category_name not in category_list:
#         print(f'Category {category_name} does not exist')

#     # return aal
#     all_expenses = Expense.query.all()
#     expense_list = []
#     amount_list = []
#     for expense in all_expenses:
#         if expense.category_name == category_name:
#             expense_data = {"amount": expense.amount, "paid to": expense.payee, "item": expense.item}
            
#             amount_list.append(float(expense.amount))
#             # sum_of_expenses = sum(amount_list)
#             # print(sum_of_expenses)
#             expense_list.append(expense_data)

    
#     print(sum(amount_list))
#     total_category_sum = sum(amount_list)
#     return {'category_name':expense_list, "Total":total_category_sum }

# # @expense_blueprint.route('/category/<category_name>', methods=['GET'])
# # def sum_of_expenses()
# @expense_blueprint.route('/by_time/<date_string>', methods=['GET'])
# def get_expense_by_date(date_string):
#     date_string = parser.parse(date_string)


#     # '2024-07-05 14:53:24.322837+03'
#     # '2024-07-05 14:53:24.322837+03'
#     all_expenses = Expense.query.filter_by(created_at=date_string).all()
#     # all_expenses = Expense.query.filter(Expense.created_at.dateutil.parser.isoparse.date()=date_string).all()

#     # expense_list = []
#     # amount_list = []
#     for expense in all_expenses:
#         expense_data = {"amount": expense.amount, "paid to": expense.payee, "item": expense.item}
#             # amount_list.append(expense.amount)
#             # sum_of_expenses = sum(amount_list)
#             # print(sum_of_expenses)
#         # expense_list.append(expense_data)

    
#     # print(amount_list)
#     return all_expenses


           

        


# class ExpenseView(MethodView):
#     def get(self):
#         data = Expense.query.all()
#         return data
    
# # peach.add_url_rule(
# #     "/expenses/all_expenses"
# # )









# # @app.route('/drink/<id>')
# # def get_drink(id):
# #     drink = Drink.query.get_or_404(id)
# #     print(type(drink))
# #     print(request.json)
# #     # output = []
# #     # drinkone = jsonify(drink.name, drink.description)
# #     # output = output.append(drinkone)
# #     # return f"drink {output}"
# #     return jsonify({drink.name:drink.description})
# #     return ({"name":drink.name, "description":drink.description})


# # @app.route('/drinks',methods=['POST'])
# # def add_drink():
# #     drink = Drink(name=request.json['name'],description=request.json['description'])
    
# #     db.session.add(drink)
# #     db.session.commit()
# #     return {'id':drink.id}

# # @app.route('/drinks/<id>', methods=["DELETE"])
# # def delete_drink(id):
# #     drink = Drink.query.get(id)
# #     db.session.delete(drink)
# #     db.session.commit()
# #     return {'message': "Deleted!"}


# # @app.route('/books')
# # def get_books():
# #     rep = jsonify({'books': books})
# #     print(type(rep))
# #     print(rep)
# #     print(rep.headers)
# #     print(rep.status_code)
# #     data = dejsonify

# #     normal = {'books':books}
 
# #     return flask.Response(mimetype='application/json')



# [{'amount': Decimal('540'), 'paid to': 'Samosa', 'item': 'Java', 'Expense category': 'Food'}, {'amount': Decimal('100'), 'paid to': 'Airtime', 'item': 'Safaricom', 'Expense category': 'Utilities'}, {'amount': Decimal('75000'), 'paid to': 'JLNGRD Investments', 'item': 'Rent', 'Expense category': 'Utilities'}, {'amount': Decimal('50'), 'paid to': 'Matatu', 'item': 'Matatu Fare', 'Expense category': 'Transport'}, {'amount': Decimal('20'), 'paid to': 'Matatu', 'item': 'Matatu Fare', 'Expense category': 'Transport'}, {'amount': Decimal('20'), 'paid to': 'Matatu', 'item': 'Matatu Fare', 'Expense category': 'Transport'}, {'amount': Decimal('200'), 'paid to': 'Uber', 'item': 'Cab fare', 'Expense category': 'Transport'}]

# class ExpenseListView(MethodView):


#     # def get(self, user.id: Text) -> flask.Response:
#     def get(self) -> flask.Response:
    
#         # onject = flask.request.args.get("thekey", None)
#         # amount = flask.request.args.get("amount", None)
#         all_expenses = Expense.query.all()
#         expense_list = []
#         for expense in all_expenses:
#             expense_data = {"amount": expense.amount, "paid to": expense.payee, "item": expense.item, "Expense category": expense.category_name}
#             expense_list.append(expense_data)



#         response = jsonify({"status": "SUCCESS",'expenses':expense_list })
#         return response
#         # return flask.Response(response, mimetype="application/json", status=200)
    
# leblueprint.add_url_rule("/expenses/",view_func=ExpenseListView.as_view("all-expenses"))



    
    # def post(self):
    #     # errors = self.validator.validate(flask.request.json)

    #     # if errors:
    #     #     return jsonify(errors), 400

    #     db.session.add(self.model.from_json(flask.request.json))
    #     db.session.commit()
    #     return jsonify(item.to_json())
    



    
    # def post(self):
    #     # errors = self.validator.validate(request.json)

    #     # if errors:
    #     #     return jsonify(errors), 400

    #     db.session.add(self.model.from_json(request.json))
    #     db.session.commit()
    #     return jsonify(item.to_json())


        
        







# class CreateExpenseView(MethodView):
#     def post(self, aggregator_name: Text) -> flask.Response:
#         request_body = dejsonify(flask.request.data)
#         response = jsonify({"status": "SUCCESS"})
#         return flask.Response(response, mimetype="application/json")

# leblueprint.add_url_rule("/expenses/",view_func=ExpenseListView.as_view("all-expenses"))

# def create_blueprint(at_prefix: str, **kwargs: Any) -> flask.Blueprint:
#     # blueprint = flask.Blueprint("peach", __name__)
#     leblueprint.add_url_rule(
#         "/expenses/",
#         view_func=ExpenseListView.as_view("all-expenses"),
#     )
#     leblueprint.add_url_rule(
#         "/expenses/",
#         view_func=CreateExpenseView.as_view("add-expenses"),
#     )
#     return leblueprint





# @leblueprint.route('/main/', methods=['GET'])
# # @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
# def get_expenses():
#     all_expenses = Expense.query.all()
#     all_accounts = Account.query.all()
#     # all_wallets = Wallet.query.all()


#     expense_list = []
#     for expense in all_expenses:
#         expense_data = {"amount": expense.amount, "paid to": expense.payee, "item": expense.item, "Expense category": expense.category_name}
#         expense_list.append(expense_data)

#     # wallet_list = []
#     # for wallet in all_wallets:
#     #     wallet_data = {"Wallet": wallet.wallet_name, "Balance": wallet.wallet_balance}
#     #     wallet_list.append(wallet_data)

#     # account_list = []
#     # for account in all_accounts:
#     #     account_data = {"Account": account.name, "Balance": account.account_balance}
#     #     account_list.append(account_data)

#     # response = {{'expenses':expense_list},{'wallets':wallet_list}, {'accounts':account_list}}

#     # response = jsonify(response)

#     # todo 
#     # fix response
#     # what do you actually want to see?
#     # lIKE THE VIEWS LIKE the views homepage, expenses page, accounts_page, 
    

#     # return flask.Response(response,mimetype="application/json", status=200)
#     # return [{'expenses':expense_list},{'wallets':wallet_list}, {'accounts':account_list}]
#     return [{'expenses':expense_list}]
