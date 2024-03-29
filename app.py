from flask import Flask , render_template, request
from flask_sqlalchemy import SQLAlchemy
import json



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/codingthunder'
app.config['SQLALCHEMY_BINDS'] = {
    'cart_details' : 'mysql://root:@localhost/cart_details',
}


db = SQLAlchemy(app) 


# This class defines a model with attributes for name, email, and phone number, with constraints for
# uniqueness and nullability.



class checker(db.Model):
    name = db.Column(db.String(20), primary_key=True, unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.Integer, unique=True, nullable=False)


class details(db.Model):
    __bind_key__ = 'cart_details'
    name = db.Column(db.String(30), primary_key=True, unique=True, nullable=False)
    address = db.Column(db.String(150), nullable=False)
    city = db.Column(db.String(20), nullable=False) 
    postalCode = db.Column(db.Integer, nullable=False) 
    country = db.Column(db.Integer, nullable=False)
    phoneNumber = db.Column(db.Integer,unique=True, nullable=False) 
    deliveryInstructions = db.Column(db.String(150), nullable=False) 
    paymentMode = db.Column(db.String(20) ,nullable=False) 


@app.route("/store")
def store():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('home.html')


@app.route("/user" , methods=['GET', 'POST'])
def contact():
    if(request.method=="POST"):
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('psw')
        
        
        entry = checker(name=name, password=password, email=email)
        db.session.add(entry)
        db.session.commit()
    return render_template('login.html')



@app.route("/info", methods=['GET', 'POST'])
def cart():
    if request.method == "POST":
        name = request.form.get('name')
        address = request.form.get('address')
        city = request.form.get('city')
        postalCode = request.form.get('postalCode')
        country = request.form.get('country')
        phoneNumber = request.form.get('phoneNumber')
        deliveryInstructions = request.form.get('deliveryInstructions')
        paymentMode = request.form.get('paymentMode')
        
        entry = details(name=name, address=address, city=city, postalCode=postalCode,country = country, phoneNumber=phoneNumber, deliveryInstructions=deliveryInstructions, paymentMode=paymentMode)
        db.session.add(entry)
        db.session.commit()
    return render_template("addtocart.html")


app.run(debug=True)



    
        
        
        














