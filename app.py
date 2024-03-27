from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

    
app = Flask(__name__)


db = SQLAlchemy(app)

class checker(db.Model):
    name = db.Column(db.String(20), primary_key = True, unique = True, nullable = False)
    email = db.Column(db.String(20), unique = True, nullable = False)
    phone = db.Column(db.String(12), unique = True, nullable = False)



@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/store")
def home():
    return render_template("home.html")





@app.route("/info" , methods = ['GET', 'POST'])
def contact():
    if(request.method=="POST"):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        
        
        entry = checker(name=name, phone=phone, email=email)
        db.session.add(entry)
        db.session.commit()

        
        
    return render_template("contact.html")


app.run(debug=True)