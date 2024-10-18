from peach.swagger_docs import swagger_blueprint


@swagger_blueprint.route('/swagger/')
def index():
    # all_expenses = Expense.query.all()

    # return render_template('index.html')
    return 'Swagger'