from flask import Flask
from peach.extensions import db
# from flask_restful import Resource, Api
from config import Config
from flask_migrate import Migrate
from flask_cors import CORS

def create_app(config_class=Config):
    peach = Flask(__name__)
    CORS(peach)
    peach.config.from_object(config_class)
    peach.config['CORS_HEADERS'] = "Content-Type"

    cors = CORS(peach, resources={r"/expenses/*": {"origins": "*"}})
    
    # Initiate flask extensions  here 
    db.init_app(peach)
    migrate = Migrate(peach, db)
    # api = Api(peach)

    # Register blueprints here
    from peach.main import leblueprint as main_bp
    peach.register_blueprint(main_bp, url_prefix='/main')

    from peach.expenses import expense_blueprint  as expense_bp
    peach.register_blueprint(expense_bp,url_prefix='/expenses' )

    from peach.swagger_docs import swagger_blueprint as swagger_bp
    peach.register_blueprint(swagger_bp,url_prefix='/swagger')

    @peach.route('/test/')
    def test_page():
        return '<h2> Testing the flask application factory pattern</h2>'
    
    return peach
