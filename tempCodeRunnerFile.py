with open('config.json', 'r'):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/codingthunder'
    db = SQLAlchemy(app)