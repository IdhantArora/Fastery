from flask import Flask,render_template,Response,request
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField,SubmitField
from wtforms.validators import DataRequired
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from sqlalchemy.orm import session
from flask import flash
from flask import redirect, url_for
from  flask_login import UserMixin
# from . import db    
from flask_mysqldb import MySQL
# from flask_mysqldb import MySQL
from datetime import date
import time
import json
# from flask import jsonify  
from flask import Flask, json

#Create a flask instance
app=Flask(__name__)
app.config['SECRET_KEY']="123"
#add datadb
# app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:sqlPass@localhost/market_management"#"sqlite:///user.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# #Initialize the db
# db=SQLAlchemy(app)

# app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:sqlPass@localhost/market_management"
# db=SQLAlchemy(app)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sqlPass'
app.config['MYSQL_DB'] = 'market_management'
db = MySQL(app)


#Create Model
# class Customer(db.Model,UserMixin):
#     __tablename__ = 'customer'
#     customer_id = Column(Integer, primary_key=True, autoincrement=True)
#     customer_name = Column(String(50), nullable=False)
#     customer_phone = Column(String(12), nullable=False)
#     customer_email = Column(String(255), nullable=False)
#     customer_password = Column(String(250), nullable=False)
#     customer_address = Column(String(255), nullable=False)
#     customer_card = Column(String(12))

# class Orders(db.Model):
#     __tablename__ = 'orders'
#     order_id = Column(Integer, primary_key=True, autoincrement=True)
#     order_date = Column(Date, nullable=False)
#     order_time = Column(Time, nullable=False)
#     order_amount = Column(Integer, nullable=False)
#     items_total = Column(Integer, nullable=False)
#     customer_id = Column(Integer, ForeignKey('customer.customer_id'), nullable=False)
#     customer = relationship('Customer')

#     def __init__(self, order_date, order_time, order_amount, items_total, customer_id):
#         if order_amount <= 0:
#             raise ValueError("Order amount must be greater than 0")
#         if items_total <= 0:
#             raise ValueError("Items total must be greater than 0")
#         self.order_date = order_date
#         self.order_time = order_time
#         self.order_amount = order_amount
#         self.items_total = items_total
#         self.customer_id = customer_id
        
# class Transactions(db.Model):
#     __tablename__ = 'transactions'
#     trans_id = Column(Integer, primary_key=True, autoincrement=True)
#     trans_type = Column(String(1), nullable=False)
#     trans_date = Column(Date, nullable=False)
#     trans_time = Column(Time, nullable=False)
#     trans_status = Column(String(1), nullable=False)
#     trans_amount = Column(Integer, nullable=False)
#     order_id = Column(Integer, ForeignKey('orders.order_id'), nullable=False)
#     order = relationship('Orders')

#     def __init__(self, trans_type, trans_date, trans_time, trans_status, trans_amount, order_id):
#         if trans_amount <= 0:
#             raise ValueError("Transaction amount must be greater than 0")
#         self.trans_type = trans_type
#         self.trans_date = trans_date
#         self.trans_time = trans_time
#         self.trans_status = trans_status
#         self.trans_amount = trans_amount
#         self.order_id = order_id

# class Shipper(db.Model):
#     __tablename__ = 'shipper'
#     shipper_id = Column(Integer, primary_key=True, autoincrement=True)
#     shipper_pin = Column(Integer, nullable=False)
#     shipper_name = Column(String(50), nullable=False)
#     shipper_phone = Column(String(12), nullable=False)
#     shipper_address = Column(String(100), nullable=False)

# class Supply(db.Model):
#     __tablename__ = 'supply'
#     order_id = Column(Integer, ForeignKey('orders.order_id'), primary_key=True, nullable=False)
#     shipper_id = Column(Integer, ForeignKey('shipper.shipper_id'), primary_key=True, nullable=False)
#     delivery_date = Column(Date)
#     supply_status = Column(String(1), nullable=False)
#     order = relationship('Orders')
#     shipper = relationship('Shipper')

# class Category(db.Model):
#     __tablename__ = 'category'
#     cat_id = Column(Integer, primary_key=True, autoincrement=True)
#     cat_name = Column(String(20), nullable=False)

# class Products(db.Model):
#     __tablename__ = 'products'
#     prod_id = Column(Integer, primary_key=True, autoincrement=True)
#     prod_name = Column(String(40), nullable=False)
#     cat_id = Column(Integer, ForeignKey('category.cat_id'), nullable=False)
#     category = relationship('Category')
#     quantity = Column(Integer, nullable=False)
#     price = Column(Integer, nullable=False)

#     def __init__(self, prod_name, cat_id, quantity, price):
#         if quantity <= 0:
#             raise ValueError("Quantity must be greater than 0")
#         if price <= 0:
#             raise ValueError("Price must be greater than 0")
#         self.prod_name = prod_name
#         self.cat_id = cat_id
#         self.quantity = quantity
#         self.price = price

# class Warehouse(db.Model):
#     __tablename__ = 'warehouse'
#     house_id = Column(Integer, primary_key=True, autoincrement=True)
#     house_address = Column(String(50), nullable=False)
#     pincode = Column(Integer, nullable=False)

# class Manager(db.Model):
#     __tablename__ = 'manager'
#     manager_id = Column(Integer, primary_key=True, autoincrement=True)
#     house_id = Column(Integer, ForeignKey('warehouse.house_id'), nullable=False)
#     warehouse = relationship('Warehouse')
#     manager_name = Column(String(30), nullable=False)
#     manager_phone = Column(String(12), nullable=False)
#     manager_address = Column(String(50), nullable=False)
#     manager_pass = Column(String(20), nullable=False)

# class Inventory(db.Model):
#     __tablename__ = 'inventory'
#     prod_id = Column(Integer, ForeignKey('products.prod_id'), primary_key=True, nullable=False)
#     house_id = Column(Integer, ForeignKey('warehouse.house_id'), primary_key=True, nullable=False)
#     product = relationship('Products')
#     warehouse = relationship('Warehouse')
#     quantity = Column(Integer, nullable=False)

#     def __init__(self, prod_id, house_id, quantity):
#         if quantity <= 0:
#             raise ValueError("Quantity must be greater than 0")
#         self.prod_id = prod_id
#         self.house_id = house_id
#         self.quantity = quantity

# class Collects(db.Model):
#     __tablename__ = 'collects'
#     order_id = Column(Integer, ForeignKey('orders.order_id'), primary_key=True, nullable=False)
#     collect_date = Column(Date, nullable=False)
#     shipper_id = Column(Integer, ForeignKey('shipper.shipper_id'), nullable=False)
#     house_id = Column(Integer, ForeignKey('warehouse.house_id'), nullable=False)
#     order = relationship('Orders')
#     shipper = relationship('Shipper')
#     warehouse = relationship('Warehouse')

# class Cart(db.Model):
#     __tablename__ = 'cart'
#     customer_id = Column(Integer, ForeignKey('customer.customer_id'), primary_key=True, nullable=False)
#     prod_id = Column(Integer, ForeignKey('products.prod_id'), primary_key=True, nullable=False)
#     quantity = Column(Integer, nullable=False)
#     customer = relationship('Customer')
#     product = relationship('Products')

# class Purchases(db.Model):
#     __tablename__ = 'purchases'
#     order_id = Column(Integer, ForeignKey('orders.order_id'), primary_key=True, nullable=False)
#     prod_id = Column(Integer, ForeignKey('products.prod_id'), primary_key=True, nullable=False)
#     quantity = Column(Integer, nullable=False)
#     order = relationship('Orders')
#     product = relationship('Products')


# class CustomerForm(FlaskForm):
#     '''
#     customer_id = Column(Integer, primary_key=True, autoincrement=True)
#     customer_name = Column(String(50), nullable=False)
#     customer_phone = Column(String(12), nullable=False)
#     customer_email = Column(String(255), nullable=False)
#     customer_password = Column(String(250), nullable=False)
#     customer_address = Column(String(255), nullable=False)
#     customer_card = Column(String(12))
#     '''
#     customer_name=StringField("Name",validators=[DataRequired()])
#     customer_phone=StringField("Phone number",validators=[DataRequired()])
#     customer_email=StringField("Email",validators=[DataRequired()])
#     customer_password=StringField("Enter Password",validators=[DataRequired()])
#     customer_address=StringField("Enter address",validators=[DataRequired()])
#     submit=SubmitField("Signup")

class NamerForm(FlaskForm):
    name=StringField("Enter user name",validators=[DataRequired()])
    submit=SubmitField("Submit")

#Create a route decorator
@app.route('/')

def index():
    return render_template("LoginPage.html")


@app.route('/user/<name>')
def home(name):
    return render_template("home.html",user_name=name)
    # resp = Response("5")
    # resp.headers['Access-Control-Allow-Origin'] = '*'
    # return resp
    # return '5'

@app.route("/name",methods=['GET','POST'])
def name():
    name=None
    form=NamerForm()
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=''
    return render_template("name.html",name=name,form=form)

@app.route("/user/signup",methods=['GET','POST'])
def signup():
    customer_name=None
    customer_phone=None
    customer_email=None
    customer_password=None
    customer_address=None
    form=CustomerForm()
    if form.validate_on_submit():
        user1=Customer.query.filter_by(customer_email=form.customer_email.data).first()
        user2=Customer.query.filter_by(customer_phone=form.customer_phone.data).first()
        
        customer_name=form.customer_name.data
        customer_phone=form.customer_phone.data
        customer_email=form.customer_email.data
        customer_password=form.customer_password.data
        customer_address=form.customer_address.data

        if user1 is None and user2 is None:
            customer=Customer(customer_name=form.customer_name.data,customer_phone=form.customer_phone.data,customer_email=form.customer_email.data,customer_password=form.customer_password.data,customer_address=form.customer_address.data)
            db.session.add(customer)
            db.session.commit()

            # Clear form fields after successful submission
            form.customer_name.data = ''
            form.customer_phone.data = ''
            form.customer_email.data = ''
            form.customer_password.data = ''
            form.customer_address.data = ''
            
    customer_table=Customer.query.order_by(Customer.customer_id)

    return render_template("signup.html",customer_name=customer_name,
                           customer_phone=customer_phone,customer_email=customer_email,
                           customer_password=customer_password,customer_address=customer_address,
                           form=form,customer_table=customer_table)


class LoginForm(FlaskForm):
    email_or_phone = StringField("Email or Phone Number", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

@app.route("/user/login", methods=['POST'])
def login():
    print("Inside fn")
    resp = Response("5")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    # return resp
    body = request.get_json()
    print(body)
    user = body['user']
    passw = body['password']

    cursor = db.connection.cursor()

    query = f"select c_pass from customer where customer_name = '{user}'"
    cursor.execute(query)
    data = cursor.fetchall()
    # print(data[0][0])
    if (len(data) != 0):
        data = data[0][0]
    else:
        data = ""

    if (data == passw):
        query11 = f"select is_blocked from customer where customer_name = '{user}'"
        cursor.execute(query11)
        checker = cursor.fetchall()
        print(checker)
        checker = checker[0][0]
        print(checker)
        print(type(checker))
        if (checker == 1):
            resp = Response("3")
            print("in checker")
        else:
            resp = Response("1")
            query100 = f"update failedLogin set attempts = 0 where customer_name = '{user}'"
            cursor.execute(query100)
            db.connection.commit()
            resp.headers['Access-Control-Allow-Origin'] = '*'
    
    elif (len(data) > 0):
        # cursor = db.connection.cursor()
        query0 = f"select attempts from failedLogin where customer_name = '{user}'"
        cursor.execute(query0)
        at = cursor.fetchall()
        print(at)
        at = at[0][0]
        print(at)
        at = at + 1
        print(at)
        print(user)
        query10 = f"update failedLogin set attempts = {at} where customer_name = '{user}'"
        cursor.execute(query10)
        db.connection.commit()
        resp = Response("2")
    
    else:
        resp = Response("0")
        resp.headers['Access-Control-Allow-Origin'] = '*'

    if True:
        # Authentication successful, redirect to a new page
        # For demonstration, let's redirect to the index page
        # return redirect(url_for('index'))
        # return redirect(f'http://127.0.0.1:5000/user/hritik')
        return resp
    else:
        flash('Invalid email/phone or password. Please try again.', 'error')

@app.route("/product/<id>", methods=['GET', 'POST'])
def getProduct(id):
    # return 1
    cursor = db.connection.cursor()

    query = f"SELECT prod_name,price FROM products WHERE prod_id = {id}"

    # Execute the query with cursor
    cursor.execute(query)
    data = cursor.fetchall()
    
    if (int(data[0][1]) > 10):
        return "yes"
    else:
        return "no"
    data = str(data[0])
    print((data))
    
    return data


@app.route("/items/<user>", methods=['GET', 'POST'])
def item(user):
    return render_template("items.html",user=user)
# def getProduct(id):
#     # return 1
#     cursor = db.connection.cursor()

#     query = f"SELECT prod_name,price FROM products WHERE prod_id = {id}"

#     # Execute the query with cursor
#     cursor.execute(query)
#     data = cursor.fetchall()
    
#     if (int(data[0][1]) > 10):
#         return "yes"
#     else:
#         return "no"
#     data = str(data[0])
#     print((data))
    
#     return data


# @app.route("/login/user/test", methods=['GET', 'POST'])
# def getProducts(id):
#     # return 1

#     cursor = db.connection.cursor()

#     query = f"SELECT prod_name,price FROM products WHERE prod_id = {id}"

#     # Execute the query with cursor
#     cursor.execute(query)
#     data = cursor.fetchall()
    
#     if (int(data[0][1]) > 10):
#         return "yes"
#     else:
#         return "no"


@app.route("/buy/<item>", methods=['GET', 'POST'])
def buying(item):
    cursor = db.connection.cursor()

    query0 = f"select quantity from products where prod_id = {item}"

    cursor.execute(query0)

    quan = cursor.fetchall()
    
    quan = int(quan[0][0])

    # print(quan)

    # query = "CREATE TRIGGER quancheck BEFORE INSERT ON people FOR EACH ROW IF NEW.age < 0 THEN SET NEW.age = 0"

    if (quan > 10):

        # print("Going in")
        # quan = quan - 1
        # query1 = "update products set quantity = %s where prod_id = %s"
        # cursor.execute(query1, (quan, item))
        # db.connection.commit() 

        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        today = date.today()
        # user = localStorage.getItem("fastery_user")
        body = request.get_json()
        user = body['user']
        query2 = f"select customer_id from customer where customer_name = '{user}'"
        cursor.execute(query2)
        d = cursor.fetchall()
        d = int(d[0][0])

        query3 = f"select price from products where prod_id = {item}"
        cursor.execute(query3)
        price = cursor.fetchall()
        price = int(price[0][0])

        query4 = f"insert into orders(order_date, order_time, order_amount, items_total,customer_id) values ('{today}', '{current_time}', {price}, 1, {d})"
        cursor.execute(query4)
        db.connection.commit()
        resp = Response("1")
        resp.headers['Access-Control-Allow-Origin'] = '*'

        query5 = f"select order_id from orders where order_date = '{today}' and order_time = '{current_time}' and customer_id = {d}"
        cursor.execute(query5)
        id = cursor.fetchall()
        id = id[0][0]

        query6 = f"insert into purchases(order_id, prod_id, quantity) values ({id}, {item}, 1)"
        cursor.execute(query6)
        db.connection.commit()

        # db.connection.commit()


        return resp
    else:
        resp = Response("0")
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    


@app.route("/admin", methods=['GET', 'POST'])
def admin():
    return render_template("random.html")

@app.route("/getPrice/<item>", methods=['GET', 'POST'])
def getPrice(item):
    cursor = db.connection.cursor()

    query0 = f"select price from products where prod_id = {item}"

    cursor.execute(query0)

    price = cursor.fetchall()
    
    price = int(price[0][0])


    

    # print(quan)
    # print(price)

    l = f"{price}"
    print(l)
    # body: JSON.stringify(l)
    resp = Response(l)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route("/getQuantity/<item>", methods=['GET', 'POST'])
def getQuantity(item):
    cursor = db.connection.cursor()


    query0 = f"select quantity from products where prod_id = {item}"

    cursor.execute(query0)

    quan = cursor.fetchall()
    
    quan = int(quan[0][0])

    # print(quan)
    # print(price)

    l = f"{quan}"
    print(l)
    # body: JSON.stringify(l)
    resp = Response(l)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp



    # data = {
    #     "quantity": quan,
    #     "price": price
    # }

    # Convert data to JSON string (if desired)
    # response_data = jsonify(data)  # Use l if data is not defined
    # response_data = Response(data)

    # Set CORS header (consider restricting origins in production)
    # response_data.headers['Access-Control-Allow-Origin'] = '*'

    # return response_data
    # return jsonify(data)
# @app.route("/getQuan/item", methods=['GET', 'POST'])
# def getPrice(item):
#     cursor = db.connection.cursor()

#     query0 = f"select quantity from products where prod_id = {item}"

#     cursor.execute(query0)

#     quan = cursor.fetchall()
    
#     quan = int(quan[0][0])

#     resp = Response(quan)
#     resp.headers['Access-Control-Allow-Origin'] = '*'
#     return resp
