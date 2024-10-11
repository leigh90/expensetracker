from flask import Blueprint

expense_blueprint = Blueprint('expense', __name__)


from peach.expenses import routes