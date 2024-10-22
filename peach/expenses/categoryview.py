from peach.expenses import expense_blueprint
import flask
from flask import jsonify, request
from .models import Category
from flask.views import MethodView
from peach.extensions import db
import json


class CategoryViewAPI(MethodView):
    init_every_request = True

    
    def __init__(self, model):
        self.model = model


    def _get_item(self, id):
        return self.model.query.get_or_404(id)
    
    def get(self, category_name=None, id=None, **kwargs ):
        if category_name:
            categories = Category.query.filter(Category.name==category_name)
            
            return jsonify([item.to_json() for item in categories])
        elif id: 
            categories = Category.query.filter(Category.id==id)
            return jsonify([item.to_json() for item in categories])
        else:
            categories = self.model.query.all()
            return jsonify([item.to_json() for item in categories])
            

    # def post(self, aggregator_name: Text) -> flask.Response:    
    def post(self, payload=None):
        data = json.loads(flask.request.data.decode())
        new_category = Category(name=data['name'] )
        db.session.add(new_category)
        db.session.commit()
        new_category= new_category.to_json()
        # return flask.Response(new_category,mimetype='application/json', status=200)
        return new_category

    
    def delete(self, id):
        category = self.get(id=None)
        # breakpoint()
        db.session.delete(category)
        db.session.commit()
        
        message = jsonify({"message":"Category removed "})
        return jsonify(message)
        # return flask.Response(message ,mimetype='application/json', status=200)

def register_category_api(app, model, name):
    categoryitem = CategoryViewAPI.as_view(f"{name}", model)

    expense_blueprint.add_url_rule(f"/{name}/", view_func=categoryitem)
    expense_blueprint.add_url_rule("/new_category/", view_func=categoryitem,methods = ['POST'])
    expense_blueprint.add_url_rule("/delete_category/<int:id>", view_func=categoryitem,methods = ['DELETE'])

    expense_blueprint.add_url_rule(f"/{name}/<int:id>",view_func=categoryitem) 
    expense_blueprint.add_url_rule(f"/{name}/<string:category_name>/",view_func=categoryitem)

