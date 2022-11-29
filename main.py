import os
from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json


with open('templates/config.json', 'r') as c:
    params = json.load(c)["params"]

local_sever=True 
app = Flask(__name__)
app.secret_key = 'super-secret-key'


if local_sever:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False #signal limiting k lye use hota
else:
    # when we used production uri
     app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app) 

#databse connection 
class Contacts(db.Model):
    # sno ,name, phone_num, msg, date, email
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(20),  nullable=False)
    phone_num = db.Column(db.String(11), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(120), nullable=True)

class Orders(db.Model):
    # sno	firstname	lastname	phonenum email	address	article_name	color	city	zip_	state	date	
    sno = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), unique=False, nullable=False)
    lastname = db.Column(db.String(11), unique=False, nullable=False)
    phonenum = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(20),  nullable=False)
    address = db.Column(db.String(50),  nullable=False)
    article_name = db.Column(db.String(20),  nullable=False)
    color = db.Column(db.String(20),  nullable=False)
    city = db.Column(db.String(20),  nullable=False)
    zip_ = db.Column(db.String(10), nullable=False)
    state = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(120), nullable=True)


@app.route("/")
def home():

    return render_template('mainPage.html',params=params)

@app.route("/order/", methods = ['POST', 'GET'])
def order():
    # sno	firstname	lastname	phonenum email	address	article_name	color	city	zip_	state	date	
    if(request.method=="POST"):
        #add entry to database
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        phonenum=request.form['phonenum']
        email=request.form['email']
        address=request.form['address']
        article_name=request.form['article_name']
        color=request.form['color']
        city=request.form['city']
        zip_=request.form['zip_']
        state=request.form['state']
        if len(firstname)==0 and len(lastname)==0 and len(phonenum)==0 and len(address)==0 :
            
            return redirect("/contact") 
        # flash("zain here","success")
        admin = Orders(firstname=firstname, lastname=lastname, phonenum=phonenum,email=email,address=address,
        color=color,city=city,zip_=zip_,state=state,article_name=article_name, date= datetime.now())
        db.session.add(admin)
        db.session.commit()
        

    return render_template('order.html',params=params)




@app.route("/contact/", methods = ['POST', 'GET'])
def contact():
    
    if(request.method=="POST"):
        #add entry to database
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        message=request.form['message']
        if len(name)==0 and len(email)==0 and len(phone)==0 and len(message)==0 :
            
            return redirect("/contact") 
        # flash("zain here","success")
        admin = Contacts(name=name, phone_num=phone, date= datetime.now(), msg=message,email=email)
        db.session.add(admin)
        db.session.commit()
        
        
    return render_template('contact.html',params=params)


@app.route("/gents/")
def gents():
    return render_template('gents.html',params=params)



@app.route("/girls/")
def girls():
    return render_template('girls.html',params=params)




@app.route("/kids/")
def kids():
    return render_template('kids.html',params=params)


@app.route("/household/")
def household():
    return render_template('household.html',params=params)


@app.route("/grocery/")
def grocery():
    return render_template('grocery.html',params=params)











        









if __name__=="__main__":
    app.run(debug=False)








