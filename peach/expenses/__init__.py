from flask import Blueprint

expense_blueprint = Blueprint('expenses', __name__)


from peach.expenses import routes