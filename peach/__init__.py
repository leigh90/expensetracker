from flask import Flask
from peach.extensions import db
# from flask_restful import Resource, Api
from config import Config

def create_app(config_class=Config):
    peach = Flask(__name__)
    peach.config.from_object(config_class)
    

    # Initiate flask extensions  here 
    db.init_app(peach)
    # api = Api(peach)

    # Register blueprints here
    from peach.main import leblueprint as main_bp
    peach.register_blueprint(main_bp)

    from peach.expenses import expense_blueprint  as expense_bp
    peach.register_blueprint(expense_bp,url_prefix='/expenses' )


    @peach.route('/test/')
    def test_page():
        return '<h2> Testing the flask application factory pattern</h2>'
    
    return peach
