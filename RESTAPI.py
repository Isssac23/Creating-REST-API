import json, requests
from flask import Flask, request, jsonify
app = Flask(__name__)

#The initial user data which is being inputted to the API
users_list = [
    {
        "id": 0,
        "name": "Is-haaq Omar",
        "age": "23",
        "DOB": "10 aprill 2000",
    },
]

#Displaying default text on API
@app.route("/")
def index():
    return "Hi!"

#Creating GET and POST request functions to be able to retreive and upload new users data
@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        if len(users_list) > 0:
            return jsonify(users_list)
        else:
            'Nothing Found', 404

    if request.method == 'POST':
        new_name = request.form['name']
        new_age = request.form['age']
        new_DOB = request.form['DOB']
        iD = users_list[-1]['id']+1

        new_obj = {
            'id' : iD,
            'name' : new_name,
            'age' : new_age,
            'DOB' : new_DOB,
        }
        users_list.append(new_obj)
        with open('data.json', 'w') as f:  #Function to retrieve and store data from API to json file while server is running
            json.dump(users_list, f)
        return jsonify(users_list), 201
    
#Creating GET, PUT, and DELETE request functions to be able to modify the data using the user id    
@app.route('/user/<int:id>', methods= ['GET', 'PUT', 'DELETE'])
def single_user(id):
    if request.method == 'GET':
        for user in users_list:
            if user['id'] == id:
                with open('data.json', 'w') as f:
                    json.dump(users_list, f)
                return jsonify(user)
            pass
    if request.method == 'PUT':
        for user in users_list:
            if user['id'] == id:
                user['name'] = request.form['name']
                user['age'] = request.form['age']
                user['DOB'] = request.form['DOB']
                updated_user = {
                    'id': id,
                    'name': user['name'],
                    'age': user['age'], 
                    'DOB': user['DOB']
                }
                with open('data.json', 'w') as f:
                    json.dump(users_list, f)
                return jsonify(updated_user)
    if request.method == 'DELETE':
        for index, user in enumerate(users_list):
            if user['id'] == id:
                users_list.pop(index)
                with open('data.json', 'w') as f:
                    json.dump(users_list, f)
                return jsonify(users_list)    


if __name__ == '__main__':
    app.run()
