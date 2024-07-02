from peach.main import leblueprint
from flask import render_template
from peach.models.category import Expense, Account, Wallet
from flask import Flask, jsonify
import flask

@leblueprint.route('/main/', methods=['GET'])
def get_expenses():
    all_expenses = Expense.query.all()
    all_accounts = Account.query.all()
    all_wallets = Wallet.query.all()


    expense_list = []
    for expense in all_expenses:
        expense_data = {"amount": expense.amount, "paid to": expense.payee, "item": expense.item, "Expense category": expense.category_name}
        expense_list.append(expense_data)

    wallet_list = []
    for wallet in all_wallets:
        wallet_data = {"Wallet": wallet.wallet_name, "Balance": wallet.wallet_balance}
        wallet_list.append(wallet_data)

    account_list = []
    for account in all_accounts:
        account_data = {"Account": account.name, "Balance": account.account_balance}
        account_list.append(account_data)

    # response = {{'expenses':expense_list},{'wallets':wallet_list}, {'accounts':account_list}}

    # response = jsonify(response)

    # todo 
    # fix response
    # what do you actually want to see?
    # lIKE THE VIEWS LIKE the views homepage, expenses page, accounts_page, 
    

    # return flask.Response(response,mimetype="application/json", status=200)
    return [{'expenses':expense_list},{'wallets':wallet_list}, {'accounts':account_list}]