from peach.main import leblueprint
# from flask import render_template
# from peach.models.category import Expense, Account
# from flask.views import MethodView

# # from peach.models.category import Expense, Account, Wallet

# from flask import Flask, jsonify
# import flask
# import peach
# from peach.extensions import db

@leblueprint.route('/main')
def index():
    return 'This is The Main Blueprint'