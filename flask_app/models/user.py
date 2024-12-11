from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
# from flask_app.models.cars import Car
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data) -> None:
        self.id=data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data["updated_at"]

    @classmethod
    def add(cls, data):
        query = "INSERT INTO users (first_name, last_name, email,password,created_at, updated_at) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s,NOW(),NOW());"
        result = connectToMySQL('TopStock').query_db(query,data)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('TopStock').query_db(query)
        users = []
        for u in results:
            users.append(cls(u))
        return users
    
    @classmethod
    def get_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('TopStock').query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s, updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL('TopStock').query_db(query,data)


    @classmethod
    def get_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('TopStock').query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @staticmethod
    def is_valid(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('TopStock').query_db(query,user)
        if len(result) > 1:
            flash("Email taken.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("email cann't be used")
            is_valid = False
        num = 1
        num2 = 8
        if len(user['first_name']) < num:
            flash("First name must be more than one charactor")
            is_valid = False
        if len(user['last_name']) < num:
            flash("Last name must be more than 1 charactor")
            is_valid = False
        if len(user['password']) < num2:
            flash("password must be at leat 8 charactor")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Password do not match")
        return is_valid
    
    @staticmethod
    def val_login(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('TopStock').query_db(query,user)
        return is_valid
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('TopStock').query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s, updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL('TopStock').query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('TopStock').query_db(query,data)
    

    # @classmethod
    # def get_car(cls, data):
    #     query = "SELECT * FROM users LEFT JOIN cars ON users.id=cars.user_id WHERE users.id=%(id)s"
    #     results = connectToMySQL('TopStock').query_db(query, data)
    #     car = cls(results[0])
    #     for cars in results: # We iterate through all items in our results
    #         car_data = {
    #             'id': cars['car.id'], 
    #             'user_id': cars['user_id'],
    #             'price': cars['price'],
    #             'model': cars['model'],
    #             'make': cars['make'],
    #             'year': cars['year'],
    #             'descriptions': cars['descriptions'],
    #             'created_at': cars['car.created_at'],
    #             'updated_at': cars['car.updated_at'],
    #             'user': None, 

    #         }
    #         this_car = cars.Car(car_data) 
    #         car.items.append(this_car) 
    #     return car 
