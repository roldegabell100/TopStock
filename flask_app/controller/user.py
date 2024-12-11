from flask import render_template,request, redirect, session, flash, Request
from flask_app.controller.stock_api import reg_log
from flask_app import app 
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user import User

# home page route - done
@app.route('/')
def index():
    return redirect('/index')

# registration route - done
@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/register/new_user',methods=["POST"])
def new_user():
    if not User.is_valid(request.form):
        return redirect('/')
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.add(data)
    session['user_id'] = id
    return redirect('/dashboard')

# login - done
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login/access',methods=["POST"])
def access():
    user = User.get_email(request.form)
    if not user:
        flash("Invalid Email")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password,request.form['password']):
        flash("wrong password")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard/')

# dashboard route - done
@app.route('/dashboard/')
def home():
    if 'user_id' not in session:
        return redirect('/logout/')
    data = {
        "id":session['user_id']
    }
    return render_template("dashboard.html", user = User.get_id(data))

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')

# update user
@app.route('/edit/<int:id>')
def edit_user(id):
    data ={
        "id":id
    }
    return render_template("edit_user.html",user=User.get_one(data))

@app.route('/update/',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/dashboard/')

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id":id
    }
    User.delete(data)
    return redirect('/index')





# @app.route('/car')
# def car():
#     return render_template('add_car.html')

# new Car - done
# @app.route('/car/new/',methods=['POST'])
# def new_car():
#     car = {
#     "user_id": session['user_id'],
#     "price": request.form['price'],
#     "model": request.form['model'],
#     "make": request.form['make'],
#     "year": request.form['year'],
#     "descriptions": request.form['descriptions']
# }
#     Car.add_car(car)
#     return redirect('/home/')

# @app.route('/home <int:id>')
# def show_car_home():
#     car = Car.get_all_car(request.form)
#     data ={
#         "id":session['user_id']
#     }
    
#     return redirect("/home/")

# @app.route('/car/edit/<int:id>')
# def edit_car(id):
#     data ={
#         "id":id,
#     }
#     return render_template("edit_car.html",car=Car.get_id(data))

# @app.route('/car/update/' ,methods=['POST'])
# def update_car():
#     Car.update_car(request.form)
#     return redirect('/home/')





# @app.route('/car/show/<int:id>')
# def show_car(id):
#     data ={ 
#         'id': id,
#         'user_id': session["user_id"]
#     }
#     return render_template("show_car.html", car = Car.get_car_id(data), user = User.get_id(data))




# @app.route('/car/delete/<int:id>')
# def delete(id):
#     data = {
#         "id":id,
#     }
#     Car.delete(data)
#     return redirect('/home/')