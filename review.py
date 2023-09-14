"""
This is a multi line comment
"""

#Variable Declaration

my_preffered_coding_language='react'


x = 10
if x > 50:
    print('I win')
else:
    print("i lose")
    x = 20
print(x)



#Booleans
garretts_hungry = True
if garretts_hungry == True:
    print('Feed gARRETT')
else:
    print("garrett not hungry")
    

age = 28
weight= 162.0

name='Garrett'


#TUPLE IS IMMUTABLE

Badass_person= ("Garrett", "Coder", "Real Estate Investor", "Diver")
print(Badass_person[1], "ftw")

# Lists

empty_list=[]
sharks = ['chomper', 'big bite', 'jaws']
print(sharks[2])
print(sharks)
sharks[2]='Garrett'
print(sharks)

#Dioctionaries

empty_dictioanry = {}
new_person={'name':"Garrett", 'age': 28, 'weight': 160, 'is_a_badass':True}
print(new_person)

new_person['name']="Gustavo"
new_person['salary']=120000

print(new_person)
print(len(new_person))

#NUMBERS INTS TO FLOATS ETC, using 'type'

float = 3.14

number = 4

sum = number + int(float)
print( type(sum), sum)

#concatination

print("hello " + str(42))

total = 16
user_val = '11'
total = total + int(user_val)
print(total)


#F Strings
first_name = 'Garrett'
last_name = "Turner"
age= 28
print(f"My name is {first_name} {last_name} and I am {age} years old")

print("my name is {} {} and i am {} yeards old".format(first_name, last_name, age))

#%formatting

hw="hello %s" % "world"
py = "I love Python %d" % 3
print(hw, py)

#Built in method

x = "hELLO WORLD"
print(x.title())

#Commonly used string methds
# string.upper(), string.lower(), 
# string.split(char) -- this splits it at a specific character
# string.join(list)


#Lists

homies = ['Matt', 'Jay', 'Varun']
#they dont have to be the same datatypes\

homies_overview = [ '3', ['Matt', 'Jay', 'Varun']]

fruits = ['apple', 'banana']
veggies = ['onion', 'pepper']
fruits_and_veggies = fruits + veggies
print(fruits_and_veggies)

#slicing

numbered_list = [2,4,8,16,32,64,128]
print(numbered_list[1:])
print(numbered_list[:4])
print(numbered_list[2:4])

#other built ins include 'enumerate', 'map'
#enumerate = returns 2 item tuple for each item in the list indicating what item and also at which index
#map = applies the function to every item in the sequence you pass in, returns a list of the results
#min(sequence) = returns lowest value
#sorted(sequence) = returns a sorted sequence

#Dictionaries

#built ins - .clear(), .copy(), .keys(), .values()

#For loops in mainly dictionaries

for x in "hello":
    print(x)

food = {'cooked': 'shrimp', 'raw': 'sushi'}
for value in food:
    print(food.keys())
    print(food['cooked'])
    print(food['raw'])
    print(food.values())

for key, value in food.items():
    print(key, "=", value)

for val in 'string':
    if val == 'i':
        continue
    print(val)

def add(a,b):
    x = a + b
    return x

new_value = add(3,5)
print(new_value)

def say_hi(name):
    return "Hi " + name

greeting = say_hi("Garrett")
print(greeting)



#OOP REVIEW

# we reviewed the 4 pillars, encapsulation, inheritance, abstraction, polymorphism
#Inheritance usues .super() to borrow attributes, you just have to pass in the other classname as a parameter so its called upon
#Abstraction is very similar to encapsulation because it does encapsulate functionality but only in certain n

#OOP 

# DRY(dont repeat yourself, OOP)

#everything in our coding world is an object, anything in the world can be an object... a Tree has properties and 
# # behaviors, like props: trunk, leaves, branches, roots. and Behaviors such as; grows, sways, produces fruit, makes and drops leaves 

#Methods give functionality to our attributesa and behaviors
#You define an object with a class, creating a class
# a class is  nearly a blueprint to what i want to do, has attributes in which are variables, has methods, or what it can do, its functionality
#you create instances of objects with the blueprint, or the class properties.
#each instance inherits attributes and methods
#you can make attributes or methods PRIVATE, 
#instances can inherit whatever the parent class has, you can identify additional attributes and methods in your child class
#METHODS CAN BE PUBLIC/PRIVATE/PROTECTED---Protected are methods that are public but go unseen
class User:
#self is a reference to the instance not the class
#right below is a class attribute
    bank_name= "Bank of hawaii"

    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 20000



    def make_deposit(self, amount):
        self.account_balance += amount

    def display_user_balance(self):
        print(f"User:{self.name}. Balance:{self.account_balance}")
        
        
        
garrett = User("Garrett Turner", "GarrettTurnerProductions@gmail.com")
print(garrett.name)
print(garrett.account_balance)
garrett.make_deposit(100)
print(garrett.account_balance)
garrett.display_user_balance()


#---------------------------------------#

#DATABASE DESIGN AND MYSQL

#-------OneToOne Relationship --

#You must refernce them with a foreign key, like customers to addresses, 
# you can refernece a customers whole address by the address ID attached to the customer


# SELECT * FROM customers 
# JOIN addresses ON addresses.id = customers.address_id;


#-------OneToMany Relationship --

#Customers can place many orders, setting up a foreign key,
#in this relationship you want to make sure the ID is within the table of many

# SELECT * FROM orders 
# JOIN customers ON customers.id = orders.customer_id;


#-------ManyToMany Relationship --

#Orders to Items
#orders can have many items and items can show up on many orders
#One specific thing will be referenced by 2 diff ID's, order ID and item ID


#QUERIES------ QUERIES--------------

#ive been practcing using limit and offset and insert and Update & Where 

# UPDATE table_name
# SET column1 = value1, column2 = value2, ...
# WHERE condition;


# SELECT * FROM orders 
# JOIN items_orders ON orders.id = items_orders.order_id 
# JOIN items ON items.id = items_orders.item_id;


#SET SQL_SAFE_UPDATES = 0;    - This tells SQL that you are going to run DELETE commands from the database

SET SQL_SAFE_UPDATES = 0;

#------------ SQL Functions -----------------#

#Ex's)  CONCAT(), LENGTH(), LOWER()
#SELECT CONCAT("Mr."m first_name, " ", last_name) AS full_name FROM clients
#SELECT LENGTH(last_name) AS last_length FROM clients;
#MONTH(), HOUR(), DATE_FORMAT()
#SELECT NOW() AS right_now;
#SELECT DATE_FORMAT()

#Multiple table Join Query

#SELECT clients.first_name, clients.last_name, sites.domain_name, leads.first_name
#FROM clients
#JOIN sites ON clients.id = sites.clients_id
#JOIN leads ON sites.id = leads.sites_id;

#LEFT JOIN
#this will pull up all the data on the left side without havinbg matching info, SQL returns NULL

# SELECT clients.first_name, clients.last_name, sites.domain_name
# FROM clients
# LEFT JOIN sites ON clients.id = sites.clients_id

# GROUP BY EXAMPLE W built-in Fuinction SUM(), also, AVG()

# when we use group by we should always use some sort of a function

# SELECT clients.first_name, SUM(billing.amount),
# FROM clients
# JOIN billing ON clients.id = billings.clients_id
# GROUP BY clients.id;

#GROUP_CONCAT()


#Find total number of leads from each site

# SELECT COUNT(leads.id), sites.domain_name
# FROM sites
# JOIN leads ON sites.id = leads.sites_id
# GROUP BY site.id



#----------------------FLASKKKK    FLASKKKKKKK------


#from flask import flask

#app = Flask(__name__)

# @app.route('/')
# def index():
#     return "Hello World"

#-- This is whats considered a path variable
# whatever the path variable name is, it just needs to match whats in the return statement
# always default to being strings but we can do it with flask, with built ins
# you can identify path variables in the @app.route call itself
# EX
# app.route('/hello/<string:banana>/<int:num>')
# def hello(banana, num):
#   return f"Hello {banana * num}"


# @app.route('/hello/<banana>')
# def hello():
#   return f"Hello {banana}


# @app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
# def show_user_profile(username, id):
#     print(username)
#     print(id)
#     return "username: " + username + ", id: " + id



# @app.route('/play/<int:num>/<string:color>')
# def playAlot(num, color):
#     return render_template("index.html", num = num, color = color)


#-----------CHECKERBOARD EXAMPLE ASSIGNEMNT

# @app.route ('/<int:num>/<int:colnum>/<color1>/<color2>')
# def diffSetup(num,colnum,color1,color2):
#     return render_template('index4th.html', num = num, col = colnum, color = color1, diffcolor = color2 )

# <body>
#     <table>
#         {% for x in range(num)%}
#             <tr>
#                 {% for y in range(col)%}
#                     {% if (x+y) % 2%}
#                         <td style="background-color: {{ color }}"> </td>
#                     {% else %}
#                         <td style="background-color: {{ diffcolor }}"> </td>
#                     {% endif %}
#                 {% endfor %}
#             </tr>
#         {% endfor %}
#     </table>
# </body>




# --------------FORM SUBMISSION ------------------------#

# FORM data we access via POST dat, by naming conventions,
# In post requests we CANNOT render_template, we only redirect to another route

# <h3> index page</h3>
# <form action='/users' method='post'>
#     <label for= 'name'>Name:</label>
#     <input type="text" name='name'
# </form>

#form_test/server.py

# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     print(request.form)
#     # Never render a template on a POST request.
#     # Instead we will redirect to our index route.
#     return redirect('/')


# We went Over session and how to transfer data between request.form to session and manipulate it,
# but never store sensitive info in session

#-------------CRUD ---------------------

#Passing or injecting variables into our render temlates through our models
#we write variable data because we dont want to hard code it
# when we want to write a query that include variables we should use a preparred statement 
# rather than string interpolation

#EX ) instead of f strings or string concatination we use preparred statements 
#query = "UPDATE friends SET first_name=%(fn)s WHERE id=%(id_num)s;"
#data = {
    # "fn": maybe a value from a form,
    # "id_num": possibly a value from the URL,
#}
#mysql.query_db(query,data)




#ANOTHER PREPARRED STATEMENT EXAMPLE

# query = "SELECT * FROM users WHERE email = %(email)s;"
# data = { 'email' : request.form['email'] }
# result = mysql.query_db(query, data)

#This is utilizing SQL injection with jinja2 syntax 

#LAZY CODING BELOW AND WHY WE DONT USE STRING INTERPOLATION

# query = f"SELECT * FROM users WHERE email = '{request.form['email']}';"
# result = mysql.query_db(query)

#This will insert this into the DB like so....we dont want that

# SELECT * FROM users WHERE email = 'joe@gmail.com' OR '1'='1'; 

#EXAMPLES OF SQL Injection in which we want to avoid
# 1. joe@gmail.com"; DROP TABLE users;
# 2. query = f"SELECT * FROM users WHERE email = '{request.form['email']}';"
    #result = mysql.query_db(query)
        # the query it would run would look like this, 
        # SELECT * FROM users WHERE email = "joe@gmail.com";  DROP users;

# What if the user passed the following as their email input?
# joe@gmail.com"; UPDATE users SET password = '____' WHERE id = '___'

# This would have changed someone's password. Similarly, you can see how one could set oneself to be an admin
# or retrieve sensitive information from other users table (e.g. credit card, address, etc). The possibilities are endless.



# Let's definitely stick with running queries by using the following pattern 
# any time user input is concerned:

# query = "SELECT * FROM users WHERE email = %(email)s;"
# data = {
    # 'email': request.form['email]
    # }
    #result = mysql.query_db(query, data)


#    UNION


# ------------- CRUD IN MODELS SETUP
# friend.py

#from mysqlconnection import connectToMySQL

#class friend:
    # @classmethod
    # def save(cls, data):
    # query = "INSERT INTO friends ( first_name, last_name, occupation) VALUES ( %(fname)s, %(lname)s, $(occ)s);"
#data is a dictioanry that will passed into the save method from our server.py
#this query uses variables, so we should use a preparred statment so our jinja2 can interpret
    # return connectToMySQL('first_flask').query_db(query, data)




# ----------FULL CRUD  from front end template and server file

#front end HTML

# <h1>Add a Friend</h1>
# <form action="/create_friend" method="POST">
#     <label for="fname">First Name:</label>
#     <input type="text" name="fname">
#     <label for="lname">Last Name:</label>
#     <input type="text" name="lname">
#     <label for="occ" >Occupation:</label>
#     <input type="text" name="occ">
#     <input type="submit" value="Add Friend">
# </form> 

#back end server.py

#from friend import friend
#app.route('/create_friend', methods=["POST"])
#def create_friend():

#since our request.form is a data dictionary with the names of our inputs we can use it
# as our data dictionary that we pass to the save method
# data = {
#     "fname": request.form["fname"],
#     "lname": request.form["lname"],
#     "occ": request.form["occ"]
# }
# Friend.save(request.form)
#   return redirect('/')

# BASIC Table EXAMPLE

# <form action= "/create_friend", method="post"
# <form action="/create_friend" method="POST">
#     <label for="fname">First Name:</label>
#     <input type="text" name="fname">
#     <label for="lname">Last Name:</label>
#     <input type="text" name="lname">
#     <label for="occ" >Occupation:</label>
#     <input type="text" name="occ">
#     <input type="submit" value="Add Friend">
# </form> 
# </form>
# <table>
#     <thead>
#         <tr>
#             <th>
#             <th>
#             <th>
#         </tr>
#     </thead>
#     <tbody>
#         {% for one_friend in friends %}
#         <tr>
#             <th> {one_friend.first_name}</th>
#             <th> {one_friend.last_name}</th>
#             <th> {one_friend.occupation}</th>
#         </tr>
#         {% endfor %}
#     </tbody>
    




#------ CRUD FUNCTION RAN BETWEEN OUR MODELS AND CONTROLLERS -------- #

#READ 

# class Friend:
#         def __init__(self, data):
#             self.id = data['id']
#             self.first_name = data['first_name']
#             self.last_name = data['last_name']
#             self.occupation = data['occupation']
#             self.created_at = data['created_at']
#             self.updated_at = data['updated_at']
#         # the get_all method will be used when we need to retrieve all the rows of the table 
#         @classmethod
#         def get_all(cls):
#             query = "SELECT * FROM friends;"
#             results = connectToMySQL('first_flask').query_db(query)
#             friends = []
#             for friend in results:
#                 friends.append( cls(friend) )
#             return friends
#         # the get_one method will be used when we need to retrieve just one specific row of the table
#         @classmethod
#         def get_one(cls,id):
#             query  = "SELECT * FROM friends WHERE id = %(id)s";
#             result = connectToMySQL('first_flask').query_db(query, {'id':id})
#             return cls(result[0])



# @app.route('/')
# def index():
#     # calling the get_all method from the friends.py
#     all_friends=Friend.get_all()
#     # passing all friends to our template so we can display them there
#     return render_template("index.html",friends=all_friends)
# @app.route('/friend/show/<int:id>')
# def show(id):
#     # calling the get_one method and supplying it with the id of the friend we want to get
#     friend=Friend.get_one(id)
#     return render_template("show_friend.html",friend=friend)



#CREATE 

# class Friend:
#     def __init__(self, data):
#         self.id = data['id']
#         self.first_name = data['first_name']
#         self.last_name = data['last_name']
#         self.occupation = data['occupation']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']
        
#     # the save method will be used when we need to save a new friend to our database
#     @classmethod
#     def save(cls, data):
#         query = "INSERT INTO friends (first_name,last_name,occupation) VALUES (%(first_name)s,%(last_name)s,%(occ)s);"
#         result = connectToMySQL('first_flask').query_db(query,data)
#         return result


# @app.route('/friend/create', methods=['POST'])
# def create():
#     Friend.save(request.form)
#     return redirect('/')




#UPDATE


# class Friend:
#     def __init__(self, data):
#         self.id = data['id']
#         self.first_name = data['first_name']
#         self.last_name = data['last_name']
#         self.occupation = data['occupation']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']
        
#     # the update method will be used when we need to update a friend in our database
#     @classmethod
#         def update(cls,data, id):
#             query = f"UPDATE friends SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s 
#                     WHERE id = {id};"
#             return connectToMySQL('first_flask').query_db(query,data)


# @app.route('/friend/update/<int:id>',methods=['POST'])
# def update(id):
#     Friend.update(request.form, id)
#     return redirect('/users')



#DELETE

# class Friend:
#     def __init__(self, data):
#         self.id = data['id']
#         self.first_name = data['first_name']
#         self.last_name = data['last_name']
#         self.occupation = data['occupation']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']
        
#     # the delete method will be used when we need to delete a friend from our database
#     @classmethod
#     def delete(cls, id):
#         query  = f"DELETE FROM friends WHERE id = {id};"
#         return connectToMySQL('first_flask').query_db(query)



# @app.route('/friend/delete/<int:id>')
# def delete(id):
#     Friend.delete(id)
#     return redirect('/')



# FLASK & PYMYSQL QUESTIONS


# 1.The query_db() method may return:
#A list of dictionaries where each dictionary represents a row in the table

# 2.  The query_db() method returns _______________ when we run an insert query.
# The row ID

#3.  Why sanitize user input data?
# To prevent against SQL injection

#4 What does the query_db() method return when we run an update or delete query?
# NOTHING


#5 . What does the query_db() method return if our query does not execute correctly?
# False


#------------VALIDATIONS & EMAIL REGEX ------------------#
# A regex is a sequence of characters that defines a search pattern. 
# r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'


#---MODEL----#
#import re	# the regex module
# create a regular expression object that we'll use later   

# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
# class User:
#     @staticmethod
#     def validate_user( user ):
#         is_valid = True
#         # test whether a field matches the pattern
#         if not EMAIL_REGEX.match(user['email']): 
#             flash("Invalid email address!")
#             is_valid = False
#         return is_valid

# The EMAIL_REGEX object has a method called .match() 
# that will return None if no match can be found. 
# If the argument matches the regular expression, 
# a match object instance is returned.

#--------CONTROLLER-----------#

# from flask_app.models.user import User
# @app.route('/register', methods=['POST'])
# def register():
#     if not User.validate_user(request.form):
#         # we redirect to the template with the form.
#         return redirect('/')
#     # ... do other things
#     return redirect('/dashboard')

#-----------------
# flash("Email cannot be blank!", 'email')